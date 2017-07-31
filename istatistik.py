#!/usr/bin/env python
#
# Verilen dosya ile ilgili istatistiki bilgiler üretir.
# Üretilen veriler :
# Kelimelerde bulunan harf sayısına göre kelimelerin sıralı hali, harf sayısına göre kelime adedi,
# harf sayısına göre kelime adedinin yüzdelik dağılımı, harflerin sayısı, haflerin yüzdelik dağılımı
#
# Author: Necmettin Çarkacı
#
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : istatistik.py sozluk.txt


import sys # To get parameter from commandline
import operator # To sort dictionary

'''
    Dosyada geçen kelimelerin uzunluklarını bulur ve sonuçları dosyaya yazar.
    
    @param string filename : Dosya adı
    @return dict kelime_uzunluklari : dosyada geçen kelimelerin uzunluklarını içeren sözlük
'''
def kelimelerin_uzunlugunu_bul(filename):
    kelime_uzunluklari = {}
    with open(filename, 'r') as input_file:
        dosya_icerigi = input_file.read()
        kelime_listesi = dosya_icerigi.split()

        for kelime in kelime_listesi:
            if kelime not in kelime_uzunluklari:
                kelime_uzunluklari[kelime] = len(kelime)

    sorted_kelime_uzunluklari = sorted(kelime_uzunluklari.items(), key=operator.itemgetter(1))

    # Dosyaya yaz
    output_file_name = 'sorted_kelime_uzunluklari_'+filename
    print('Uzunluklarına göre sıralanmış kelimeler '+output_file_name+' dosyasına yazılıyor ...')
    with open(output_file_name,'w') as output_file:
        for kelime_uzunlugu in sorted_kelime_uzunluklari:
            kelime, uzunluk = kelime_uzunlugu
            output_file.write(kelime+"\t"+str(uzunluk)+"\n")

    return sorted_kelime_uzunluklari

'''
    Hangi uzunlukta kaç tane kelime olduğunu ve bunların toplam kelimeler içindeki yüzdelik dilimini hesaplar. 
    Örneğin : 1 uzulukta 10 adet kelime var ve bu tüm kelimelerin %11'i.
    Çıktıları dosyaya yazar.
    
    @param list sorted_kelime_uzunluklari : Kelime ve uzunluğunu içeren tuple'lar içeren, uzunluğa göre sıralı liste.
    @return dict sorted_uzunluk_kelime_adedi : Hangi kelime uzunluğundan kaç adet olduğu 
    @info : dosya çıktısında yüzdelik sonuçların hesapları da bulunmaktadır.
'''
def uzunluklara_gore_kelime_sayisi_hesapla(sorted_kelime_uzunluklari, toplam_kelime_sayisi):

    uzunluk_kelime_adedi = {}

    for kelime_uzunlugu in sorted_kelime_uzunluklari:
        kelime, uzunluk = kelime_uzunlugu

        if uzunluk not in uzunluk_kelime_adedi:
            uzunluk_kelime_adedi[uzunluk] = 1
        else:
            uzunluk_kelime_adedi[uzunluk] +=1

    sorted_uzunluk_kelime_adedi = sorted(uzunluk_kelime_adedi.items(), key=operator.itemgetter(1))

    # Dosyaya yaz
    output_file_name = 'uzunluk_kelime_sayisi_'+filename
    print('Uzunluk değerine göre hangi uzunluktan kaç adet kelime olduğu '+output_file_name+' dosyasına yazılıyor ...')
    with open(output_file_name,'w') as output_file:
        for uzunluk_kelime_adedi in sorted_uzunluk_kelime_adedi:
            uzunluk, kelime_adedi = uzunluk_kelime_adedi
            yuzdesi = (kelime_adedi*100)/toplam_kelime_sayisi
            output_file.write(str(uzunluk)+"\t"+str(kelime_adedi)+'\t'+str(yuzdesi)+"\n")

    return sorted_uzunluk_kelime_adedi


'''
    Alfabedeki harflerin kullanım sayısı ve yüzdelik dağılımını hesaplar.
    Örneğin : a 83706 adet ve tüm harflerin toplam %11'i a harfinden oluşuyor.
    Çıktıları dosyaya yazar.

    @param string filename : Analiz yapılan dosya adı
    @param boolean lowercase : Kelime içindeki büyük harfler küçük harfe dönüştürülsün mü. Varsayılan değer Evet
    @return dict sorted_uzunluk_kelime_adedi : Harflerin adedini içeren sözlük
    @info : dosya çıktısında yüzdelik sonuçların hesapları da bulunmaktadır.
'''
def harf_sayisini_hesapla(filename, lowercase=True):

    harf_adedi = {}
    toplam_harf_sayisi = 0

    with open(filename, 'r') as input_file:
        dosya_icerigi = input_file.read()
        if lowercase:
            dosya_icerigi = dosya_icerigi.lower()

        kelime_listesi = dosya_icerigi.split()

        for kelime in kelime_listesi:
            harf_listesi = list(kelime)

            toplam_harf_sayisi += len(harf_listesi)

            for harf in harf_listesi:

                if harf not in harf_adedi:
                    harf_adedi[harf] = 1
                else:
                    harf_adedi[harf] += 1

    sorted_harf_adedi = sorted(harf_adedi.items(), key=operator.itemgetter(1))

    print('Toplam harf sayısı : '+str(toplam_harf_sayisi))

    # Dosyaya yaz
    output_file_name = 'sorted_harf_adedi_'+filename
    print('Harflerin dağılımı '+output_file_name+' dosyasına yazılıyor ...')
    with open(output_file_name,'w') as output_file:
        for harf_sayisi in sorted_harf_adedi:
            harf, sayisi = harf_sayisi
            yuzdesi = (sayisi*100)/toplam_harf_sayisi
            output_file.write(harf+"\t"+str(sayisi)+"\t"+"{0}$".format(yuzdesi)+"\n")

    return sorted_harf_adedi


if __name__ == '__main__':

    filename = sys.argv[1]
    sorted_kelime_uzunluklari   = kelimelerin_uzunlugunu_bul(filename)
    toplam_kelime_sayisi        = len(sorted_kelime_uzunluklari)
    #print('Kelimelerin uzunlukları : \n')
    #print(sorted_kelime_uzunluklari)

    uzunluklara_gore_kelime_sayisi = uzunluklara_gore_kelime_sayisi_hesapla(sorted_kelime_uzunluklari,toplam_kelime_sayisi)
    #print('Uzunluk değerine göre hangi uzunluktan kaç adet kelime olduğu : uzunluk - kelime sayısı : \n')
    #print(uzunluklara_gore_kelime_sayisi)

    harf_sayisini_hesapla(filename)
