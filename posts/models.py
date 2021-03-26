from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
        else:
            return f'{self.body}'

class Video(models.Model):

    author = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.author}: {self.body}'