import numpy
import cv2
from math import *
import sys
import os

image = cv2.imread(sys.argv[1])

x = 242
y = 450

path = ""

name_img = image[y:y+30, x:x+33*29-5].copy() # Crop from x, y, w, h -> 100, 200, 300, 400
mob_img = image[y+38:y+68, x+2*29:x+11*29-5].copy()
date_img = image[y+152:y+182, x:x+2*29-5].copy()
month_img = image[y+152:y+182, x+2*29+3:x+4*29-2].copy()
year_img = image[y+152:y+182, x+4*29+6:x+8*29+1].copy()
nid_img = image[y+191:+y+221, x:x+17*29-5].copy()
mail_img = image[y+256:y+286, x:x+33*29-5].copy()
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]


cv2.destroyAllWindows()

cv2.imshow("name", name_img)
cv2.imshow("mob", mob_img)
cv2.imshow("date", date_img)
cv2.imshow("month", month_img)
cv2.imshow("year", year_img)
cv2.imshow("nid", nid_img)
cv2.imshow("mail", mail_img)

cv2.waitKey(0)

#adding each box of a row in arrays assigned for each required row
#name has 33 boxes
#mob has 9 boxes, excluding the preceeding 2 boxes those always contain 01
#dob has 8 boxes, first 2 for date, next 2 for month & last 4 for year
#nid has 17 boxes
#mail has 33 boxes
name = []
mob = []
dob = []
nid = []
mail = []

dir_names = ['name', 'mob', 'dob', 'nid', 'mail'];

for x in dir_names:
    os.makedirs(x)

for i in range (0,33*29,29):
    name.append(name_img[0:30,i:i + 24].copy())
    mail.append(mail_img[0:30, i:i + 24].copy())
    st="0" if (i<10*29) else ""
    cv2.imwrite(path + "name/" +st+ str(i/29) + ".jpg", name_img[0:30,i:i + 24].copy())
    cv2.imwrite(path + "mail/" +st+ str(i/29) + ".jpg", mail_img[0:30,i:i + 24].copy())
    #cv2.imwrite(str(i/29),mail[i/29])
    print(st+ str(i/29))
    print(i)

for i in range (0,9*29,29):
    mob.append(mob_img[0:30,i:i + 24].copy())
    st="0" if (i<10*29) else ""
    cv2.imwrite(path + "mob/" +st+ str(i/29) + ".jpg", mob_img[0:30,i:i + 24].copy())
	#cv2.imshow(i/29,mob[i/29])
for i in range (0,17*29,29):
    nid.append(nid_img[0:30,i:i + 24].copy())
    st="0" if (i<10*29) else ""
    cv2.imwrite(path + "nid/" +st+ str(i/29) + ".jpg", nid_img[0:30,i:i + 24].copy())
	#cv2.imshow(i/29,nid[i/29])
for i in range (0,2*29,29):
    dob.append(date_img[0:30,i:i + 24].copy())
    st="0" if (i<10*29) else ""
    cv2.imwrite(path + "dob/" + st+str(i/29) + ".jpg", date_img[0:30,i:i + 24].copy())
	#cv2.imshow(i/29,dob[i/29])
for i in range (0,2*29,29):
    dob.append(month_img[0:30,i:i + 24].copy())
    st="0" if (i<10*29) else ""
    cv2.imwrite(path + "dob/" + st+str(2+i/29) + ".jpg", month_img[0:30,i:i + 24].copy())
	#cv2.imshow(2+(i/29),dob[2+(i/29)])
for i in range (0,4*29,29):
    dob.append(year_img[0:30,i:i + 24].copy())
    st="0" if (i<10*29) else ""
    cv2.imwrite(path + "dob/" + st+ str(4+i/29) + ".jpg", year_img[0:30,i:i + 24].copy())
	#cv2.imshow(4+(i/29),dob[4+(i/29)])
# cnt='0'
# for im in dob:
#     cnt=cnt+'1'
#     cv2.imshow(cnt,im)
# cv2.waitKey(0)


'''
#name row
cv2.line(image, (0, 447), (1999, 445), (0, 0, 255), 1)
cv2.line(image, (0, 477), (1999, 475), (0, 0, 255), 1)
#mobile no row
cv2.line(image, (0, 485), (1999, 483 ), (0, 0, 255), 1)
cv2.line(image, (0, 515), (1999, 513), (0, 0, 255), 1)
#dob row
cv2.line(image, (0, 599), (1999, 597 ), (0, 0, 255), 1)
cv2.line(image, (0, 629), (1999, 627), (0, 0, 255), 1)
#nid row
cv2.line(image, (0, 638), (1999, 636), (0, 0, 255), 1)
cv2.line(image, (0, 668), (1999, 666), (0, 0, 255), 1)
#email row
cv2.line(image, (0, 703), (1999, 701), (0, 0, 255), 1)
cv2.line(image, (0, 733), (1999, 731), (0, 0, 255), 1)

for i in range (240, 240+33*29, 29):
    cv2.line(image, (i, 1), (i+1, 1000), (0, 0, 255), 1)
    cv2.line(image, (i+24, 1), (i+25, 1000), (0, 0, 255), 1)

# for a in arr:
#     print (a)
#cv2.line(image, (240, 1), (240, 600), (0, 0, 255), 1)
#cv2.line(image, (265, 1), (265, 600), (0, 0, 255), 1)
#cv2.line(image, (270, 1), (270, 600), (0, 0, 255), 1)
#cv2.line(image, (295, 1), (295, 600), (0, 0, 255), 1)

cv2.imshow("showing...",image)
cv2.waitKey(0)
'''
