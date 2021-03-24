"""movepig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theme.urls')),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.detail, name='detail'),
    # path('posts/<int:post_id>/comments', views.comments),
    path('posts/new', views.new, name='new'),
    path('posts/create/', views.create, name='create'),
    path('posts/<int:post_id>/edit/', views.edit, name='edit'),
    path('posts/<int:post_id>/update/', views.update, name='update'),
    path('posts/<int:post_id>/delete/', views.delete, name='delete'),
    # path('detail/', views.detail, name='detail'),
    path('video/', views.video, name='video'),
    path('video/<int:video_id>/', views.videodetail, name='videodetail'),
    # path('videodetail/', views.videodetail, name='videodetail'),
    path('accounts/', include('accounts.urls')),
    # path('signin/', include('accounts.urls')),
    path('mypage/', views.mypage, name='mypage'),
    # views 모듈 안에 있는 index라는 것을 사용하겠다!
]
