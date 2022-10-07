# 1. Вычислить число c заданной точностью d
# in                                                      in
# Enter a real number: 9                                  Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.000001          Enter the required accuracy '0.0001': 0.001
# out                                                     out
# 9.000000                                                8.988


num_1 = float(input('Введите действительное число: '))
num_2 = str(input('Введите требуемую точность (например: "0.0001"): '))

print(f'{num_1:.{len(num_2)-2}f}')









