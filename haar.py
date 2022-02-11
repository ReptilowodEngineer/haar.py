from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
n = str(1)
p = '/home/pi/Desktop/10Jan/'  # адрес пустой папки
# p = 'C:/Users/messi/Desktop/OpenCV_automobile/'
y = 0
import cv2
import time
import os

l1 = {0: 0}
l2 = {0: 0}
l3 = {0: 0}
l4 = []
x1 = {0: 0}
y1 = {0: 0}
h1 = {0: 0}
w1 = {0: 0}
tim = 0
q = 1

bag_cascade = cv2.CascadeClassifier('/home/pi/Desktop/10Jan/cascade_bag.xml')
cr_cascade = cv2.CascadeClassifier('/home/pi/Desktop/10Jan/cascade_cr.xml')
qr_cascade = cv2.CascadeClassifier('C:/Users/messi/Desktop/OpenCV_automobile/qr/data/cascade.xml')
# img camera name n=0 n=n+1 list +n if list(c)==key delete if p=0 & list not empty print list


"""
bag_cascade = cv2.CascadeClassifier('C:/Users/messi/Desktop/OpenCV_automobile/Bags/ha/cascade_bag.xml')
cr_cascade = cv2.CascadeClassifier('C:/Users/messi/Desktop/OpenCV_automobile/Bagscrashed/ha/cascade_cr.xml')
imgg = 'C:/Users/messi/Desktop/OpenCV_automobile/Bagscrashed/Good/9.jpg'
# imgg='C:/Users/messi/Desktop/OpenCV_automobile/Bags/Good/1.jpg'
qr_cascade=cv2.CascadeClassifier('C:/Users/messi/Desktop/OpenCV_automobile/qr/data/cascade.xml')
"""

nam = ''
z = 1.5
u = 1
while True:
    camera.capture(p + str(n) + '.jpg')
    img = cv2.imread(p + str(n) + '.jpg')
    # img=cv2.imread(p+n+'.jpg')

    # camera.capture(p+str(n)+'.jpg')
    # img=cv2.imread(p+str(n)+'.jpg')
    h8, w8 = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bag = bag_cascade.detectMultiScale(gray, z, 5)
    qrCodeDetector = cv2.QRCodeDetector()
    qr = qr_cascade.detectMultiScale(gray, z, 5)
    for (xq, yq, wq, hq) in qr:
        decodedText, points, _ = qrCodeDetector.detectAndDecode(img)

        if points is not None:

            nrOfPoints = len(points)

            for i in range(nrOfPoints):
                nextPointIndex = (i + 1) % nrOfPoints
                cv2.line(img, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255, 0, 0), 5)

        print(decodedText)
    for (x, y, w2, h2) in bag:
        s2 = (w2 + h2)
        s1 = (w8 + h8) / 2
        if s2 > s1:
            k = int(n)
            for u in range(k + 1):
                u = int(u)
                print(u)
                xx1 = x1.get(u)
                yy1 = y1.get(u)
                hh1 = h1.get(u)
                ww1 = w1.get(u)
                if xx1 != x:
                    if yy1 != y:
                        if hh1 != h2:
                            if ww1 != w2:
                                k = int(n)
                                org = (x, y + 20)
                                cv2.putText(img, 'Bag', org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)
                                cv2.rectangle(img, (x, y), (x + w2, y + h2), (255, 255, 0), 2)
                                roi_gray = gray[y:y + h2, x:x + w2]
                                roi_color = img[y:y + h2, x:x + w2]
                                x1[k] = x
                                y1[k] = y
                                w1[k] = w2
                                h1[k] = h2
                                # cv2.imwrite(p + str(n) + '.jpg', cv2.imread(imgg))
                                cr = cr_cascade.detectMultiScale(gray, 1.004, 1)

                                for (x3, y3, w3, h3) in cr:
                                    s3 = (w3 + h3)
                                    s4 = (w8 + h8) / 3
                                    if s3 > s4:
                                        org = (x3, y3 + 20)
                                        cv2.putText(img, 'Damage', org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)
                                        cv2.rectangle(img, (x3, y3), (x3 + w3, y3 + h3), (255, 255, 0), 2)
                                        roi_gray = gray[y3:y3 + h3, x3:x3 + w3]
                                        roi_color = img[y3:y3 + h3, x3:x3 + w3]
                                        k = int(n)
                                        x = 0
                                        if x >= 1:
                                            x = l1.get(k)
                                        else:
                                            x = 0
                                        c = x + 1
                                        l1[k] = c
                                q = 1

                                # When everything is done, release the capture
                                n = int(int(n) + 1)

    cv2.startWindowThread()
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    time.sleep(5)
    cv2.destroyAllWindows()
    os.remove(str(n) + '.jpg')
    print(l3)
    print(l4)
    g = 2


