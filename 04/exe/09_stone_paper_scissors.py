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
    figura_com = random.choice(seq)
    figura_gracz = input('Wybierz kamien, papier lub nozyce:\n')
    print('Pojedynek KOMPUTER vs GRACZ -- RUNDA --', i,':\n',figura_com, 'vs', figura_gracz)
    
    if figura_gracz == figura_com:
        print('MAMY REMIS!')
    
    elif figura_gracz == 'kamien' and figura_com == n:
        print('WYGRYWA GRACZ')
        gracz+=1
        i+=1
    elif figura_gracz == 'kamien' and figura_com == p:
        print('WYGRYWA KOMPUTER')
        komputer+=1
        i+=1
    
    elif figura_gracz == 'papier' and figura_com == k:
        print('WYGRYWA GRACZ')
        gracz+=1
        i+=1
    elif figura_gracz == 'papier' and figura_com == n:
        print('WYGRYWA KOMPUTER')
        komputer+=1
        i+=1

    elif figura_gracz == 'nozyce' and figura_com == p:
        print('WYGRYWA GRACZ')
        gracz+=1
        i+=1
    elif figura_gracz == 'nozyce' and figura_com == k:
        print('WYGRYWA KOMPUTER')
        komputer+=1
        i+=1

print('Wynik ostateczny po' ,rundy, 'rundach: Gracz - ',gracz,'pkt --- Komputer - ',komputer)
input('press enter...')
