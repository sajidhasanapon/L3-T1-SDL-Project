import numpy
import cv2
from math import *
import os




threshold = 230


def ProcessImage(image):
    print (image)
    src_image = cv2.imread(image)
    print(src_image.shape)

    row = src_image.shape[0]
    col = src_image.shape[1]

    rot_mat = cv2.getRotationMatrix2D((col / 2, row / 2), 0, 1)
    image = cv2.warpAffine(src_image, rot_mat, (col, row))

    for i in range(0, row):
        for j in range(0, col):
            baal = image.item(i, j, 0)
            gaal = image.item(i, j, 1)
            laal = image.item(i, j, 2)

            image.itemset(i, j, 0, laal)
            image.itemset(i, j, 2, baal)

            if (baal > threshold or laal > threshold or gaal > threshold):
                image.itemset(i, j, 0, 0)
                image.itemset(i, j, 2, 0)
                image.itemset(i, j, 1, 0)
            else:
                image.itemset(i, j, 0, 255)
                image.itemset(i, j, 2, 255)
                image.itemset(i, j, 1, 255)


    edges = cv2.Canny(image, 0, 500, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, numpy.pi / 180, 150)

    for rho, theta in lines[0]:
        # rot_mat = cv2.getRotationMatrix2D((col / 2, row / 2), degrees(theta) + 270, 1)
        print(degrees(theta))


        # The following block works, but I have no fucking idea why.

        if degrees(theta) <= 5:  # actually, works like theta < 0
            print("in theta less than 90")
            rot_mat = cv2.getRotationMatrix2D((col / 2, row / 2), degrees(theta), 1)

        else:  # actually, works like theta > 0
            print("in else")
            # theta = theta - pi / 2
            rot_mat = cv2.getRotationMatrix2D((col / 2, row / 2), degrees(theta) - 90, 1)

        image = cv2.warpAffine(image, rot_mat, (col, row))


        '''
        cv2.imshow('Rotate', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''

        break

    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, numpy.pi / 180, 200)

    arr = []
    cnt = 0
    y = 445
    for rho, theta in lines[0]:
        a = numpy.cos(theta)
        b = numpy.sin(theta)
        x0 = a * rho
        y0 = b * rho

        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000 * a)
        if y1 > 442 and y1 < 447:
            y = y1 + 5
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000 * a)

        if fabs(theta - pi / 2) < 0.0001:
            cnt = cnt + 1
            arr.append(y1)
            # cv2.line(image, (x1, y1+2), (x2, y2), (0, 0, 255), 1)
    print ("SORTED ARRAY")
    arr.sort()
    # kernel=numpy.ones((3,3),numpy.uint8)
    # image=cv2.erode(image,kernel=kernel,iterations=1)


    # cropping different rows from the given image
    print ('starting height : ', y)
    # y=arr[4]
    x = 240
    name_img = image[y:y + 30, x:x + 33 * 29 - 5].copy()  # Crop from x, y, w, h -> 100, 200, 300, 400
    mob_img = image[y + 38:y + 68, x + 2 * 29:x + 11 * 29 - 5].copy()
    date_img = image[y + 152:y + 182, x:x + 2 * 29 - 5].copy()
    month_img = image[y + 152:y + 182, x + 2 * 29 + 3:x + 4 * 29 - 2].copy()
    year_img = image[y + 152:y + 182, x + 4 * 29 + 6:x + 8 * 29 + 1].copy()
    nid_img = image[y + 191:+y + 221, x:x + 17 * 29 - 5].copy()
    mail_img = image[y + 256:y + 286, x:x + 33 * 29 - 5].copy()

    # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]


    #cv2.destroyAllWindows()
    '''
    cv2.imshow("name", name_img)
    cv2.imshow("mob", mob_img)
    cv2.imshow("date", date_img)
    cv2.imshow("month", month_img)
    cv2.imshow("year", year_img)
    cv2.imshow("nid", nid_img)
    cv2.imshow("mail", mail_img)
    cv2.waitKey(0)
    '''

    # adding each box of a row in arrays assigned for each required row
    # name has 33 boxes
    # mob has 9 boxes, excluding the preceeding 2 boxes those always contain 01
    # dob has 8 boxes, first 2 for date, next 2 for month & last 4 for year
    # nid has 17 boxes
    # mail has 33 boxes
    name = []
    mob = []
    dob = []
    nid = []
    mail = []

    all=[]
    cnt = 0
    for i in range(0, 33 * 29, 29):

        crp = name_img[0:30, i:i + 24].copy()
        arrName=[]
        cv2.imwrite('/home/apon/Ongoing/SDL/myproject/media/output/name/'+str(cnt)+'.jpg', crp)
        print (str(cnt)+'.jpg')

        crp = mail_img[0:30, i:i + 24].copy()
        cv2.imwrite('/home/apon/Ongoing/SDL/myproject/media/output/mail/' + str(cnt) + '.jpg', crp)
        print (str(cnt) + '.jpg')

        name.append(name_img[0:30, i:i + 24].copy())
        mail.append(mail_img[0:30, i:i + 24].copy())

        cnt = cnt + 1

    cnt = 0
    for i in range(0, 9 * 29, 29):
        crp = mob_img[0:30, i:i + 24].copy()
        cv2.imwrite('/home/apon/Ongoing/SDL/myproject/media/output/mob/' + str(cnt) + '.jpg', crp)
        print (str(cnt) + '.jpg')

        cnt +=1

        mob.append(mob_img[0:30, i:i + 24].copy())

    cnt = 0
    for i in range(0, 17 * 29, 29):
        crp = nid_img[0:30, i:i + 24].copy()
        cv2.imwrite('/home/apon/Ongoing/SDL/myproject/media/output/nid/' + str(cnt) + '.jpg', crp)
        print (str(cnt) + '.jpg')

        cnt += 1
        nid.append(nid_img[0:30, i:i + 24].copy())

    cnt = 0
    for i in range(0, 2 * 29, 29):
        crp = date_img[0:30, i:i + 24].copy()
        cv2.imwrite('/home/apon/Ongoing/SDL/myproject/media/output/dob/' + str(cnt) + '.jpg', crp)
        print (str(cnt) + '.jpg')

        cnt += 1
        dob.append(date_img[0:30, i:i + 24].copy())

    for i in range(0, 2 * 29, 29):
        crp = month_img[0:30, i:i + 24].copy()
        cv2.imwrite('/home/apon/Ongoing/SDL/myproject/media/output/dob/' + str(cnt) + '.jpg', crp)
        print (str(cnt) + '.jpg')

        cnt += 1
        dob.append(month_img[0:30, i:i + 24].copy())
    for i in range(0, 4 * 29, 29):
        crp = year_img[0:30, i:i + 24].copy()
        cv2.imwrite('/home/apon/Ongoing/SDL/myproject/media/output/dob/' + str(cnt) + '.jpg', crp)
        print (str(cnt) + '.jpg')

        cnt += 1
        dob.append(year_img[0:30, i:i + 24].copy())
    # cnt='0'
    # for im in dob:
    #     cnt=cnt+'1'
    #     cv2.imshow(cnt,im)
    # cv2.waitKey(0)

    # name row
    cv2.line(image, (0, 447), (1999, 445), (0, 0, 255), 1)
    cv2.line(image, (0, 477), (1999, 475), (0, 0, 255), 1)
    # mobile no row
    cv2.line(image, (0, 485), (1999, 483), (0, 0, 255), 1)
    cv2.line(image, (0, 515), (1999, 513), (0, 0, 255), 1)
    # dob row
    cv2.line(image, (0, 599), (1999, 597), (0, 0, 255), 1)
    cv2.line(image, (0, 629), (1999, 627), (0, 0, 255), 1)
    # nid row
    cv2.line(image, (0, 638), (1999, 636), (0, 0, 255), 1)
    cv2.line(image, (0, 668), (1999, 666), (0, 0, 255), 1)
    # email row
    cv2.line(image, (0, 703), (1999, 701), (0, 0, 255), 1)
    cv2.line(image, (0, 733), (1999, 731), (0, 0, 255), 1)

    for i in range(240, 240 + 33 * 29, 29):
        cv2.line(image, (i, 1), (i + 1, 1000), (0, 0, 255), 1)
        cv2.line(image, (i + 24, 1), (i + 25, 1000), (0, 0, 255), 1)

    # for a in arr:
    #     print (a)
    # cv2.line(image, (240, 1), (240, 600), (0, 0, 255), 1)
    # cv2.line(image, (265, 1), (265, 600), (0, 0, 255), 1)
    # cv2.line(image, (270, 1), (270, 600), (0, 0, 255), 1)
    # cv2.line(image, (295, 1), (295, 600), (0, 0, 255), 1)

    screen_res = 1366, 768

    #cv2.imshow("showing...", image)
    #cv2.waitKey(0)
