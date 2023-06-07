# Хакер василийполучил доступ к классному журналу
# хотел заменить оценки мин на макс
# напишите программу, которая заменяет оценки наоборот
# макс на мин
# n = int(input("Введите количество оценок "))
# list = [int(i) for i in input("Введите оценки: ").split()]
# for i in range(len(list)-1):
#     if list[i] > 3:
#         list[i] = 1
#         i += 1
# print(list)  
n = int(input())
array = [int(i) for i in input().split()][:n]
min_value = array[0]
max_value = array[0]
for i in range(1, len(array)):
    if min_value > array[i]:
            min_value = array[i]
    elif max_value<array[i]:
           max_value = array[i]
for i in range(len(array)):
        if array[i] == max_value:
           array[i] = min_value
print(array)
    
        

