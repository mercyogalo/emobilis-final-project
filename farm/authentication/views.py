from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm
# Create your views here.

def register(request):
    
    if request.method == 'POST' :
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)  
                user.set_password(form.cleaned_data['password']) 
                user.save()
                return redirect('authentication:login') 
            except:
                print(form.cleaned_data)
    else:
        form = UserForm()
    return render(request, 'login/register.html', {'form': form})

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
