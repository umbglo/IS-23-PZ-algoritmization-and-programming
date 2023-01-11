try:
    numbers = list(map(int, input('Введите целочисленные значения списка через пробел: ').split()))
except ValueError:
    print('введите целые числа списка!')
    numbers = list(map(int, input('Введите целочисленные значения списка через пробел: ').split()))
    
N = len(numbers)
    
while N > 1:
    i = numbers[N-1] - numbers[N-2]
    N -= 1
    if i == numbers[N-1] - numbers[N-2]:
        print(i)
    else:
        print('0')
        break
