#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def degree(m, n):
    if n == 0:
        return 1
    print 
    return m * degree(m, n - 1)
  
    


a = int(input("Введите значение числа А "))
b = int(input("Введите значение числа В "))
print (degree(a,b))