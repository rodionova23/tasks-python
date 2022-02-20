# Удалить вторую цифру трёхзначного числа
import random
a = random.randint(100,999)
print(a)
b = str(a)
c = b[0]+b[2]
print(c)

# Второе решение
# a = -547
# number3 = a % 10
# number1 = a // 100
# new_a = number1*10+number3
# print (new_a)