a = input('введите трехзначное число: ')

while type(a) != int: #обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('введите целое трехзначное число!')
        a = input('введите трехзначное число: ')
    while len(str(a)) != 3:
        print('вы ввели не трехзначное число!')
        a = input('введите трехзначное число: ')
    else:
        a == a

first = a//100
second = (a - first * 100)//10
third = a - first * 100 - second * 10

if first > second > third:
    print('утверждение верно')
elif first < second < third:
    print('утверждение верно')
else:
    print('утверждение неверно')
