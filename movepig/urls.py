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
    path('create/', views.create, name='create'),
    path('detail/', views.detail, name='detail'),
    path('video/', views.video, name='video'),
    path('videodetail/', views.videodetail, name='videodetail'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='signup'),
    # views 모듈 안에 있는 index라는 것을 사용하겠다!
]
