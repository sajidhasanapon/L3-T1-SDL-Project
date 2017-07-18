#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Opencv

class ImageForm(forms.Form):
   name = forms.CharField(max_length = 100)
   image = forms.ImageField()