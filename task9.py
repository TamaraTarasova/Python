# вычислите факториал числа п

n = int(input("Введите число n "))
i = 1
result = 1
while i <= n:
    result *= i 
    i += 1

print (f'{n}! = {result}')
    