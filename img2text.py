import pytesseract,cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = '/usr/share/tesseract-ocr/4.00/tessdata'



def textTransform(path):
    img = cv2.imread(path)
    txt = pytesseract.image_to_string(img)
    return txt

im1 = cv2.imread('cikti/0.jpeg')
im2 = cv2.imread('cikti/1.jpeg')
im3 = cv2.imread('cikti/2.jpeg')
im4 = cv2.imread('cikti/3.jpeg')
im5 = cv2.imread('cikti/4.jpeg')
im6 = cv2.imread('cikti/5.jpeg')
im7 = cv2.imread('cikti/6.jpeg')
im8 = cv2.imread('cikti/7.jpeg')
im9 =  cv2.imread('cikti/8.jpeg')
im10 = cv2.imread('cikti/44.jpeg')
im11 = cv2.imread('cikti/47.jpeg')
im12 = cv2.imread('cikti/46.jpeg')
im13 = cv2.imread('cikti/48.jpeg')


im_v = cv2.resize(im1,(100,100))
im_v = cv2.GaussianBlur(im_v,(5,5),cv2.BORDER_DEFAULT)
_, im_v = cv2.threshold(im_v,150,230,cv2.THRESH_BINARY)
for i in [im2,im3,im4,im5,im6,im7,im8]:
    i = cv2.resize(i,(100,100))
    i = cv2.GaussianBlur(i,(5,5),cv2.BORDER_DEFAULT)
    _, i = cv2.threshold(i,150,230,cv2.THRESH_BINARY)
    im_v=np.concatenate([im_v,i],axis=1)
cv2.imwrite('vconcat.jpg', im_v)
