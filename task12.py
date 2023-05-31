# найти числа X b Y если известна их сумма и произведение

s = int(input("Введите сумму чисел "))
p = int(input("Введите произведение чисел "))
x = (s+(s * s - 4 * p) ** 0.5)/2
y = s - x
print(x, y)

# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)