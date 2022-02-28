# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

x = 1
y = 1
if (not (x or y)) == ((not x) and (not y)):
    print(True)
else:
    print(False)