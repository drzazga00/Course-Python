def tablica_liczb():
    z = []
    x = int(input('Podaj liczbe x: '))
    for i in range(1,x+1):
        z.append(i)
    return z

suma = sum(tablica_liczb())
print(suma)
