book = {'овощ': 'морковь', 'мебель': 'стул'}
print(book)

a = ('фрукт', 'яблоко') in dict.items(book)
if a == False:
    book['фрукт'] = 'яблоко'
    print(book)
else:
    print(book)
