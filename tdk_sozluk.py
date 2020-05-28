#!/usr/bin/env python
#
# Türk Dil Kurumu Büyük Türkçe Sözlük Kelime Toplayıcı
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : tdk_sozluk.py

import requests
import os


def kelime_topla():

    print ("Kelimeler alınıyor....")

    kelime_listesi = set()

    try:
        data_url        = "https://sozluk.gov.tr/autocomplete.json"
        response        = requests.get(data_url)
        json_data       = response.json()

        print("Bulunan toplam kelime saysısı : ", len(json_data))

        for item in json_data:

            kelime = preprocessing(item['madde'], remove_hat=False, lowercase=False)

            if kelime is not None:
                kelime_listesi.add(kelime)

        sırala_ve_yaz(kelime_listesi, './sözlükler/TDK_Sözlük_Kelime_Listesi.txt')

    except Exception as e:
        print('Bir şeyler ters gitti hata aldım. Hata :',e)


def preprocessing(kelime, remove_hat=True, lowercase=True):
    """
    Toplanan kelimeler içinde deyimler, atasözleri, birleşik kelimeler olduğu için bu kelimeler kaldırıldı.
    Bu kelimelerin kaldırılmasını istemiyorsanız. Önişlemi devredışı bırakmanız gerekecek.
    :param kelime: Önişlemden geçirilecek kelime öbeği
    :param remove_hat: Şapkalı karakterler kaldırılsın mı?
    :param lowercase: Tüm büyük harfli karakterler küçük harfe dönüştürülsün mü?
    :return: önişlemden geçirilmiş kelime
    """
    # Tüm harfleri küçük harfe dönüştür
    if lowercase:
        kelime = kelime.lower()

    # Çok kelimeden oluşan kelimeleri kaldır
    if " " in kelime:
        kelime = kelime.split(" ")[0]

    # ' işaretiyle ayrılmış kelimeleri sadeleştir
    if "'" in kelime:
        kelime = kelime.split("'")[0]

    # Sonunda virgül olan kelimelerden virgül kaldır
    kelime = kelime.replace(',', '')

    # Ünlem Kaldır
    kelime = kelime.replace('!','')

    # Şapkalı harfleri kaldır
    if remove_hat:
        kelime = kelime.replace('â', 'a')
        kelime = kelime.replace('î', 'i')
        kelime = kelime.replace('û', 'u')

    # Kelime . ya da - ila başlıyorsa kelimeyi ekleme
    if kelime[0] == "." or kelime[0] == "-":
        return None
    else:
        return kelime


def sırala(kelime_listesi):
    """
    Türkçe kelimelerin alfabeye göre doğru sıralanmasını sağlar. Aynı zamanda alfabede olmayan
    fakat kelimelerde olan karakterleri de alfabenin sonuna akleyerek sıralama ölçütünü gösterir.
    @param list kelime_listesi : Sıralanacak kelimelerin listesi
    @return list : Türk alfabesine göre sıralanmış kelime listesi
    """

    alfabe = ' aâbcçdefgğhıîijklmnoöprsştuûüvyz'  # Başlangıç alfabesi

    # Kelimelerde yer alan fakat alfabede olmayan karakter için alfabeyi güncelle. Örn : -/ karakterleri
    for kelime in kelime_listesi:
        harf_listesi = list(kelime.lower())
        for harf in harf_listesi:
            if harf not in alfabe:  # harf alfabede yoksa sonuna ekle
                alfabe = alfabe + harf

    print('Alfabe : ' + alfabe)

    def sıralayıcı(kelime):
        """
        Alfabedeki harfler için sayısal değerler üretip bunları bir listede tutan ve
        listenin indeksine göre sıralama yapar. Belirtilen kaynaktan alınmıştır.
        # @source : istihza python
        # @url : https://belgeler.yazbel.com/python-istihza/gomulu_fonksiyonlar.html
        """
        kelime = kelime.lower()
        çevrim = {i: alfabe.index(i) for i in alfabe}
        return ([çevrim.get(kelime[i]) for i in range(len(kelime))])

    sorted_list = sorted(kelime_listesi, key=sıralayıcı)

    return sorted_list


def sırala_ve_yaz(kelime_listesi, sonuc_dosyası):

    print("Toplam kelime saysısı : ", len(kelime_listesi))

    # Sonuç dosyasını alfabeye göre sırala
    print('Kelimeler alfabetik olarak sıralanıyor ...')
    kelime_listesi = sırala(kelime_listesi)

    # Bulunan kelimeleri dosyaya yaz
    print('Elde edilen kelimeler '+sonuc_dosyası+' dosyasına yazılıyor ...')
    with open(sonuc_dosyası, 'w', encoding="utf-8") as fileobject:
        fileobject.write('\n'.join(kelime_listesi))

def dosyalari_birlestir(directory="./sözlükler", sonuc_dosyası="sonuc.txt"):
    """
    Birden fazla sözlük dosyasını tek bir dosya içerisinde birleştirir. Bu amaçla
    dosyalar içerisinde tekrar eden kelimeleri çıkarır. Aynı zamanda çıktı olarak
    kelimelerin sıralı olarak bulunduğu bir dosya üretir.

    @param string filename_list : Birleştirilecek dosyaların isimlerini içeren dosya listesi
    @return : Birleştirilmiş dosya
    @warn : Bütün işlemleri bellekte yaptığı için çok boyutlu ya da çok fazla dosyada yetersiz bellek hatası alınabilir.
    """

    kelime_listesi = set()

    # Bütün dosyaların içeriği oku ve sonuç dosyasının sonuna ekle
    for filename in os.listdir(directory):
        print(filename+' dosyası okunuyor ...')
        kelime_listesi.update(set(open(os.path.join(directory, filename), encoding="utf-8").read().lower().split()))

    sırala_ve_yaz(kelime_listesi, sonuc_dosyası="./birleştirilmiş_sözlük_kelime_listesi.txt" )

if __name__ == '__main__':
    #kelime_topla()
    dosyalari_birlestir()


