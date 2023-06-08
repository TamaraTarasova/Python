# data = list(map(int, input().split()))   // ввод данных равноценные варианты
# data = [int(i) for i in input().split()]

def same_by(characteristic, objects):
    return list(map(characteristic, objects))


values = [0, 2, 10, 6]
print(same_by(lambda x: x % 2, values))
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
def same_by(characteristic, objects):
    return sum(list(map(characteristic, objects))) == 0


values = [0, 2, 10, 6]
print(same_by(lambda x: x % 2, values))
if same_by(lambda x: x % 2, values):
    






    print('same')
else:
    print('different')
values = [0, 2, 10, 6]
# print(same_by(lambda x: x % 2, values))
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')



    def same_by(characteristic, objects):
    return len(list(filter(characteristic, objects))) == 0


values = [0, 2, 10, 6]
# print(same_by(lambda x: x % 2, values))
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')