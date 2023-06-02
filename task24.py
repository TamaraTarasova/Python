#задача про чернику, N кустов на i кусте выросло А(i) ягод
#сколько максимум соберут ягод с 3 ближайших кустов 

n = int(input("Введите число n "))
array = [int(i) for i in input("Введите количество ягод на каждом кусте ").split()]
sum = array[1]
max = 0
for i in range(-1, n-1):
    sum = array[i] + array[i+1] + array[i-1]
    if sum > max:
        max = sum
print(max)       
