# Дан список чисел. 
# посчитайте сколько в нем пар элементов равных друг другу
n = int(input("Введите число n "))
array = [int(i) for i in input("Введите значения массива ").split()][:n]
result = {}
for i in array:    #создаем словарь и подсчитываем элементы
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(sum([i//2 for i in result.values()]))      