# найти дружественные числа, суммы всех делителей равны

n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i//2 + 1):
        if i % j == 0:
            summa += j
    list_1.append((i, summa))
for i in range(len(list_1)):
    for j in range(i, len(list_1)):
        if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
            print(*list_1[i])    
