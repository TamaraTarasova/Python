#Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке 
#вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. 
##Последняя строка содержит число X

#*Пример:*

#5
#    1 2 3 4 5
#    6
 #   -> 5
n = int(input("Введите число n "))
array = [int(i) for i in input("Введите значения массива ").split()]
x = int(input("Введите число x "))
min = abs(x - array[0])
near = array[0]
for j in range(1, n):
    diff = abs(x - array[j])
    if diff < min:
        min = diff
        near = array[j] 
print(near)       


        
