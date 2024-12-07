from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password  = request.POST['password']
        password2  = request.POST['password2']
        user_type = 'admin'
        
        check = True if CustomUser.objects.filter(email=email).exists() else False
        if check: 
           return HttpResponse("user Exists")
            
        if password2 != password:
            messages.error(request, 'Passwords do not match')
            return HttpResponse("passwords do not match")
        
        try:
            user = CustomUser.objects.create_user(username=username, email=email, user_type=user_type, password=password)
            user.superuser = True
            user.save()
        except:
            return HttpResponse("User creation fail")
        
        messages.success(request, 'Account Registered Successfuly')
        return redirect('authentication:login')
    
    return render(request,'login/register.html')

@csrf_exempt
def login_(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome { user.username}')
            
            if user.user_type == 'admin':
                return redirect('farmers:home')
            elif user.user_type == 'supervisor':
                return redirect('farmers:supervisorHome')
            else:
                return redirect('farmers:workerHome')
        else:
            print("Login fail")
    return render(request, 'login/login.html')

def logout_(request):
    logout(request) 
    return redirect('authentication:login')       
