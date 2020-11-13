import cv2,pytesseract,os


for i in sorted(os.listdir("temp/18")):
    print(i)
    img = cv2.imread(f"temp/18/{i}")
    print(pytesseract.image_to_string(img,config='--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789').strip(" "))