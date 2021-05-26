from django.shortcuts import render
from subjects.models import Subject
# from .data import data
# import json


def home(request):
    # user = request.user
    classes = dict(Subject.CLASSTYPE)
    # classObj =
    # print("classes: ", classes)
    # print(data)

    user = request.user
    # print("user: ", user)
    if user == "AnonymousUser":
        user = None
    # print("user after: ", user)

    context = {
        "classes": classes,
        "user": user,
    }
    return render(request, 'home/home.html', context)

def aboutUs(request):
    classes = dict(Subject.CLASSTYPE)
    
    user = request.user
    # print("user: ", user)
    if user == "AnonymousUser":
        user = None
    # print("user after: ", user)

    context = {
        "classes": classes,
        "user": user,
    }
    return render(request, 'about.html', context)


def schoolasiumFellowship(request):
    classes = dict(Subject.CLASSTYPE)
    
    user = request.user
    # print("user: ", user)
    if user == "AnonymousUser":
        user = None
    # print("user after: ", user)

    context = {
        "classes": classes,
        "user": user,
    }
    return render(request, 'fellowship.html', context)