# Вам требуется написать программу, которая проверяет 
# счастливость билета.

# *Пример:*

# 385916 -> yes
a = int(input("Введите номер билета: "))
n = a//1000
m = a%1000
b = int(n // 100) + (n // 10 % 10) + (n % 10)  
c = int(m // 100) + (m // 10 % 10) + (m % 10) 
if b == c: 
    print("yes")
else:
    print("no")
    