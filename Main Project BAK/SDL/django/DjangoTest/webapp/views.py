#coding: utf8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from Tkinter import *
import tkFileDialog

import cv2

from .forms import ImageForm
from .models import Image

def index(request):
    #root = Tk()

    #root.withdraw() # close the gui window
    #in_path = tkFileDialog.askopenfilename()

    return render(request, 'webapp/home.html')

# -*- coding: utf-8 -*-


def SaveFile(request):
    saved = False

    if request.method == "POST":
        # Get the posted form
        myImageForm = ImageForm(request.POST, request.FILES)

        if myImageForm.is_valid():
            img = Image()
            img.name = myImageForm.cleaned_data["name"]
            img.image = myImageForm.cleaned_data["picture"]
            img.save()
            saved = True
    else:
        myImageForm = ImageForm()

    return render(request, 'webapp/home.html')
