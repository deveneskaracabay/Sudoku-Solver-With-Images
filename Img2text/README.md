
# Fonksiyonların Özeti
<br/>

## Sudok Sınıfı
İçerisine **integer** veri tipinde 9*9 boyutunda bir matrix alır. Girilen bu matrixi geçerli bir sudoku olup olmadığını içerisinde bulunan **control** fonksiyonu sayesinde kontrol eder. Eğer geçerli bir sudoku değil ise **False** olarak geri döner. Ama eğer geçerli bir sudoku ise cevabını bulmak için sınıfın içerisindeki **solve** fonksiyonuna gönderir ve çözümü geri döner.
<br/>

## cropIMG Fonksiyonu
içerisine sudoku fotoğrafının adresini alır. **temp** adında bir klasor olusturur. Aldığı **path** sayesinde sudoku fotoğrafını okur. Fotoğrafa **Binarization** işlemi uygular. Bu işlem sayesinde çizgiler keskinleşir. Daha sonra fotoğrafta kareleri arıyoruz. Buldugumuz 81 adet kareyi fotoğraftan kırpıp **temp** dosyası içerisine kaydediyoruz. Bu işlemleri yaparken ileride sonucu yazarken gerekecek olan koordinatları bir liste halinde kaydediyoruz. 
<br/>

## zero2IMG Fonksiyonu
Temp dosyasında kırpılan 81 adet fotoğrafı dolaşır. Eğer fotoğraf boş ise bunu rgb kodlarını kullanarak tespit eder. Tespit ettiği boş fotoğrafların ortalarına "0" yazar.
<br/>

## concatIMG Fonksiyonu
temp dosyasında bulunan tüm fotoğrafları birleştirir. Birleştirdiği bu fotoğrafı kaydeder.
<br/>

## transformIMG Fonksiyonu
Bir üst fonksiyonda birleştirilen fotoğrafı **pytesseract** paketini kullanarak text haline getirir.
<br/>

## txt2mat Fonksiyonu
<br/>

## transformIMG2 Fonksiyonu
<br/>

## editMatrix Fonksiyonu
<br/>

## removeFiles Fonksiyonu
<br/>

## solution_func Fonksiyonu
<br/>

## writeAnswer2IMG Fonksiyonu
<br/>

## showSolution Fonksiyonu
<br/>

## solver Fonksiyonu
<br/>



