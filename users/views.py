from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from subjects.models import Subject
from django.contrib import messages

# Create your views here.


def register_user(request):
    if request.method == 'GET':
        user_type = request.GET.get('type')
        if user_type:
            user_type = user_type.split('/')[0]
        print("user_type: ", user_type)

        classes = dict(Subject.CLASSTYPE)

        context = {
            "classes": classes,
            "user_type": user_type,
        }
        return render(request, 'users/register.html', context)


def adminLogin(request):
    if request.method == "GET":
        return render(request, 'users/login.html')

    if request.method == "POST":
        context = {
            'data': request.POST,
        }

        username = request.POST.get('username')
        # email = request.POST.get('email')
        password = request.POST.get('password')

        if username == '' or password == '':
            messages.add_message(request, messages.ERROR,
                                 'Please fill all the fields')
            return render(request, 'users/login.html', status=401,
                          context=context)

        # user = authenticate(request, username=username, password=password)
        user = authenticate(request, username=username, password=password)
        print("user: ", user)

        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Username or Password is Wrong')
            return render(request, 'users/login.html', status=401,
                          context=context)

        login(request, user)
        return redirect('home')


def logoutUser(request):
    logout(request)
    return redirect('home')
