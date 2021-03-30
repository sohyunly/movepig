from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Video
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import CommentForm


def posts(request):
    posts = Post.objects.all()
    # context = {
    #     'posts' :  posts,
    # }
    search_key = request.GET.get('search_key')
    if search_key :
        posts = posts.filter(title__icontains=search_key)
    return render(request, 'posts/posts.html', {'posts':posts})
    

@login_required
def new(request):    
    return render(request, 'posts/new.html')

@login_required
def create(request):
    user = request.user
    title = request.POST.get('title')
    body = request.POST.get('body')
    image = request.FILES.get('image')
    post = Post(user=user, title=title, body=body, image=image, created_at=timezone.now())
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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("detail", post_id)
    else:
        form = CommentForm()
        return render(request, 'posts/detail.html', {"post":post, "form":form})

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
    post.title = request.POST.get('title')
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

@login_required
def vlike(request, video_id):
    if request.method == 'POST':
        try:
            video = Video.objects.get(id=video_id)

            if request.user in video.vliked_users.all():
                video.vliked_users.remove(request.user)
            else:
                video.vliked_users.add(request.user)
            
            return redirect('videodetail', video_id=video.id)
        except Post.DoesNotExist:
            pass
    return redirect('video')

def mypage(request):
    return render(request, 'posts/mypage.html')