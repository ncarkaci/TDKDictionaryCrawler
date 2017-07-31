#!/usr/bin/env python
#
# Türk Dil Kurumu Büyük Türkçe Sözlük Kelime Toplayıcı
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : tdk_sozluk.py

import re, time,  requests

'''
    Türk Dil Kurumu sanal yöresine bağlanarak sistemde kayıtlı kelimeleri çekip bunları dosyaya kaydeder.
    Bu iş için TDK'nın sesli Türkçe sözlük bağlantı url'sini kullanır. Bu url yapısında her bir sözcük için
    0 ile 1 milyon arasında id değeri belirlenmiştir. Yazılan fonksiyonda bu id değerlerini sırayla ilgili
    url üzerinden çeker.
    
    @param ilk_sozcuk_id : Fonksiyonun arama yapacağı sözcük id. Fonksiyon zaman zaman time out hatası aldığından
    kaldığı yerden devam etmesi için böyle bir parametre değeri kullanıldı. 

'''
def tdk_sozluk(sozcuk_baslangic_id):

    # TDK web sayfasında kullanılan ana url
    TDK_URL = "http://www.tdk.gov.tr/index.php?option=com_seslissozluk&view=seslissozluk&kategori1=yazimay&kelimesec="
    
    # Bulunan kelimelerin yazılacağı sözlük dosyasını oluştur.
    file = open('tdk_sozluk.txt', 'a+')

    for id in range (sozcuk_baslangic_id, 999999): # TDK 1000000'lık id sistemi tuttuğu için 999999
        
        try: 
            # Bağlantı url'sini oluştur : ana url sonuna sözcük id'sini ekle
            sozcuk_id   = str(id).zfill(6) # Sol tarafa 6 tane 0 koy
            url         = TDK_URL+sozcuk_id

            # Sahte user agent profili oluştur
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            agentHeader = {'User-Agent': user_agent}
            
            # Sayfaya bağlan ve içeriği al
            if proxy['host'] != "": # proxy adres belirtilmiş ise onu kullan
                content= requests.get(url, headers = agentHeader,  proxies=proxy).text
            else :
                content= requests.get(url, headers = agentHeader).text
            
            # Sözcüğü regex'le sayfadan al    
            match = re.findall(r'<b>(.*?)<i>', content)
            
            if match:
                for text in match:
                    print (sozcuk_id+" Bulunan Kelime : %s " % str(text))
                    file.write(text+"\n") # Bulunan kelimeyi dosayanın sonuna ekle
            else: # Verilen id için kelime yoksa uyarı oluştur.
                print ("Id : "sozcuk_id+" için kelime bulunamadı.")
                
        except Exception as err: #Hata aldığında 5 sn bekle kaldığın yerden devam et. Muhtemelen time out hatası.
                print ("Hata aldım,5 sn sonra kaldığım yerden devam edeceğim. Hata : ",  err)
                file.close() # Sözlük dosyasını kapat
                time.sleep( 5 ) # 5 saniye bekle
                tdk_sozluk(id) # Kaldığın sözcük id'sinden devam et.
        finally:
            # Sözlük dosyasını kapat
            file.close()
    
if __name__ == '__main__':
    proxy = {
        'user' : '', # proxy username
        'pass' : '', # proxy password
        'host' : "", # proxy host (Kullanılmayacaksa boş bırak)
        'port' : 8080 # proxy port
    }

    proxy['host'] = "5.196.218.190" # Örnek proxy sunuxu adresi

    print ("Kelimeler alınıyor....")
    ilk_sozcuk_no = 1
    tdk_sozluk(ilk_sozcuk_no)


