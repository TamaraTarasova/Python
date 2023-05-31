#Напишите программу для печати всех уникальных значений в словаре
data = [{"V": "S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
values = set()
for i in data:
#     print(list(i.values())[0])
# print(values)
    for key in i:
        values.add(i[key])
print(values)