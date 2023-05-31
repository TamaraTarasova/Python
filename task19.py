# Дана последовательность из N целых чисел и число К
# Необходимо сдвинуть всю последовательность на К элементов вправо
# К - положительное число
list_1 = [int(i) for i in input().split()]
step = int(input("Введите число k "))
# 
    
result_list = list()
for i in range(len(list_1)):
  result_list.append(list_1[i - step])
print(result_list)  
