# Дано число. Проверить кратно ли оно 7 и 23

a = int(input('Введите число: '))
if a%7==0 and a%23==0:
    print(f'Число {a} делится на 7 и 23 без остатка')
else:
    print(f'Число {a} не делится на 7 и 23 без остатка')