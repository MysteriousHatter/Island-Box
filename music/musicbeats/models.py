from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
# Create your models here.




class Albums(models.Model):
    albums_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=10000)
    title = models.CharField(max_length=1000)
    artist_pic = models.ImageField(upload_to='images')
    art_name = models.CharField(max_length=2000)


    def __str__(self):
        return self.title + ' - ' + self.art_name


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    song = models.FileField(upload_to='images')
    credit = models.CharField(max_length=1000, default="")
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

class Watchlater(models.Model):
     watch_id = models.AutoField(primary_key=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     video_id = models.FileField(max_length=1000, default="")

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=100, default="")

class Channel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    bio = models.TextField(default='no bio')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10000)
    song = models.FileField(upload_to='images',default='music\media\images\European-village-birds-sounds.mp3')
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return  str(self.user.username)

    class Meta:
        ordering = ('-created',)





