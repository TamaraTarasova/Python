# Пользователь вводит число N - общее количество арбузов
# в след строках располагается N целых чисел - вес арбуза
# найти самый тяжелый и самый легкий арбуз
n = int(input("Введите число n "))
max_massa = 0
min_massa = 1000
for i in range(n):
    x = int(input("Введите массу арбуза:  "))
    if x > max_massa:
      max_massa = x
    elif x < min_massa:
      min_massa = x
print(min_massa, max_massa)        

