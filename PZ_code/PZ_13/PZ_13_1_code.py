#В матрице найти максимальный положительный элемент, кратный 4.

n = int(input('введите количество столбцов: '))
m = int(input('введите количество строк: '))

matrix = []

matrix = [ [0]*m for i in range(n) ] #создание матрицы

for i in range(n): #заполнение столбцов матрицы
    for j in range(m): #заполнение строк матрицы
        matrix[i][j] = int(input('введите значения матрицы '))

result = list(map(lambda x: max(x), matrix)) #максимальные значения в каждой строке

presult = []
for c in result: #фильтрация по кратности на 4
    if c % 4 == 0 and c > 0:
        presult.append(c)
        print(presult)
