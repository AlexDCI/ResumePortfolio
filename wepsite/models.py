from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=250)
    owner = models.CharField(max_length=100)
    rating = models.FloatField(default=5.0)
    validated = models.BooleanField(default=False)
    short_description = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(null=True,blank=True)





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=200, blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.user.username
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=300)
    message = models.TextField()