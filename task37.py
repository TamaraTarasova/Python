# Дано натуральное число N и последовательность из N элементов
# Требуется вывести эту последовательность в обратном порядке

def vvod(n):
    if n == 0:
        return ' '
    k = int(input())
    return vvod(n - 1) + f' {k}'

n = int(input())
print(vvod(n))