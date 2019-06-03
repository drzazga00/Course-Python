

def uzupelnij_bib():
    biblioteka = {}
    ile = int(input('Ile ksiazek? '))
    for i in range(ile):
        tytul = input('Podaj tytul: ')
        ocena = input('Podaj ocene: ')
        biblioteka[tytul] = ocena
    return biblioteka

def znajdz(tytul):
    print('Ocena dla ', tytul, 'to: ', bibl[tytul])



bibl = uzupelnij_bib()


ksiazka = input('Jaka ksiazke chcesz sprawdzic: ')

if ksiazka in bibl:
    znajdz(ksiazka)
else:
    print('nie mamy tej pozycji')
print(bibl)

