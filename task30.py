# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно 
# ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
a_1 = int(input("Введите первый элемент "))
n = int(input("Введите количество элементов "))
d = int(input("введите разность "))
for i in range(n):
   print(a_1 + i * d)
print([a_1 + i * d for i in range(n)])




























