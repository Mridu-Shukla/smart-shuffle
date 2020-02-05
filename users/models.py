from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Songs(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=200)
    duration = models.IntegerField(editable=False)

    def __str__(self):
        return self.title
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    fav_song = models.CharField(null=True, max_length=100)
    fav_artist = models.CharField(null=True, max_length=100)
    contact = models.IntegerField(null=True,blank=True)
    fav_songs = models.ManyToManyField(Songs)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username
     
