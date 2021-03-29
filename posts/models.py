from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.TextField(null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField()
    n_hit = models.PositiveIntegerField(default=0, null=True)
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
        else:
            return f'{self.body}'

    @property
    def update_counter(self):
        self.n_hit = self.n_hit + 1
        self.save()

class Video(models.Model):

    author = models.CharField(max_length=100)
    title = models.TextField()
    video_image = models.ImageField(upload_to='videos', null=True)
    video_key = models.CharField(max_length=12, null=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.author}: {self.title}'