from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.TextField()
    address = models.TextField()
    profile_pic = models.ImageField(upload_to="user_profile_pic/")

    def __str__(self):
        return self.user.username

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to="companies/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MotoCompany(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="moto_companies/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


