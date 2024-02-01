

import cv2
face_cascade = cv2.CascadeClassifier('haar.xml')   #pretrained haar cascade classfier mainly used in object detection

img = cv2.imread('test1.jpg')
faces = face_cascade.detectMultiScale(img, 1.1, 4)
#incase if the face is smalled due ti distance then scale factor...resizes image 1.1 times to its original size
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (200,100,50), 4)

cv2.imwrite("output.jpg", img)
print("face Dectection successfull")