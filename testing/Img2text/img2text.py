import pytesseract, cv2, os, copy, shutil, sys
import numpy as np
from decoderClass import Sudoku

def cropIMG(path):
    try:
        os.mkdir("temp")
    except:
        pass

    dirName = path
    _,dirName = os.path.split(dirName)
    dirName = dirName.replace("\\","_"
    ).replace("/","_"
    ).strip(".png"
    ).strip(".jpeg"
    ).strip(".jpg")

    img_name = dirName
    
    dirName = os.path.join("temp",dirName)
    try:
        os.mkdir(dirName)
    except:
        pass

    #fotoyu okudum
    img = cv2.imread(path,0)

    #blurladım(köşeler belli olsun diye)
    img_gray_blur = cv2.GaussianBlur(img,(1,1),cv2.BORDER_DEFAULT)

    ##THRESH BINARY ya beyaz ya da siyah yapıyo)
    _ , thresh = cv2.threshold(img_gray_blur,150,230,cv2.THRESH_BINARY)

    # Köşeleri alıyorsun
    contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

    # 81 tane fotoğfar kırpılmasını kontrol ediyorum
    counter = 10

    # kesilen karelerin koordinatları
    xy = list()

    # tespit edilen köşeleri geziyoruz
    for cnt in reversed(contours): 

        # bazen büyük kareleri de dörtgen olarak alıyor
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
                x1 = approx[0][0][1]
                y1 = approx[2][0][1]
                x2 = approx[0][0][0]                
                y2 = approx[2][0][0]

                # koordinatları kaydediyorum
                xy.append((x1,y1,x2,y2))

                #x1y1 x2y2 adresleri ile dörtgenleri kırpıyorum
                rect = img[x1:y1,x2:y2]

                # kesilen bölgeyi okunma ve birleştirme
                #  işlemi için hazır olmasını sağlıyorum
                rect = cv2.resize(rect,(100,100))
                rect = cv2.GaussianBlur(rect,(1,1),cv2.BORDER_DEFAULT)
                _, rect = cv2.threshold(rect,127,255,cv2.THRESH_BINARY)

                # kırpılan fotograf kaydedilir
                path = f"{dirName}/{counter}.jpeg"
                cv2.imwrite(path,rect)
                counter+=1
    return dirName, xy ,img_name

def zero2IMG(path):

    # dosyayı geziyorum
    for p in sorted(os.listdir(path)):
        
        # path adresini alıyorum
        newPath = os.path.join(path,p)

        # fotografı okuyorum
        img = cv2.imread(newPath,0)
        
        # ortalaması 253ten buyukse bos bir fotodur
        if np.mean(img)>253:

            # sıfırı yazmak için pozisyon alıyorum
            position = (30,70)

            # yazıyı ekliyorum
            cv2.putText(
                img, #fotograf
                "0", # yazılacak text
                position, # pozisyon
                cv2.FONT_HERSHEY_SIMPLEX, #font türü
                2, #font büyüklüğü
                (0, 0, 0), #font rengi
                3) #font gücü


            # sıfırlı fotoğrafı kaydediyorum
            cv2.imwrite(newPath,img)

