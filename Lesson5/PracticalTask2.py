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


def encoding (f_encoding: str):
    with open(f_encoding, 'r', encoding='utf-8') as my_f_encoding:
            # open(f_decoding, 'r', decoding='utf-8') as my_f_decoding:
        os.path.exists
        text_encoding =  my_f_encoding.writelines()
        cout = 1
        for i, v in enumerate(text_encoding):
            for i in range(v):
                if i <= v:
                    if text_encoding[i] == text_encoding[i + 1]:
                        cout += 1
                    else:
                        print(cout, text_encoding[i])
                        cout = 1
    




# decoding
encoding('Lesson/text_words.txt')

# encoding(input('Введите имя файла с текстом: '))
# 'text_words.txt '
# int(input('Введите имя файла для записи: ;')
# # 'text_code_words.txt '
# int(input('Введите имя файла для декодирования: ')
# 'text_code_words.txt '

# Мария Андреева: from itertools import groupby, starmap
# Мария Андреева: from os import path
# Мария Андреева: exists

