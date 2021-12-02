#!/usr/bin/env python
#
# Verilen kelime dosyası içerisindeki kelimelerin n-gram'larını çıkararak dosyaya yazar.
# Örn : arabacı kelimeis için 2-gram : [ar, ra, ab, ba, ac, cı]
#
# Author: Necmettin Çarkacı
#
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : n-gram.py sozluk.txt


import sys # Komut satırından paramtre okumak için
from nltk import ngrams # Kelimeler için n-gram değer üretmek için


'''
    Verilen dosyadaki kelimeleri okur ve bu kelimelere ait n-gram alt kelime gruplarını oluşturarak bir dosyaya yazar.
    Alt kelime guruplarını dosyay sıralı olarak yazar.
        
    @param string dosya_adi : Kelime listeleri içeren dosya.
    @param int n-gram : Kelimelerin alt kelime gruplarının bulunacağı alt kelime uzunluğu
   
    @return list : Alt kelime listesi 
'''
def find_ngrams(dosya_adi, n):

    # Sıralanmış kelimeleri dosyaya yaz
    output_file_name = str(n)+'_gram_'+dosya_adi
    print('Sıralanmış kelimeler '+output_file_name+' dosyasına yazılıyor ...')
    with open(output_file_name,'w') as output_file:

        # Dosyadan kelimeleri oku
        print(dosya_adi + ' dosyasının içeriği okunuyor ...')
        with open(dosya_adi, 'r') as input_file:
            dosya_icerigi = input_file.read()
            kelime_listesi = dosya_icerigi.split()

        for kelime in kelime_listesi:
            harfler = list(kelime)

            kelime_n_gram = ngrams(harfler,n)

            for ngram in kelime_n_gram:
                word = ''.join(list(ngram))
                output_file.write('\n'+word)



if __name__ == '__main__':
    dosya_adi = sys.argv[1]
    find_ngrams(dosya_adi,8)