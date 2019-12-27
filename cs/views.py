from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth

# Create your views here.
from .models import User


def index(request):
    return render(request, 'index.html')


def forgot(request):
    return render(request, 'forgot.html')


def login(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        password = request.POST.get('password')
        user = User.objects.filter(Email=Email, Password=password).exists()
        if user:
            return redirect('/')
        else:
            messages.info(request, 'invalid cerdentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


# Create your views here.
def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('First_Name')
        last_name = request.POST.get('Last_Name')
        Middle_Name = request.POST.get('Middle_Name')
        password = request.POST.get('password')
        Phone_Number = request.POST.get('Phone_Number')
        password2 = request.POST.get('re-password')
        Type = request.POST.get('Type')
        email = request.POST.get('email')

        if password == password2:
            if User.objects.filter(Email=email).exists():
                messages.info(request, 'email taken')
                return redirect('registration')
            else:
                user = User(Email=email, Middle_Name=Middle_Name, Password=password,
                            Phone_Number=Phone_Number, Type=Type, First_Name=first_name,
                            Last_Name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'password does not match')
            return redirect('registration')

    else:
        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
