# дано натуральное число А  > 1
# определите, каким по счету числом Фибоначи оно является.
# То есть выведите такое число n, что h(n)=A.Если А не является числом 
# числом фибоначи, выведите -1

n = int(input("Введите число n "))
n0 = 0
a0 = 0
a1 = 1
i = 2
while n0 < n:
    n0 = a0 + a1
    a0 = a1
    a1 = n0
    i += 1
    if n0 > n:
        i = 0

if i != 0:
    print(i)
else:
    print(-1)
