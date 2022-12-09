def TrianglePS():
    P = 3 * a
    S = a ** 2 * ((3 ** 0.5) / 4)
    return(P, S)
    
a = input('введите значение стороны равностороннего треугольника: ')

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print('введите число!')
        a = input('введите числовое значение стороны равностороннего треугольника: : ')
        
print('периметр и площадь заданного треугольника: ', TrianglePS())
