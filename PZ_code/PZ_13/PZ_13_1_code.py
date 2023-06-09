#В матрице найти максимальный положительный элемент, кратный 4.

import random

n = random.randint(1, 5)
m = random.randint(1, 5)

matrix = []

matrix = [[0] * m for i in range(n)] #создание матрицы

for i in range(n): #заполнение столбцов матрицы
    for j in range(m): #заполнение строк матрицы
        matrix[i][j] = random.randint(-100, 100)

print(matrix)

result = list(set(map(lambda x: max(x), matrix))) #максимальные значения в каждой строке

presult = []
for c in result: #фильтрация по кратности на 4 и положительности
    if c % 4 == 0 and c > 0:
        presult.append(c)
        result.pop(0)

if presult == []:
    print('нет элементов, удовлетворяющих условию задачи')
else:
    print(max(presult))
