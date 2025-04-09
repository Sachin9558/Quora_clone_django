from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def User_Signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username Already Taken")
            return redirect('signup')
        
        User.objects.create_user(username=username,email=email,password=password)
        messages.success(request, "Account Created Successfully!")
        return redirect ('login')
    
    return render(request, "Auth_user_app/user_signup.html")

def User_login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('question_list')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    
    return render(request,"Auth_user_app/user_login.html")

def User_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, "Auth_user_app/dashboard.html")
    
        
