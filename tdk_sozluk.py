#!/usr/bin/env python
# Türk Dil Kurumu Büyük Türkçe Sözlük Kelime Toplayıcı
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
#Usage : 

import re, time,  requests

def tdk_sozluk(sozcuk_baslangic_no):

    # TDK web sayfasında kullanılan ana url
    TDK_URL = "http://www.tdk.gov.tr/index.php?option=com_seslissozluk&view=seslissozluk&kategori1=yazimay&kelimesec="
    
    # Sözlük dosyası oluştur.
    file = open('tdk_sozluk.txt', 'a+')

    for iter in range (sozcuk_baslangic_no,999999):
        
        try: 
            # Bağlantı url'sini oluştur - Ana url sonuna sözcük id'sini ekle
            sozcuk_no   = str(iter).zfill(6) # Sol tarafa 6 tane 0 koy
            url         = TDK_URL+sozcuk_no

            # Sahte user agent profili oluştur
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            agentHeader = {'User-Agent': user_agent}
            
            # Sayfaya bağlan ve içeriği al
            if proxy['host'] != "":
                content= requests.get(url, headers = agentHeader,  proxies=proxy).text
            else :
                content= requests.get(url, headers = agentHeader).text
            
            # Sözcüğü regex'le sayfadan al    
            match = re.findall(r'<b>(.*?)<i>', content)
            
            if match:
                for text in match:
                    print (sozcuk_no+" Bulunan Kelime %s " % str(text))
                    file.write(text+"\n") # Bulunan kelimeyi dosayanın sonuna ekle
            else: # Verilen id için kelime yoksa uyarı oluştur.
                print (sozcuk_no+" - Kelime yok - ")
                
        except Exception as err: #Hata aldığında 5 sn bekle kaldığın yerden devam et. Muhtemelen bağlantı hatası 
                print ("Hata aldım,5 sn sonra kaldığım yerden devam edeceğim. Hata : ",  err)
                file.close()
                time.sleep( 5 )
                tdk_sozluk(iter)
    
    # Sözlüğü kapat
    file.close()
    
if __name__ == '__main__':
    proxy = {
        'user' : '', # proxy username
        'pass' : '', # proxy password
        'host' : "", # proxy host (Kullanılmayacaksa boş bırak)
        'port' : 8080 # proxy port
    }

    #proxy['host'] = "5.196.218.190" # Örnek proxy sunuxu adresi

    print ("Kelimeler alınıyor....")
    ilk_sozcuk_no = 1
    tdk_sozluk(ilk_sozcuk_no)


