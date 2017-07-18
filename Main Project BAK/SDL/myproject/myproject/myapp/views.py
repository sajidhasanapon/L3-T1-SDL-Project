# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

from myproject.opencv import opencv
import os
from PIL import Image

images=[]

def login(request):
    return render(request, 'login.html')


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()


            #pass to opencv
            BASE_PATH = '/home/apon/Ongoing/SDL/myproject/media/'
            folder = 'documents/'
            uploaded_filename = request.FILES['docfile'].name
            full_filename = BASE_PATH + folder + uploaded_filename
            print (full_filename)
            #global images = opencv.ProcessImage(full_filename)

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
            return HttpResponseRedirect(reverse('myproject.myapp.views.show'))
            #return render(request, 'show.html')
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def show(request):

    path = '/home/apon/Ongoing/SDL/myproject/media/output/name/'
    classnames = os.listdir(path)
    images = []
    for i in range (len(classnames) - 1):
        images.append(Image.open(path + str(i) + '.jpg'))

    k = len(images) - 1
    im2 = []
    for i in range(k):
        im2.append(images[i])
    h = 0
    for i in range(k):
        h = h + 40 * im2[i].size[1] / im2[i].size[0] + 5

    result = Image.new('L', (40, h), 'white')
    lp = 0
    for i in range(k):
        img = im2[i]
        img = img.convert('L')
        print 'before ',
        print img.size
        img = img.resize((40, 40 * img.size[1] / img.size[0]), Image.ANTIALIAS)
        print 'after ',
        print img.size
        result.paste(img, box=(0, lp))
        lp = lp + 5 + img.size[1]

    result.save('/home/apon/Ongoing/SDL/myproject/media/output/name/res.png')

    path = '/home/apon/Ongoing/SDL/myproject/media/output/mob/'
    classnames = os.listdir(path)
    images = []
    for i in range(len(classnames) - 1):
        images.append(Image.open(path + str(i) + '.jpg'))

    k = len(images) - 1
    im2 = []
    for i in range(k):
        im2.append(images[i])
    h = 0
    for i in range(k):
        h = h + 40 * im2[i].size[1] / im2[i].size[0] + 5

    result = Image.new('L', (40, h), 'white')
    lp = 0
    for i in range(k):
        img = im2[i]
        img = img.convert('L')
        print 'before ',
        print img.size
        img = img.resize((40, 40 * img.size[1] / img.size[0]), Image.ANTIALIAS)
        print 'after ',
        print img.size
        result.paste(img, box=(0, lp))
        lp = lp + 5 + img.size[1]

    result.save('/home/apon/Ongoing/SDL/myproject/media/output/mob/res.png')

    path = '/home/apon/Ongoing/SDL/myproject/media/output/nid/'
    classnames = os.listdir(path)
    images = []
    for i in range(len(classnames) - 1):
        images.append(Image.open(path + str(i) + '.jpg'))

    k = len(images) - 1
    im2 = []
    for i in range(k):
        im2.append(images[i])
    h = 0
    for i in range(k):
        h = h + 40 * im2[i].size[1] / im2[i].size[0] + 5

    result = Image.new('L', (40, h), 'white')
    lp = 0
    for i in range(k):
        img = im2[i]
        img = img.convert('L')
        print 'before ',
        print img.size
        img = img.resize((40, 40 * img.size[1] / img.size[0]), Image.ANTIALIAS)
        print 'after ',
        print img.size
        result.paste(img, box=(0, lp))
        lp = lp + 5 + img.size[1]

    result.save('/home/apon/Ongoing/SDL/myproject/media/output/nid/res.png')

    path = '/home/apon/Ongoing/SDL/myproject/media/output/dob/'
    classnames = os.listdir(path)
    images = []
    for i in range(len(classnames) - 1):
        images.append(Image.open(path + str(i) + '.jpg'))

    k = len(images) - 1
    im2 = []
    for i in range(k):
        im2.append(images[i])
    h = 0
    for i in range(k):
        h = h + 40 * im2[i].size[1] / im2[i].size[0] + 5

    result = Image.new('L', (40, h), 'white')
    lp = 0
    for i in range(k):
        img = im2[i]
        img = img.convert('L')
        print 'before ',
        print img.size
        img = img.resize((40, 40 * img.size[1] / img.size[0]), Image.ANTIALIAS)
        print 'after ',
        print img.size
        result.paste(img, box=(0, lp))
        lp = lp + 5 + img.size[1]

    result.save('/home/apon/Ongoing/SDL/myproject/media/output/dob/res.png')

    path = '/home/apon/Ongoing/SDL/myproject/media/output/mail/'
    classnames = os.listdir(path)
    images = []
    for i in range(len(classnames) - 1):
        images.append(Image.open(path + str(i) + '.jpg'))

    k = len(images) - 1
    im2 = []
    for i in range(k):
        im2.append(images[i])
    h = 0
    for i in range(k):
        h = h + 40 * im2[i].size[1] / im2[i].size[0] + 5

    result = Image.new('L', (40, h), 'white')
    lp = 0
    for i in range(k):
        img = im2[i]
        img = img.convert('L')
        print 'before ',
        print img.size
        img = img.resize((40, 40 * img.size[1] / img.size[0]), Image.ANTIALIAS)
        print 'after ',
        print img.size
        result.paste(img, box=(0, lp))
        lp = lp + 5 + img.size[1]

    result.save('/home/apon/Ongoing/SDL/myproject/media/output/mail/res.png')

    return render(request, 'show.html')