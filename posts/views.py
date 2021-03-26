from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Video
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts' :  posts
    }
    return render(request, 'posts/posts.html', context)

@login_required
def new(request):    
    return render(request, 'posts/new.html')

@login_required
def create(request):
    user = request.user
    body = request.POST.get('body')
    image = request.FILES.get('image')

    post = Post(user=user, body=body, image=image, created_at=timezone.now())
    post.save()
    return redirect('detail', post_id=post.id)
    

# def create(request):
#     print(request.GET) # request.GET이 서버 로그로 출력됨
#     print(request.GET.get('author'))
#     print(request.GET.get('body'))

#     context = {'author':request.GET.get('author'), 'body': request.GET.get('body')}
#     return render(request, 'posts/create.html', context)
@login_required
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' :  post
    }
    return render(request, 'posts/detail.html', context)

@login_required
def edit(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts')

    context = {'post': post}
    return render(request, 'posts/edit.html', context)

@login_required
def update(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts')
    post.body = request.POST.get('body')
    image = request.FILES.get('image')
    if image:
        post.image = image
    post.save()
    
    return redirect('detail', post_id=post.id)

@login_required
def delete(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts')
   
    post.delete()
    
    return redirect('posts')

@login_required
def like(request, post_id):
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)

            if request.user in post.liked_users.all():
                post.liked_users.remove(request.user)
            else:
                post.liked_users.add(request.user)
            
            return redirect('detail', post_id=post.id)
        except Post.DoesNotExist:
            pass
    return redirect('posts')

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


def mypage(request):
    return render(request, 'posts/mypage.html')