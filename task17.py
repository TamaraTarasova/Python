#Дан список чисел.Определите, сколько в нем встречается различных чисел
#[1, 1, 2, 0, -1, 3, 4, 4]
# 6
n = [int(i) for i in input().split()]
n = set(n)
print(len(n))    