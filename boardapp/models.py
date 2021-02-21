from django.contrib.auth import get_permission_codename
from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    auther = models.CharField(max_length=50)
    snsimage = models.ImageField(upload_to='',null=True, blank=True, default='default2.png')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.TextField(null=True, blank=True,default='a')
    
    def __str__(self):
        return self.title