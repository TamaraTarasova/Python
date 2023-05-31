# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть

n = int(input("Введите число n - количество монет: "))
count1 = 0
count0 = 0
min_coin_side = 0
for i in range(n):
  x = int(input("Введите на какой стороне монетка (орел - 1, решка - 0):  "))
  if x > 0:
      count1 += 1
  else:
      count0 += 1

  if count1 < count0:
      max_coin_side = count1
  else: 
      max_coin_side = count0    
print(max_coin_side) 

# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)

