import pytesseract, cv2, os, sys
import numpy as np

def cropIMG(path):
    try:
        os.mkdir("Solution")
    except:
        pass

    dirName = path
    dirName = dirName.replace("\\","_").replace("/","_").strip(".png").strip(".jpeg").strip(".jpg")
    
    dirName = os.path.join("Solution",dirName)
    try:
        os.mkdir(dirName)
    except:
        pass

    #fotoyu okudum
    img = cv2.imread(path,0)

    #griye dönüştürdüm
    # img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #blurladım(köşeler belli olsun diye)
    img_gray_blur = cv2.GaussianBlur(img,(1,1),cv2.BORDER_DEFAULT)

    ##THRESH BINARY ya beyaz ya da siyah yapıyo)
    _ , thresh = cv2.threshold(img_gray_blur,150,230,cv2.THRESH_BINARY)

    # Köşeleri alıyorsun
    contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

    counter = 10
    # tespit edilen köşeleri geziyoruz
    for cnt in reversed(contours): 

        if counter == 91:
            break
        
        # köşeler arası uzaklık
        area = cv2.contourArea(cnt) 
        
        # katsayı veriyoruz uzaklık için
        epsilon = 0.01 * cv2.arcLength(cnt, True)

        ## Her şeklin köşe adresleri
        approx = cv2.approxPolyDP(cnt,epsilon, True) 
        
        if area >400 : 

            # 4 köşegeni olanlar burda ayrılıyor
            if len(approx)==4: 

                #x1y1 x2y2 adresleri ile dörtgenleri kırpıyorum
                rect = img[approx[0][0][1]:approx[2][0][1],
                    approx[0][0][0]:approx[2][0][0]]
                rect = cv2.resize(rect,(100,100))
                rect = cv2.GaussianBlur(rect,(1,1),cv2.BORDER_DEFAULT)
                _, rect = cv2.threshold(rect,127,255,cv2.THRESH_BINARY)

                path = f"{dirName}/{counter}.jpeg"
                cv2.imwrite(path,rect)
                counter+=1
    return dirName

def zero2IMG(path):
    counter = 0
    for p in sorted(os.listdir(path)):
        if counter == 81:
            break
        counter += 1
        newPath = os.path.join(path,p)
        img = cv2.imread(newPath,0)
        _, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        if np.mean(img)>253:
            position = (30,70)
            cv2.putText(
                img, #numpy array on which text is written
                "0", #text
                position, #position at which writing has to start
                cv2.FONT_HERSHEY_SIMPLEX, #font family
                2, #font size
                (0, 0, 0, 0), #font color
                3) #font stroke
            cv2.imwrite(newPath,img)

def concatIMG(path):
    img_list = list()

    counter = 0
    for p in sorted(os.listdir(path)):
        if counter == 81:
            break
        counter += 1
        newPath = os.path.join(path,p)
        img = cv2.imread(newPath)
        img_list.append(img)
        
    img1 = img_list[0]
    for im in img_list[1:9]:
        img1 = np.concatenate((img1,im),axis=1)


    img2 = img_list[9]
    for im in img_list[10:18]:
        img2 = np.concatenate((img2,im),axis=1)

    img3 = img_list[18]
    for im in img_list[19:27]:
        img3 = np.concatenate((img3,im),axis=1)

    img4 = img_list[27]
    for im in img_list[28:36]:
        img4 = np.concatenate((img4,im),axis=1)

    img5 = img_list[36]
    for im in img_list[37:45]:
        img5 = np.concatenate((img5,im),axis=1)

    img6 = img_list[45]
    for im in img_list[46:54]:
        img6 = np.concatenate((img6,im),axis=1)

    img7 = img_list[54]
    for im in img_list[55:63]:
        img7 = np.concatenate((img7,im),axis=1)

    img8 = img_list[63]
    for im in img_list[64:72]:
        img8 = np.concatenate((img8,im),axis=1)

    img9 = img_list[72]
    for im in img_list[73:81]:
        img9 = np.concatenate((img9,im),axis=1)

    img = np.concatenate((img1,img2,img3,img4,img5,img6,img7,img8,img9))
    pathIMG = 'img.jpeg'
    cv2.imwrite(pathIMG, img)
    return pathIMG

def transformIMG(path):
    img = cv2.imread(path)
    txt = pytesseract.image_to_string(img)
    return txt

def txt2mat(temp):
    text = ""
    for i in temp:
        if i in "0123456789":
            text = text + i

    temp_list = []
    for i in range(0,73,9):
        temp_list.append(text[i:i+9])
        
    matrix = [[] for j in range(9)]

    i = 0
    while i<9:
        matrix[i][:0] = temp_list[i] 
        j=0
        while j<9:
            matrix[i][j] = int(matrix[i][j])
            j+=1
        i += 1

    return matrix

dirName = cropIMG("trainingData/1.png")
zero2IMG(dirName)
pathIMG = concatIMG(dirName)
temp = transformIMG(pathIMG)
matrix = txt2mat(temp)
print(np.matrix(matrix))

