#По двум заданным числам проверять является ли одно квадратом другого
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1**2 == num2:
    print(f'Число {num2} является квадратом числа {num1}')
else:
    print(f'Число {num2} не является квадратом числа {num1}')