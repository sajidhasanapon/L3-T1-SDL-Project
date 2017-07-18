#coding: utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Opencv(models.Model):
    imagem = models.ImageField(upload_to="opencv/media")


class Image(models.Model):
   name = models.CharField(max_length = 50)
   image = models.ImageField(upload_to = 'images')

   class Meta:
      db_table = "image"
