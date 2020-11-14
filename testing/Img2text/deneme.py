import cv2,pytesseract,os


for i in sorted(os.listdir("temp/20")):
    print(i)
    img = cv2.imread(f"temp/20/{i}")
    print(pytesseract.image_to_string(img,
    config='--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789').strip(" "))

    # 6  err 7
    # 8  err 4
    # 13 err 4