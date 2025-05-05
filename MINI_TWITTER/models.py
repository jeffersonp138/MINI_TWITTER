from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): 
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email' # O email é usado para fazer o login
    REQUIRED_FIELDS = []
    
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='following', blank=True
        )


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')  #Para associar o tweet ao user
    content = models.TextField(max_length=280, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #Será usado para ordenar os tweets no feed
    liked_by = models.ManyToManyField(User, related_name='liked_tweets', blank=True, default=0)
    
    @property
    def likes_count(self):
        return self.liked_by.count()

    def __str__(self):
        return self.content or "Image Tweet"
