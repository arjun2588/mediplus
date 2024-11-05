from django.db import models
from django import forms
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=320)
    phone = models.CharField(max_length=15)
    subject = models.TextField()
    message = models.TextField()
    is_notify= models.BooleanField(default=False)
    
    def __str__(self):
        return self.name