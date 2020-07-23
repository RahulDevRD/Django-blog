import datetime
from django.db import models
from django.utils import timezone

class Material(models.Model):
    material_type=models.CharField(max_length=200)
    dress_image=models.ImageField(default='default.jpg',upload_to='DressImage')


    def __str__(self):
        return self.material_type
