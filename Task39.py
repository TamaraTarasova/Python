# Даны два массива чисел. Требуется вывести те элементы первого
# массива (в том же порядке), которых нет во втором массиве. 
# Пользователь водит число N - количество эл. в 1 массиве 
# затем элементы массива.Затем число М - количество элементов во втором массиве.
# Затем эл 2 массива

n = int(input("Введите число n "))
array_1 = [int(i) for i in input("Введите значения массива ").split()][:n]
m = int(input("Введите число m "))
array_2 = [int(i) for i in input("Введите значения массива ").split()][:m]
for i in array_1:
    if i not in array_2:
        print(i,end = ' ')       