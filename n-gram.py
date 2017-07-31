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
        
    @param string filename : Kelime listeleri içeren dosya.
    @param int n-gram : Kelimelerin alt kelime gruplarının bulunacağı alt kelime uzunluğu
   
    @return list : Alt kelime listesi 
'''
def find_ngrams(filename, n):

    # Sıralanmış kelimeleri dosyaya yaz
    output_file_name = str(n)+'_gram_'+filename
    print('Sıralanmış kelimeler '+output_file_name+' dosyasına yazılıyor ...')
    with open(output_file_name,'w') as output_file:

        # Dosyadan kelimeleri oku
        print(filename + ' dosyasının içeriği okunuyor ...')
        with open(filename, 'r') as input_file:
            dosya_icerigi = input_file.read()
            kelime_listesi = dosya_icerigi.split()

        for kelime in kelime_listesi:
            harfler = list(kelime)

            kelime_n_gram = ngrams(harfler,n)

            for ngram in kelime_n_gram:
                word = ''.join(list(ngram))
                output_file.write('\n'+word)



if __name__ == '__main__':
    filename = sys.argv[1]
    find_ngrams(filename,8)