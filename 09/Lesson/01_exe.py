import sys
lista = ['a', 4, 8, 44, 77, 99, 'b', 'c', 1.88, 1.52, 0]

for i in lista:
    try:
        r = 10/i
        print(i, '=', r)
    except (TypeError, ZeroDivisionError) as er:
        print('10 nie podzielimy przez ', i, '-', er)
