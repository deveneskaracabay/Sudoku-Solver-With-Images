# Sudoku-Solver-With-Images
#### Bu sayfada yalnızca fotoğraf ile çözümden bahsedeceğim. Önceki versiyonu hakkında bilgi almak istiyorsanız [buradan](https://github.com/deveneskaracabay/SudokuSolver) ulaşabilirsiniz.
<br/>

## Hedef
Kullanıcı tarafından girilen bir sudoku fotoğrafının çözümünü gerçekleştirmek.
<br/>

## Kısaca Algoritma

1. Kullanıcı fotoğraf seçmek için **OPEN** butonuna basar.
2. Seçtiği fotoğraf çözümlenebilmek için image binarization işlemi uygulanır.
3. Bu fotoğraftaki sudokunun her bir karesi parçalanıp geçici bir klasore kaydedilir.
4. Bu fotoğraflardaki boş kutuların herbirine **0** değeri yazılır.
5. Kaydedilen bu fotoğraflar okunabilmek için birleştirilir. Bu sayede sudoku içerisindeki çizgilerden kurtuluruz.
6. Birleştirilen fotoğraflar pytesseract paketi sayesinde string veri tipine dönüştürülür.
7. String veri tipine dönüşen matrix değişkenimiz üzerinde işlem yapılabilmesi için integer veri tipine çeviririz.
8. Oluşturulan bu int matrix listesi Sudoku Sınıfı sayesinde çözümü gerçekleşir. 
9. Gerçekleşen çözümü ilk dosyamız üzerine boşluklarını doldururuz ve bu çözüm dosyasını **Solution** klasoru içerisine kaydediyoruz.
10. Geçici oluşturduğumuz klasorleri sileriz.
11. Kaydedilen çözüm dosyasını ekrana bastırıyoruz.

**Eğer 5. satırdaki işlemden sonra sudoku çözümü gerçeklenemezse, parçaladığımız 81 fotoğraf ayrı ayrı farklı konfigürasyonlarla okunup doğru matris bulunup tekrar çözüm gerçekleştiririz.** 

## Gereklilikler

Bu klasoru bilgisayarınıza indirip komut satırını bu klasorde açıp
``pip install - r requirements.txt`` yazarak gerekli paketlere sahip olabilirsiniz.

## Programdan Görüntüler
Programı çalıştırdığımızda bu ekranı görüntüleyeceğiz :
<br/>
![img1](https://github.com/deveneskaracabay/Sudoku-Solver-With-Images/blob/master/Images/1.png)
<br/>
<br/>
**OPEN** butonuna basalım.
<br/>
![img2](https://github.com/deveneskaracabay/Sudoku-Solver-With-Images/blob/master/Images/2.png)
<br/>
<br/>
Bu kısımda örnek olarak önceden hazırladığımız datasetteki 2.png dosyasıne seçeçeğiz.
<br/>
![img2](https://github.com/deveneskaracabay/Sudoku-Solver-With-Images/blob/master/trainingDataset/2.png)
<br/>
<br/>
Dosyayı seçtiğimizde programımız çalışarak bize çıktıyı bu şekilde verecektir:
<br/>
![img3](https://github.com/deveneskaracabay/Sudoku-Solver-With-Images/blob/master/Images/3.png)
<br/>
<br/>
Datasetteki **diğer sudoku örneklerine [buradan](https://github.com/deveneskaracabay/Sudoku-Solver-With-Images/tree/master/trainingDataset)**
ulaşabilirsiniz.
<br/>
<br/>
Datasetin tamamının **çözümlerine de [buradan](https://github.com/deveneskaracabay/Sudoku-Solver-With-Images/tree/master/Solution)**
ulaşabilirsiniz.

















