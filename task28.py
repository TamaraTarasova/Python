#Вводится десятичное число. Реализовать алгоритм его перевода в двоичную систему счисления через рекурсию. Нельзя использовать функцию bin()
n = int(input("Введите десятичное число: "))
r = []
def binary(m):  
    if m == 0:
        return r 
    binary(m//2)
    b = m % 2
    r.append(b)
    return r 
print(binary(n))

# вариант преподавателя
# def binary(n):
#     if n == 0 or n == 1:
#        return f'{n}'
#     return binary(n//2) + f'{n%2}'


# n = int (input ())
# print (binary(n))


