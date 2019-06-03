import random
k = 'kamien'
p = 'papier'
n = 'nozyce'
seq = [k,p,n]

print('KAMIEN - PAPIER - NOZYCE')
rundy = int(input('podaj liczbe rund:\n'))
i = 1
gracz = 0
komputer = 0

while i <= rundy:
    def wyb_gra():
        figura_gracz = input('\nWybierz kamien, papier lub nozyce:\n')
        return figura_gracz

    def wyb_komp():
        figura_com = random.choice(seq)
        return figura_com
    a = wyb_gra()
    b = wyb_komp()
    
    print('\n-- RUNDA',i,'--\n--KOMPUTER vs GRACZ:\n--', b, 'vs', a, '--')
    
    if a == b:
        print('-- MAMY REMIS! --')
    
    elif a == 'kamien' and b == n:
        print('-- WYGRYWA GRACZ --')
        gracz+=1
        i+=1
    elif a == 'kamien' and b == p:
        print('-- WYGRYWA KOMPUTER --')
        komputer+=1
        i+=1
    
    elif a == 'papier' and b == k:
        print('-- WYGRYWA GRACZ --')
        gracz+=1
        i+=1
    elif a == 'papier' and b == n:
        print('-- WYGRYWA KOMPUTER --')
        komputer+=1
        i+=1

    elif b == 'nozyce' and b == p:
        print('-- WYGRYWA GRACZ --')
        gracz+=1
        i+=1
    elif a == 'nozyce' and b == k:
        print('-- WYGRYWA KOMPUTER --')
        komputer+=1
        i+=1

print('\nWynik ostateczny po' ,rundy, 'rundach: Gracz - ',gracz,'pkt --- Komputer - ',komputer)
input('press enter...')


