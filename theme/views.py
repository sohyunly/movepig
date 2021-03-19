from django.shortcuts import render
from django.views.generic .base import TemplateView

class MainpageView(TemplateView):
    template_name = 'theme/main.html'

class Map(TemplateView):
    template_name = 'theme/map.html'

class Video(TemplateView):
    template_name = 'theme/video.html'

class VideoDetail(TemplateView):
    template_name = 'theme/video_detail.html'