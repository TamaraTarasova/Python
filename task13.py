# Пользователь вводит число N - общее количество дней
# в след строках располагается N целых чисел - температура в этот день
# сколько дней длилась оттепель, температура была выше 0

n = int(input("Введите число n "))
count = 0
max_day_positiv = 0
for i in range(n):
  x = int(input("Введите температуру дня:  "))
  if x > 0:
      count += 1
  else:
      count = 0

  if max_day_positiv < count:
      max_day_positiv = count
print(max_day_positiv)        
