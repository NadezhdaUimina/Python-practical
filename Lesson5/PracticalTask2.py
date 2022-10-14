# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные 
# хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from itertools import groupby, starmap
from os import path


def encoding (f_text: str, f_text_code: str):   # кодирование
    if path.exists(f_text) and not path.exists(f_text_code):
        with open(f_text, 'r') as my_text, \
            open(f_text_code, 'w') as my_text_code:
            text = my_text.readlines()
            for i, v in enumerate(text):
                my_text_code.write(''.join([f'{len(list(g))}{k}' for k, g in groupby(v)]))
    else: print("Ошибка, проверьте имя файлов!")


def decoding (f_text_code: str):
    if path.exists(f_text_code):
        with open(f_text_code) as my_text_code:
            num = ""
            for i in my_text_code:
                decoding = []
                for j in i:
                    if j.isdigit():
                        num += j
                else:
                    decoding.append([int(num), j])
                    num = ""
                print("".join(starmap(lambda x, y: x * y, decoding)))
    else:
        print("Ошибка, проверьте имя файла!")


encoding(input('Введите имя файла с текстом: ;'), input('Введите имя файла для записи: ')
decoding(input('Введите имя файла для декодирования: ')

