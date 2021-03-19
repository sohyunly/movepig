from django.shortcuts import render
from django.http import HttpResponse


def posts(request):
    return render(request, 'posts/posts.html')

def create(request):
    return render(request, 'posts/create.html')

def detail(request):
    return render(request, 'posts/detail.html')

def signin(request):
    return render(request, 'posts/signin.html')

def signup(request):
    return render(request, 'posts/signup.html')

def mypage(request):
    return render(request, 'posts/mypage.html')