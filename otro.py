import cv2
import matplotlib.pyplot as plt
import numpy as np 
import time
import pytesseract 
from PIL import Image


pantentClassifier = cv2.CascadeClassifier('imgPatentes\classifier\cascade.xml')
# cap = cv2.VideoCapture(2,cv2.CAP_DSHOW)
cap = cv2.VideoCapture("Fotos sacadas por mi\patentes2.mkv")
# image = cv2.imread('imgPatentes\p\carro.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# patentes = pantentClassifier.detectMultiScale(gray,
#   scaleFactor=1.3,
#   minNeighbors=5,
#   minSize=(20,6),
#   maxSize=(800,260))

# for (x,y,w,h) in patentes:
#   cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




while True:
    
    ret,frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = pantentClassifier.detectMultiScale(frame,
   scaleFactor=1.2,
   minNeighbors=30,
   minSize=(40,13),
   maxSize=(300,100)
  )

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Roman\AppData\Local\Tesseract-OCR\tesseract.exe'
    for (x,y,w,h) in toy:
        rectangulo = cv2.rectangle(frame, (x-10,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Patente',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
        # print("x=",x,"y=",y,"w=",w,"x+w=",x+w,"h+y=",h+y)
        objeto = frame[y:y+h,x:x+w]
        cv2.imshow('rect',objeto)
        texto = pytesseract.pytesseract.image_to_string(objeto, config="--psm 1")
        print(texto)
        # print(pytesseract.get_languages(config=''))
        time.sleep(0.01)

        
    time.sleep(0.01)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


# import cv2
# import os 
# import glob
# import imutils

# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# majinBooClassif = cv2.CascadeClassifier('cascade.xml')
# while True:
    
#     ret,frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     toy = majinBooClassif.detectMultiScale(gray,
#     scaleFactor = 5,
#     minNeighbors = 91,
#     minSize=(70,78))
#     for (x,y,w,h) in toy:
#         cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
#         cv2.putText(frame,'Majin Boo',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
#     cv2.imshow('frame',frame)
    
#     if cv2.waitKey(1) == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()



# Datos = 'p'
# if not os.path.exists(Datos):
#     print('Carpeta creada: ',Datos)
#     os.makedirs(Datos)
# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# x1, y1 = 190, 80
# x2, y2 = 450, 398
# count = 0
# while True:
#     ret, frame = cap.read()
#     if ret == False: break
#     imAux = frame.copy()
#     cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
#     objeto = imAux[y1:y2,x1:x2]
#     objeto = imutils.resize(objeto,width=38)
#     #print(objeto.shape)
#     k = cv2.waitKey(1)
#     if k == ord('s'):
#         cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
#         print('Imagen guardada:'+'/objeto_{}.jpg'.format(count))
#         count = count +1
#     if k == 27:
#         break
#     cv2.imshow('frame',frame)
#     cv2.imshow('objeto',objeto)
# cap.release()
# cv2.destroyAllWindows()



# img = imread('imgPatentes')
# cv2.imshow('image',img)
# Datos= 'P'

# inputFolder = '\imgPatentes\p'
# if not os.path.exists(Datos):
#     print("Carpeta creada: ", Datos)
# i=0
# for img in glob.glob(inputFolder + "/*.jpg"):
#     image=imread(img)
#     cv2.imshow('image',image)
#     cv2.waitKey(1000)
# cv2.destroyAllWindows()
