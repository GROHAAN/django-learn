from django.db import models


# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    qualification=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    audio=models.ImageField(upload_to='audio/')
    video=models.ImageField(upload_to='video/')
    document=models.ImageField(upload_to='document/')

