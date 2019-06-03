print('____________________zad1________________\n')

plecak = ['jedzenie', 'woda', 'kurtka', 'czapka', 'GPS']
plecak.sort()
print(plecak,'\n')

print('____________________zad3________________\n')
lista = []

for i in range(0,5):
    cyfra = input('podaj liczbe:\n')
    lista.append(cyfra)
if lista[0] == lista[-1]:
    print('Pierwszy element jest taki sam jak ostatni')
else:
    print('Pierwszy element rozni sie od ostatniego')

print(lista,'\n')

print('____________________zad5________________\n')
dane = [
['Dorota', 'Wellman', 'dziennikarka'],
['Adam', 'Małysz', 'sportowiec'],
['Robert', 'Lewandowski', 'piłkarz'],
['Krystyna', 'Janda', 'aktorka']
]

for i in range(3):
    name = input('podaj imie: \n')
    surname = input('podaj nazwisko:\n')
    job = input('podaj zawod:\n')
    dane.append([name, surname, job])

print(dane)
print()

for i in dane:
    print('\t'.join(i))

for i in dane:
    print(i[0],i[1],i[2])

print('Imie \tNazwisko \tZawod')
print(dane[0][0],'\t',dane[0][1],'\t',dane[0][2])
print(dane[1][0],'\t',dane[1][1],'\t', dane[1][2])
print(dane[2][0],'\t',dane[2][1],'\t', dane[2][2])
print(dane[3][0],'\t',dane[3][1],'\t', dane[3][2])


