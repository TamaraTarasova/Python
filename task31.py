# найти N-е число Фибоначи через рекурсию

def fib(n):
    if n ==0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input("Введите номер числа Фиббоначи: "))
print(fib(n))