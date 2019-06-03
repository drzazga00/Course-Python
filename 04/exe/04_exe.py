n = int(input('Podaj N do obliczenia silni:\n'))
z = 1
if n < 9:
    if n == 0:
        print(z)
    else:
        for i in range(1,n+1):
            z = z*i
            print('Wyniki silini', i,'=', z)
else:
    print('N nie moze byc wieksze niz 8')
