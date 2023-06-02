# Напишите программу, которая принимает на вход строку и отслеживает
# сколько раз каждый символ уже встречался
# количество повторов добавляется к символам с помощью постфикса _n 

word = input('Введите строку: ').split()
result = {}
for i in word:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
        result[i] += 1
    else:
        print(i, end='')
        result[i] = 1
        

    # if i in result:
    #     print(f'{i}_{result[i]}', end=' ')
    # else:
    #     print(i, end='')
    # result[i] = result.get(i, 0) + 1

