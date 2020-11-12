import cv2,sys,os
#1,2,3,4


def cropIMG(path):
    try:
        os.mkdir("Solution")
    except:
        pass

    dirName = path
    dirName = dirName.replace("\\","").replace("/","").strip(".png").strip(".jpeg").strip(".jpg")
    
    dirName = os.path.join("Solution",dirName)
    os.mkdir(dirName)
    #fotoyu okudum

    img = cv2.imread(path)

    #griye dönüştürdüm
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #blurladım(köşeler belli olsun diye)
    img_gray_blur = cv2.GaussianBlur(img_gray,(1,1),cv2.BORDER_DEFAULT)

    ##THRESH BINARY ya beyaz ya da siyah yapıyo)
    _ , thresh = cv2.threshold(img_gray_blur,150,230,cv2.THRESH_BINARY)

    # Köşeleri alıyorsun
    contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

    counter = 0
    # tespit edilen köşeleri geziyoruz
    for cnt in reversed(contours): 
        
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

                path = f"{dirName}/{counter}.jpeg"
                cv2.imwrite(path,rect)
                counter+=1


cropIMG("trainingData/3.png")