dlugosc = int(input('podaj ocene pod wzgledem dlugosci 1-10:'))
ogolne = int(input('ogolne wrazenie 1-10:'))
okladka = int(input('ocena okladki 1-10:'))

sred = (dlugosc + ogolne + okladka)/3

if sred>7:
    print('BARDZO DOBRY')
elif sred>4:
    print('PRZECIETNA')
else:
    print('NIE WARTA UWAGI')
    
