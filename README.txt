# Proje-odevi-yerlestiricisi
Bu ortaokul ve lise sınıfları için bir proje ödevi yerleştiricisidir. 
Kullanım kılavuzu:
Ortaokul veya lise uygulamalrarından hangisi size uygunsa onu seçiniz.
Uygulama çalışması için Python diline ihtiyaç duymaktadır.
Uygulamayı açınız.
İlk önce sistem sizden sınıfta kaç kişi olduğunu soracaktır. Sayı biçiminde giriniz.(Örn. 23, 30, 21)
Girdikten sonra teker teker öğrenci isimlerini ve istedikleri ders numaralırını girin.
Sonra her bir ders iin bir sınır belirleyin. Bu sınır o dersten maksimum kaç kişinin proje ödevi alacağı hakkındadır.
Eğer bir derste sınırdan fazla öğrenci yazılmış ise o dersi ilk tercihe yazanların o dersten aldığı notlar alınır. En yüksek notu alanlar, o dersten proje ödevi alanlar sınıra eşitlenene kadar atılır.
Atılan öğrencileri yerleştirmek için iki seçenek sunulur.
1. Seçenekte atılan öğrenciler sınırı ile öğrenci sayısı eşit derslere yani dolu derslere yerleştirilmezler.
2. Seçenekte atılan öğrenciler o derse yerleşmiş öğrencilerle birlikte sayılır ve eğer sınırı geçerlerse tekrar not alma işlemi başlatılır ve gene en yüksek notu alanlar, o dersten proje ödevi alanlar sınıra eşitlenene kadar atılır.

Eğer 1. seçeneği seçerseniz dolu derslere yani sınırı ile öğrenci sayısı eşit derslere, önceki derslerden atılan öğrencileri yerleştiremezsiniz. Eğer yerleştirmeye çalışırsanız yazılım sizi uyaracaktır.
Her diğer tercihi dediğinde o öğrencide bi alttaki tercihi söyleyin. Yani eğer 1. tercihine Matematik 2. tercihine Türkçe 3. tercihine İngilizce(Yabancı dil) yazmış bir öğrenci var.
sistem onu Matematik dersinden notu yüksek diye çıkardı. Ve siz 1. seçeneği seçtiğinizde, yazılım onun diğer tercihini söyleyin dediğinde Türkçe demelisiniz.

