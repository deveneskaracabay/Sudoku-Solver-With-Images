# Sudoku-Solver-With-Images
#### Bu sayfada yalnızca fotoğraf ile çözümden bahsedeceğim. Önceki versiyonu hakkında bilgi almak istiyorsanız [buradan](https://github.com/deveneskaracabay/SudokuSolver) ulaşabilirsiniz.
<br/>

## Kısaca Algoritma
<br/>
1. Kullanıcı fotoğraf seçmek için **OPEN** butonuna basar.
2. Seçtiği fotoğraf çözümlenebilmek için image binarization işlemi uygulanır.
3. Bu fotoğraftaki sudokunun her bir karesi parçalanıp geçici bir klasore kaydedilir.
4. Kaydedilen bu fotoğraflar okunabilmek için birleştirilir. Bu sayede sudoku içerisindeki çizgilerden kurtuluruz.
5. Birleştirilen fotoğraflar pytesseract paketi sayesinde string veri tipine dönüştürülür.
6. String veri tipine dönüşen matrix değişkenimiz üzerinde işlem yapılabilmesi için integer veri tipine çeviririz.
7. Oluşturulan bu int matrix listesi Sudoku Sınıfı sayesinde çözümü gerçekleşir. 
8. Bu çözümü **Solution** klasoru içerisine kaydedip gösteririz.
