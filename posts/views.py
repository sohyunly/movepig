from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts' :  posts
    }
    return render(request, 'posts/posts.html', context=context)

def create(request):
    return render(request, 'posts/create.html')

def detail(request):
    return render(request, 'posts/detail.html')

def video(request):
    return render(request, 'posts/video.html')

def videodetail(request):
    return render(request, 'posts/video_detail.html')

def signin(request):
    return render(request, 'posts/signin.html')

def signup(request):
    return render(request, 'posts/signup.html')

def mypage(request):
    return render(request, 'posts/mypage.html')