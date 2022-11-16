# import cv2 
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Roman\AppData\Local\Tesseract-OCR\tesseract.exe'

# placa=[]
# image=cv2.imread("imgPatentes\p\IMG8.jpg")
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# gray= cv2.blur(gray,(3,3))
# canny = cv2.Canny(gray,150,200)
# canny = cv2.dilate(canny,None,iterations=1)

# cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image,cnts,-1,(0,255,0),2)
# cv2.imshow('imagen',image)
# cv2.imshow('Canny',canny)
# cv2.moveWindow('imagen',45,10)
# cv2.waitKey(0)

print(float(2.3)/float(3.3))