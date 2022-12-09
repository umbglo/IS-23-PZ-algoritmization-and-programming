def horisontal(l):
    print(' ' + '-' * l + ' ')
    
def vertical(s):
    print('|' + s + '|')
    
horisontal(len(s := input('введите слово: '))); vertical(s); horisontal(len(s))
