import random
import time
karty_gracza = []
karty_kom = []
karty = [2,3,4,5,6,7,8,9,10,11,12,13,14]
zasady_gry ='''
1. Komputer rozdaje po 10 kart
2. '11' - walet
   '12' - dama
   '13' - krol
   '14' - as
3. Wyzsza karta wygrywa
'''
print(zasady_gry)
#print(karty)
talia = 4*karty
#print(talia)

karty_gracza = random.sample(talia, k = 10)
print('Karty gracza:\n', karty_gracza)

karty_kom = random.sample(talia, k = 10)
print('Karty komputera:\n', karty_kom)

gracz = 0
komputer = 0
i = 0
while i <10:
    print('RUNDA'.center(10),i+1,':\n    ', karty_gracza[i], 'VS', karty_kom[i])
    
    if karty_gracza[i] == karty_kom[i]:
        print('** Mamy remis')
        time.sleep(2)
        i+=1
        
    elif karty_gracza[i] > karty_kom[i]:
        print('** Wygral gracz')
        time.sleep(2)
        gracz += 1
        i+=1
        
    elif karty_gracza[i] < karty_kom[i]:
        print('** Wygral komputer')
        time.sleep(2)
        komputer += 1
        i+=1

print('Wynik ostateczny - gracz: ', gracz, 'komputer: ', komputer)
