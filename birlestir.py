#!/usr/bin/env python
#
# Birden fazla sözlük içeren dosyaları tekrar eden kelimeler içermeyecek ve
# Türk alfabesine uygun olarak sıralanmış şekilde birleştirerek yeni bir dosya olarak kaydeder.
# Programa birleştirmek için birden fazla dosya verilebilir.
#
# Author: Necmettin Çarkacı
#
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : birlestir.py filename1 filename2 .... filenameN

import sys # To get parameter from commandline
import sort # To sort word list as a Turkish alphabet

'''
    Birden fazla sözlük dosyasını tek bir dosya içerisinde birleştirir. Bu amaçla
    dosyalar içerisinde tekrar eden kelimeleri çıkarır. Aynı zamanda çıktı olarak
    kelimelerin sıralı olarak bulunduğu bir dosya üretir.

    @param string filename_list : Birleştirilecek dosyaların isimlerini içeren dosya listesi
    @return : Birleştirilmiş dosya
    @warn : Bütün işlemleri bellekte yaptığı için çok boyutlu ya da çok fazla dosyada yetersiz bellek hatası alınabilir.
'''
def dosyalari_birlestir(filename_list):

    # Dosyaların birleştirileceği sonuç çıktı sözlük dosyası
    result_filename = 'merged_file.txt'
    result_content  = ''

    # Bütün dosyaların içeriği oku ve sonuç dosyasının sonuna ekle
    for filename in filename_list:
        print(filename+' dosyası ekleniyor ...')
        with open(filename, 'r') as input_file:
            result_content = result_content+input_file.read().lower()

    words = result_content.split()

    # Aynı olan kelimeleri çıkar
    print('Aynı olan kelimeler çıkarılıyor ....')
    word_set = set(words)

    # Sonuç dosyasını alfabeye göre sırala
    print('Kelimeler alfabetik olarak sıralanıyor ...')
    words = list(word_set)
    sorted_list = sort.sırala(words)

    print('Elde edilen kelimeler '+result_filename+' dosyasına yazılıyor ...')
    with open(result_filename,'w') as output_file:
        output_file.writelines(["%s\n" % word for word in sorted_list])


if __name__ == '__main__':

    filename_list = sys.argv[1:]
    dosyalari_birlestir(filename_list)
