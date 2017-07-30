# Türk Dil Kurumu (TDK) Türkçe Sözlük Kelime Toplayıcı / Turkish Language Institue Dictionary Crawler

Türk Dil Kurumu (TDK) web sayfasından Türkçe kelimeleri toplayarak Türkçe kelime dosyası oluşturur. Son çalıştırdığında program toplam 76187 kelime toplamıştır. Toplanan kelimeler Türk diline ait özelliklerinin çıkarılması, şifre saldırıları ve kriptanaliz işlemlerinde kullanılabilir.

Collect Turkish language word from Turkish Language Institue web site http://www.tdk.gov.tr/ and create turkish word file. It can be useful for cryptanalysis and brute force password attacks and appeare other turkish language features.

# Türkçe kelime sıralayıcısı

Python dilinde Türkçe karakter içeren kelimeleri sıralamak istediğimizde doğru sıralama sonuçları döndürmektedir. Her ne kadar locale dosyası Türk diline uygun konfigüre edilerek bu problem çözülmeye çalışılsa da "â", "ı" ve "i" vb. gibi karakterleri içeren kelimeler arasında doğru sıralama yapılamamaktadır. Özellikle "ı" ve "i" harfi içeren kelimeler doğru şekilde sıralanamaktadır. Bu problem için [isithza.com](https://belgeler.yazbel.com/python-istihza/gomulu_fonksiyonlar.html) adresinde çözüm önerilmiştir. Bununla birlikte ".", "/",","â" vb. gibi karakterler için önerilen yöntem çalışmamaktadır. İlgili yöntem tüm karakter kümeleri için düzenlenerek Türkçe kelimeler için sıralama yapacak python fonksiyonu oluşturulmuştur. İlgili fonksiyon TDK ve Zemberek sözlük birleştirilmesiyle elde edilen sözlük sıralanmasında kullanılarak test edilmiştir.


