from django.db import models

class Information(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    address = models.CharField(max_length=100)
    career=models.TextField(max_length=100)
    education=models.TextField(max_length=100)
    skill=models.TextField(max_length=100)
    project=models.TextField(max_length=100)





