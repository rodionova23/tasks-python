# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа.
import random

a = random.randint(10,99)
print (a)

b = str(a)
if b[0]>b[1]:
    print(f'в числе {b} цифра {b[0]} наибольшая')
else:
    print(f'в числе {b} цифра {b[1]} наибольшая')