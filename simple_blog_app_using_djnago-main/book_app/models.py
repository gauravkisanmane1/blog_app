from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class post(models.Model):
    
    author = models.ForeignKey(User, null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    body = tinymce_models.HTMLField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField(null=False)
  
    def __str__(self):
        return self.body

