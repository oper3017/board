from django.db import models
from django.forms import ModelForm
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    


    def publish(self):
        self.published_date = timezone.now()
        self.save() 

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Upload(models.Model):
    post = models.ForeignKey(Post)
    pic = models.FileField(upload_to="images/")    
    upload_date=models.DateTimeField(auto_now_add =True)

class Shoplist(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.TextField()
