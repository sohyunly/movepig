from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Video


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts' :  posts
    }
    return render(request, 'posts/posts.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    print(request.GET) # request.GET이 서버 로그로 출력됨
    print(request.GET.get('author'))
    print(request.GET.get('body'))

    context = {'author':request.GET.get('author'), 'body': request.GET.get('body')}
    return render(request, 'posts/create.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' :  post
    }
    return render(request, 'posts/detail.html', context)

def video(request):
    videos = Video.objects.all()
    context = {
        'videos' :  videos
    }
    return render(request, 'posts/video.html', context)

def videodetail(request, video_id):
    video = Video.objects.get(id=video_id)
    context = {
        'video' :  video
    }
    return render(request, 'posts/video_detail.html', context)

def signin(request):
    return render(request, 'posts/signin.html')

def signup(request):
    return render(request, 'posts/signup.html')

def mypage(request):
    return render(request, 'posts/mypage.html')