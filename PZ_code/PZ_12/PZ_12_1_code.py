#В последовательности на n целых элементов в последней ее половине найти сумму элементов.

numbers = []

n = int(input('введите количество элементов в списке: '))

for i in range(0, n): #создание списка
    elements = int(input())
    
    numbers.append(elements)

if n%2: #удаление элементов первой половины списка
    while int(len(numbers)) > n/2:
        numbers.pop(0)
else: #удаление центрального элемента и элементов первой половины списка
    while int(len(numbers)) > n/2+0.5:
        numbers.pop(0)

print('сумма элементов в последней половине последовательности: ', sum(numbers))
