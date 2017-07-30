#!/usr/bin/env python
#
# İki sözlük dosyası arasındaki farklı ve aynı olan kelimeleri bulur.
# Birinci sözlükte bulunan fakat ikinci sözlükte bulunmayan kelimeleri bulur ve dosyaya yazar.
# Her iki sözlükte ortak olan kelimeleri bulur ve dosyaya yazar.
#
# Author: Necmettin Çarkacı
#
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : ortak_fark.py filename_A filename_B


import sys # To get parameter from commandline
import sort # To sort word list as a Turkish alphabet

'''
    İki sözlük dosyası arasındaki farkı bulur. Fark birinci sözlüğün ikinci sözlükten farkıdır.
    Birinci sözlükte bulunan fakat ikinci sözlükte bulunmayan kelimeleri geri döner.

    @param string filename_A : İlk dosya
    @param string filename_B : İkinci dosya

    @return list : Birinci dosyada bulunan fakat ikinci dosyada bulunmayan kelime listesi
'''
def fark(filename_A, filename_B, lowercase=True):
    with open(filename_A, 'r') as input_A_file:
        dosya_icerigi = input_A_file.read()
        if lowercase:
            dosya_icerigi = dosya_icerigi.lower()

    kelime_listesi = dosya_icerigi.split()
    A_kelime_kumesi = set(kelime_listesi)

    with open(filename_B, 'r') as input_B_file:
        dosya_icerigi = input_B_file.read()
        if lowercase:
            dosya_icerigi = dosya_icerigi.lower()

    kelime_listesi = dosya_icerigi.split()
    B_kelime_kumesi = set(kelime_listesi)

    fark_kumesi = A_kelime_kumesi - B_kelime_kumesi

    fark_kelime_listesi = list(fark_kumesi)
    sorted_fark_kelime_listesi = sort.sırala(fark_kelime_listesi)

    result_filename = "fark_"+filename_A+"_from_"+filename_B
    with open(result_filename,'w') as output_file:
        output_file.writelines(["%s\n" % word for word in sorted_fark_kelime_listesi])

    print(sorted_fark_kelime_listesi)
    return sorted_fark_kelime_listesi



'''
    İki sözlük dosyası arasında ortak olan elamanları bulur.

    @param string filename_A : İlk dosya
    @param string filename_B : İkinci dosya

    @return list : Her iki dosyada bulunan kelimelerin listesi
'''
def ortak(filename_A, filename_B, lowercase=True):
    with open(filename_A, 'r') as input_A_file:
        dosya_icerigi = input_A_file.read()
        if lowercase:
            dosya_icerigi = dosya_icerigi.lower()

    kelime_listesi  char= dosya_icerigi.split()
    A_kelime_kumesi = set(kelime_listesi)

    with open(filename_B, 'r') as input_B_file:
        dosya_icerigi = input_B_file.read()
        if lowercase:
            dosya_icerigi = dosya_icerigi.lower()

    kelime_listesi = dosya_icerigi.split()
    B_kelime_kumesi = set(kelime_listesi)

    ortak_elemanlarin_kumesi = (A_kelime_kumesi - (A_kelime_kumesi - B_kelime_kumesi))

    ortak_kelime_listesi = list(ortak_elemanlarin_kumesi)
    sorted_ortak_kelime_listesi = sort.sırala(ortak_kelime_listesi)

    result_filename = "ortak_"+filename_A+"_from_"+filename_B
    with open(result_filename,'w') as output_file:
        output_file.writelines(["%s\n" % word for word in sorted_ortak_kelime_listesi])

    print(sorted_ortak_kelime_listesi)
    return sorted_ortak_kelime_listesi


if __name__ == '__main__':

    filename_A = sys.argv[1]
    filename_B = sys.argv[2]
    fark(filename_A,filename_B, lowercase=True)
    ortak(filename_A,filename_B, lowercase=True)