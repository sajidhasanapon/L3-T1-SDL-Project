from random import randint

import os
from PIL import Image

all_dirs = ['name', 'mob', 'dob', 'nid', 'mail']

for path in all_dirs:
	classnames=os.listdir(path)
	classnames.sort()
	images=[]

	for img_name in classnames:
		images.append(Image.open(path + '/' + img_name))

	k=len(images)
	im2=[]

	for i in range(k):	
		img=images[i]
		im2.append(img)

	h=0
	for i in range(k):
		h=h+40*im2[i].size[1]/im2[i].size[0]+5

	result = Image.new('L', (40,h),'white')
	lp=0

	for i in range(k):	
		img=im2[i]
		img=img.convert('L')
		print 'before ',
		print img.size
		h=40*img.size[1]/img.size[0]
		if h<1:
			h=1
		img=img.resize((40,h),Image.ANTIALIAS)
		print 'after ',
		print img.size
		result.paste(img, box=(0, lp))
		lp=lp+5+img.size[1]
		
	
	result.save(path + '.png')	
