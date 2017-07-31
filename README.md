# Türk Dil Kurumu (TDK) Türkçe Sözlük Kelime Toplayıcı / Turkish Language Institue Dictionary Crawler

Türk Dil Kurumu (TDK) web sayfasından [http://www.tdk.gov.tr/](http://www.tdk.gov.tr/) Türkçe kelimeleri toplayarak Türkçe kelime dosyası oluşturur. Son çalıştırdığında program toplam 76187 kelime toplamıştır. Toplanan kelimeler Türk diline ait özelliklerinin çıkarılması, şifre saldırıları ve kriptanaliz işlemlerinde kullanılabilir.

Collect Turkish language word from Turkish Language Institue web site [http://www.tdk.gov.tr/](http://www.tdk.gov.tr/) and create turkish word file. It can be useful for cryptanalysis and brute force password attacks and appeare other turkish language features.

# Türkçe kelime sıralayıcısı

Python dilinde Türkçe karakter içeren kelimeleri sıralamak istediğimizde doğru sıralama sonuçları döndürMemektedir. Her ne kadar locale dosyası Türk diline uygun konfigüre edilerek bu problem çözülmeye çalışılsa da "â", "ı" ve "i" vb. gibi karakterleri içeren kelimeler arasında doğru sıralama yapılamamaktadır. Özellikle "ı" ve "i" harfi içeren kelimeler doğru şekilde sıralanamaktadır. Bu problem için [isithza.com](https://belgeler.yazbel.com/python-istihza/gomulu_fonksiyonlar.html) adresinde çözüm önerilmiştir. Bununla birlikte ".", "/",","â" vb. gibi karakterler için önerilen yöntem çalışmamaktadır. İlgili yöntem tüm karakter kümeleri için düzenlenerek Türkçe kelimeler için sıralama yapacak python fonksiyonu oluşturulmuştur. İlgili fonksiyon TDK ve Zemberek sözlük birleştirilmesiyle elde edilen sözlük sıralanmasında kullanılarak test edilmiştir.

# Sözlük birleştirici

Zaman zaman elimizde birden fazla sözlük dosyası yer almakta ve bu dosyaları tek bir dosya altında birleştirmek istemekteyiz. Bu durumda çözülmesi gereken iki problem bizi bekliyor; ilk olarak dosyalar birleştirilince tekrar eden kelimeler olmaması gerekiyor. İkinci durum ise birleştirme sonucu elde edilen dosyanın sıralanmış olması gerekiyor. Sıralama işlemi ingilizce kelimeler için problem olmazken Türkçe kelimeler de problem yaşanabilmektedir. Bu durumda bir önce başlıkta anlatılan Türkçe diline özgü sıralama fonksiyonu ile çözülmüştür. Bu amaçla kütüphane içerisinde yer alan birlestir.py betiği birden fazla sözlük içeren dosyaları tekrar eden kelimeler içermeyecek ve Türk alfabesine uygun olarak sıralanmış şekilde birleştirerek yeni bir dosya olarak kaydeder. Programa birleştirilmek üzere birden fazla dosya verilebilir.

# İstatistik

Elimizde bulunan kelimelerin istatiksel değerleri için oluşturulmuş istatistik.py kütüphanesidir. Bu kütüphane elimizde bulunan kelime listesinde kaç adet kelime geçtiği, kelimelerin uzunlukları, hangi uzunlukta ne kadar kelime olduğu, bu uzunluk değerlerine göre kelime sayısı dağılımı, kelime listesine göre harf sayıları, harf sayılarının yüzdelik dağılımı gibi istatistiki bilgileri içerir. Bu bilgilere göre TDK ve Zemberek sözlüğün farklılık içerdiği gözlenmiştir. İlerki zamanlarda bu çalışmanın çıktıları burada yayınlanacaktır. Bu verilere özellikle n-gram değerleri ve bu değerlerin istatistik çıktıları eklenmesi gelecek çalışmalar arasındadır.

TDK'dan elde edilen kelimeler içinde harflerin kullanım sayısı ve yüzdelik dilimi Tablo'de gösterilmiştir.

| HARF | Kullanım Sayısı | Kullanım Yüzdesi |
|------|-----------------|------------------|
| a    | 83706           | 12.046           |
| e    | 62987           | 9.065            |
| l    | 56121           | 8.077            |
| i    | 51988           | 7.482            |
| k    | 49880           | 7.178            |
| m    | 40547           | 5.835            |
| r    | 38321           | 5.515            |
| ı    | 34434           | 4.956            |
| t    | 31581           | 4.545            |
| n    | 29246           | 4.209            |
| s    | 24800           | 3.569            |
| u    | 19142           | 2.755            |
| b    | 16669           | 2.399            |
| y    | 15991           | 2.301            |
| d    | 15758           | 2.268            |
| ş    | 15349           | 2.209            |
| o    | 14928           | 2.148            |
| z    | 13146           | 1.892            |
| ü    | 13006           | 1.872            |
| c    | 9106            | 1.310            |
| ç    | 9025            | 1.299            |
| p    | 8269            | 1.190            |
| g    | 8024            | 1.155            |
| h    | 7479            | 1.076            |
| v    | 7325            | 1.054            |
| f    | 5638            | 0.811            |
| ğ    | 5242            | 0.754            |
| ö    | 4980            | 0.717            |
| j    | 915             | 0.132            |
| â    | 812             | 0.117            |
| î    | 249             | 0.036            |
| ̇     | 108             | 0.016            |
| û    | 53              | 0.008            |
| -    | 26              | 0.004            |
| .    | 6               | 0.001            |
| '    | 3               | 0.000            |
| /    | 3               | 0.000            |

Benzer şekilde kelime listesinde bulunan kelimelerin uzunluklarına bakıldı ve bu değerler üzerinden kelime uzunluk dağılım değerleri çıkarıldı. Buna göre dilimizde en fazla 8, 7, 9 harften oluşan kelimeler bulunurken, en az 23 harften oluşan kelime bulunmaktadır. Kelime uzunluğu ve bu uzunluklarda kaç kelime olduğu Tablo 2'de gösterilmiştir.

| Kelime Uzunluğu | Bu Uzunlukta Kaç Kelime Kullanıldığı  | Bu Uzunlukta Kullanılan Kelime Sayısı Yüzdesi |
|-----------------|---------------------------------------|-----------------------------------------------|
| 8               | 9314                                  | 14.368578569                                  |
| 7               | 8605                                  | 13.2748141063                                 |
| 9               | 7756                                  | 11.9650735861                                 |
| 10              | 7391                                  | 11.4019931505                                 |
| 6               | 7078                                  | 10.9191323933                                 |
| 5               | 6149                                  | 9.4859769831                                  |
| 11              | 5503                                  | 8.4894017463                                  |
| 12              | 3495                                  | 5.3916880072                                  |
| 4               | 2400                                  | 3.7024467002                                  |
| 13              | 2302                                  | 3.5512634599                                  |
| 14              | 1708                                  | 2.6349079016                                  |
| 15              | 1032                                  | 1.5920520811                                  |
| 3               | 863                                   | 1.3313381259                                  |
| 16              | 459                                   | 0.7080929314                                  |
| 17              | 247                                   | 0.3810434729                                  |
| 2               | 212                                   | 0.3270494585                                  |
| 18              | 128                                   | 0.197463824                                   |
| 19              | 70                                    | 0.1079880288                                  |
| 1               | 47                                    | 0.0725062479                                  |
| 20              | 40                                    | 0.061707445                                   |
| 21              | 17                                    | 0.0262256641                                  |
| 22              | 3                                     | 0.0046280584                                  |
| 23              | 3                                     | 0.0046280584                                  |


TDK kelime listesine göre en uzun 23 harften oluşan kelime bulunmaktadır. 23 harften oluşan bu en uzun 3 kelime; belirsizleştirilebilmek, demokratikleştirebilmek, belirginleştirilebilmek.

# n-gram kelime listesi oluşturucu

Kelimelere ait n-gram değerlerini oluşturup bunları dosyaya yazan betik. Bu betik sonuçları istatistik betiği ile incelenecektir.

# Kelime listesi farkları ve benzerlikleri

TDK üzerinden kelimeler toplandıktan sonra bu kelime listesinin Zemberek ile güçlendirilmesi düşünmüştüm. Bu betik ile TDK sözlük ve zemberek sözlük arasında hangi kelimelerin farklı olduğunu, hangilerinin ortak olduğunu çıkarmaya çalıştım. Ayrıca istatistik kütüphanesi kullanılarak bu farklı kümeler aradasındaki değerler de ilerki zamanlarda araştırılabilir. İLk bakışta TDK'da bulunan fakat Zemberekte bulunmayan kelimeler olması beni çok şaşırttığını söyleyebilir. TDK'da olan yaklaşık 25.000 sözcük zemberekte yok. Yaklaşık 40.000 kadar kelimede ortak.

# Rastgele kelime seçme

Verilen kelime listesinden rastgele istenilen sayı kadar kelime getirir. Bu betik yazılmasından Murat Gülsoy'un Bu Kitabı Çalın isimli kitabındaki bir öyküden esinlenilmiştir. Betik her çalıştırıldığında rastgele kelimeler üretmektedir. Ayrıca sıkıcı zamanlarda arkadaşlarımla oynadığım oyununda temelidir. Oyun şu şekildedir, karşınızdaki size rastgele kelimeler verir ve sizden bu kelimeleri kullanarak bir öykü uydurmanızı ister. Sonra onun verdiği rastgele kelimelerle öyküyü devam ettirmenizi bekler. Bu durum sırayla devam eder. Daha adil olması kelimelerin tamamen rastgele seçilmesi için bu programı kullanabilirsiniz. Bu programı kullanarak oynadığınız oyun sonucunda elde ettiğiniz öyküyü yorum kısmına yazabilirsiniz.
