#Дана строка, изображающая арифметическое выражение вида «<цифра>±<цифра>±…±<цифра>», где на месте
#знака операции «±» находится символ «+» или «–» (например, «4+7–2–8»). Вывести значение данного
#выражения (целое число).

a = str(input('введите выражение: '))
print(eval(a))
