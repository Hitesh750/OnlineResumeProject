from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Information

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user!=None:
            return redirect('index')

        else:
            messages.add_message(request, messages.INFO,"You have supplied invalid login credentials, please try again!", "danger")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if password == password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
            else:
                user = User.objects.create_user(username=username, password=password)

                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')  # Replace 'login' with your desired URL for the login page
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'register.html')

def index(request):
    return render(request,"index.html")

def create_resume(request):
    if request.method == "POST":
        name = request.POST.get("name")

        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        career = request.POST.get("career")
        education = request.POST.get("education")
        skill=request.POST.get("skill")
        project=request.POST.get("project")


        profile=Information(name=name,phone=phone,email=email,address=address,career=career,education=education,skill=skill,project=project)
        profile.save()
    return render(request,'create_resume.html')

def resume(request,id):
    user_profile=Information.objects.get(pk=id)
    return render(request,'resume.html',{'user_profile':user_profile})


