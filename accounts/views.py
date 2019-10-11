from django.shortcuts import render,redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # Regsister user
        messages.error(request, 'Testing the error')
        return redirect('register')
    
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login  user
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect(request, 'index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')