def concatIMG(path):

    # Bos bir img olusturuyorum
    img_list = np.zeros((900,900,3))
    for cnt,pth in enumerate(sorted(os.listdir(path))):
        # Fotografı okudum
        newPath = os.path.join(path,pth)
        img = cv2.imread(newPath)
        
        # buyuk fotograftaki nereye kaydedecegimi buluyorum
        x1 = (cnt // 9) * 100
        y1 = (cnt % 9)  * 100 
        x2 = x1 + 100
        y2 = y1 + 100 

        # Fotoğrafa ekliyorum
        img_list[x1:x2,y1:y2] = img
     
    # Fotografı kaydediyorum
    pathIMG = 'temp/img.jpeg'
    cv2.imwrite(pathIMG, img_list)

    # Nereye kaydettiğimi donuyorum
    return pathIMG

def transformIMG(path):

    # Fotografı okuyorum
    img = cv2.imread(path)

    # fotografı text haline ceviriyorum
    
    txt = pytesseract.image_to_string(img)

    # olusturdugum text degiskenini geri donuyorum
    return txt

def transformIMG(path):
    list1,list2=list(),list()
    for i in sorted(os.listdir(path)):
        img = cv2.imread(os.path.join(path,i))
    
        temp = pytesseract.image_to_string(img,
            config='--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789')
        list1.append(temp.strip())
    
        temp = pytesseract.image_to_string(img,
            config='--oem 3 --psm 13 -c tessedit_char_whitelist=0123456789')
        list2.append(temp.strip())
    i = 0
    m = list()
    while i < 81:
        temp1,temp2=None,None
        try:
            temp1 = int(list1[i])         
        except:
            pass
        try:
            temp2 = int(list2[i]) 
        except:
            pass        

        if temp1==temp2 and type(temp1)==int:
            m.append(temp2)
        elif type(temp1)==int :
            m.append(temp1)
        elif type(temp2)==int :
            m.append(temp2)
        else:
            return False
        i+=1
    return m


def txt2mat(temp):

    # gelen text dosyasındaki sayıları alıyorum
    text = ""
    for i in temp:
        if i in "0123456789":
            text = text + i

    # aldıgım sayıları 9 satıra boluyorum
    temp_list = []
    for i in range(0,73,9):
        temp_list.append(text[i:i+9])
        
    # tum satirlari int degerlere ceviriyorum 
    matrix = [[] for j in range(9)]
    i = 0
    while i<9:
        matrix[i][:0] = temp_list[i] 
        j=0
        while j<9:
            matrix[i][j] = int(matrix[i][j])
            j+=1
        i += 1

    # Olusturdugum int matrixi donuyorum
    return matrix

def removeFILES(path):
    shutil.rmtree(path)

def solution_func(matrix):
    solution = Sudoku(matrix)
    if solution.flag:
        return solution.matrix
    else:
        print("hatalı işlem")

def writeAnswer2IMG(imgname,path,xy,mat1,mat2):
    try:
        os.mkdir("Solution")
    except:
        pass
    
    img = cv2.imread(path)
    cnt = 0
    j,cnt = 0,0

    while j<9:
        i = 0
        while i < 9:

            # eğer eski eleman değil ise
            # yeni değerleri yazıyorum
            if mat1[i][j]!=mat2[i][j]:

                # yazılacak rakamı alıyorum
                text = mat2[i][j]

                # yazılacak pozisyonu belirliyorum
                x = (xy[cnt][0] + xy[cnt][1]) // 2
                y = (xy[cnt][2] + xy[cnt][3]) // 2
                position = (x-10,y+15)

                # yazıyı ekliyorum
                cv2.putText(
                    img, #fotograf
                    str(text), # yazılacak text
                    position, # pozisyon
                    cv2.FONT_HERSHEY_SIMPLEX, #font türü
                    1.4, #font büyüklüğü
                    (0, 255, 0), #font rengi
                    3) #font gücü    

            cnt+=1
            i+=1
        j+=1

    cv2.imwrite(f"Solution/solution{imgname}.jpeg",img)

def solver(path):

    dirName, xy, img_name = cropIMG(path)
    zero2IMG(dirName)
    # pathIMG = concatIMG(dirName)
    # temp = transformIMG(pathIMG)
    print(transformIMG(dirName))
    temp = asd
    print(temp)
    matrix = txt2mat(temp)
    oldMatrix = copy.deepcopy(matrix)
    # removeFILES("temp")
    solutionMatrix = solution_func(matrix)
    writeAnswer2IMG(img_name,path,xy,oldMatrix,solutionMatrix)
   

if __name__=="__main__": 
    solver("../trainingData/20.png")
