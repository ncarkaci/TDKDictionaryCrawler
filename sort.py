#!/usr/bin/env python
#
# Türkçe kelimelerin sıralamasında python dilinde problem yaşanmaktadır.
# Her ne kadar locale dosyası Türk diline uygun konfigüre edilerek bu problem çözülmeye çalışılsa da
# "â", "ı" ve "i" vb. gibi karakter içeren kelimeler arasında doğru sırada yapılamamaktadır.
# Bu fonksiyon Türkçe kelimelerin alfabeye göre doğru sıralanmasını sağlar.
#
# Author: Necmettin Çarkacı
#
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : sort.py filename

'''
    Türkçe kelimelerin alfabeye göre doğru sıralanmasını sağlar. Aynı zamanda alfabede olmayan
    fakat kelimelerde olan karakterleri de alfabenin sonuna akleyerek sıralama ölçütünü gösterir.

    @param list kelime_listesi : Sıralanacak kelimelerin listesi
    @return list : Türk alfabesine göre sıralanmış kelime listesi
'''

import sys

def sırala(kelime_listesi):
    alfabe = ' aâbcçdefgğhıîijklmnoöprsştuûüvyz'  # Başlangıç alfabesi

    # Kelimelerde yer alan fakat alfabede olmayan karakter için alfabeyi güncelle. Örn : -/ karakterleri
    for kelime in kelime_listesi:
        harf_listesi = list(kelime)
        for harf in harf_listesi:
            if harf not in alfabe:  # harf alfabede yoksa sonuna ekle
                alfabe = alfabe + harf

    print('Alfabe : ' + alfabe)

    ''' 
        Alfabedeki harfler için sayısal değerler üretip bunları bir listede tutan ve 
        listenin indeksine göre sıralama yapar. Belirtilen kaynaktan alınmıştır.

        # @source : istihza python
        # @url : https://belgeler.yazbel.com/python-istihza/gomulu_fonksiyonlar.html
    '''

    def sıralayıcı(kelime):
        çevrim = {i: alfabe.index(i) for i in alfabe}
        return ([çevrim.get(kelime[i]) for i in range(len(kelime))])

    sorted_list = sorted(kelime_listesi, key=sıralayıcı)

    return sorted_list

'''
    Kelimelerden oluşan dosyayı alır, içindeki kelimeleri Türk alfabesine göre sıralayarak
    sıralı kelimelerden oluşan yeni bir dosya oluşturur.
    
    @param string filename : sıralanacak kelimeleri içeren dosyanın adı
'''
def dosya_sırala(filename):

    # Dosyadan kelimeleri oku
    print(filename+' dosyasının içeriği okunuyor ...')
    with open(filename, 'r') as input_file:
        dosya_icerigi = input_file.read()
        kelime_listesi = dosya_icerigi.split()

        # Kelimeleri sırala
        print('Kelimeler sıralanıyor ...')
        sorted_kelime_listesi = sırala(kelime_listesi)

    # Sıralanmış kelimeleri dosyaya yaz
    output_file_name = 'sorted_'+filename
    print('Sıralnamış kelimeler '+output_file_name+' dosyasına yazılıyor ...')
    with open(output_file_name,'w') as output_file:
        output_file.writelines(["%s\n" % word for word in sorted_kelime_listesi])


if __name__ == '__main__':

    filename = sys.argv[1]
    dosya_sırala(filename)


