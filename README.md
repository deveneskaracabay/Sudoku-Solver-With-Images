# Sudoku-Solver-With-Images
#### Bu sayfada yalnızca fotoğraf ile çözümden bahsedeceğim. Önceki versiyonu hakkında bilgi almak istiyorsanız [buradan](https://github.com/deveneskaracabay/SudokuSolver) ulaşabilirsiniz.
<br/>

## Hedef
<br/>
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
