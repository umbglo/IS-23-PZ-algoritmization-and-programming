#Даны целые положительные числа N и K. Найти сумму 1**K + 2**K + ... + N**K.

n, k = input('введите первое число: '), input('введите второе число: ')

while type(n) != int: #обработка исключений
    try:                #соблюдение положительности первого числа
        n = int(n)
    except ValueError:
        print('введите целое число!')
        n = input('введите первое число: ')
    while n < 0:
        try:
            n = abs(n)
        except TypeError:
            print('неправильный ввод, попробуйте еще!')
            n = input('введите первое число: ')
    else:
        n == n
        
while type(k) != int: #обработка исключений
    try:                #соблюдение положительности первого числа
        k = int(k)
    except ValueError:
        print('введите целое число!')
        k = input('введите первое число: ')
    while k < 0:
        try:
            k = abs(k)
        except TypeError:
            print('неправильный ввод, попробуйте еще!')
            k = input('введите первое число: ')
    else:
        k == k

result = 0
for i in range(1, n + 1):
    result += i ** k
print(result)
