#!/usr/bin/env python
#
# Verilen kelime listesinden rastgele istenilen sayı kadar kelime getirir.
# Bu betik yazılmasından Murat Gülsoy'un Bu Kitabı Çalın isimli kitabındaki bir öyküden esinlenilmiştir.
#
# Author: Necmettin Çarkacı
#
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : kelime_getir.py sozluk.txt kelime_sayisi

import sys # Komut satırından paramtre okumak için
from random import randint # Rastgele kelime üretebilmek için

'''
    Verilen dosyanın içerisinden rastgele istenilen sayı kadar kelime seçer ve bu kelimeleri geri döndürür.
    
    @param string filename : Kelimelerin yer aldığı dosyanın ismi
    @param int kelime_sayisi : Geri döndürülecek kelime adedi. Varsayılan değeri 6'dır.
    
    @return list : Rastgele seçilmiş kelimelerden oluşmuş kelime listesi
'''
def rastgele_kelime_getir(filename, kelime_sayisi = 6):

    kelimeler = []
    with open(filename, 'r') as input_file:
        dosya_icerigi = input_file.read()

        kelime_listesi = dosya_icerigi.split()

        for i in range(0,int(kelime_sayisi)):
            index = randint(0, len(kelime_listesi))
            kelimeler.append(kelime_listesi[index])

    return kelimeler

if __name__ == '__main__':

    filename = sys.argv[1]

    if len(sys.argv) > 2:
        kelime_sayisi = sys.argv[2]
        kelimeler = rastgele_kelime_getir(filename,kelime_sayisi)
    else :
        kelimeler = rastgele_kelime_getir(filename)

    print(kelimeler)