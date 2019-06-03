##rece = {}

def ksiazka(answear):
    print('Tytul ksiazki: ')
    print(answear)
def rec(answear):
    print('Ocena: ')
    print(answear)

##i = 0
##while i < 3:
##    
##    tytul = input('Podaj tytul: ')
##    ocena = input('Podaj ocene: ')
##    i+=1
##    rece[tytul] = ocena
##
##print(rece)
##ksiazka()


biblioteka = {}
def uzupelnij_bib():
    i = 0
    while i < 3:
        tytul = input('Podaj tytul: ')
        ocena = input('Podaj ocene: ')
        biblioteka[tytul] = ocena
        i+=1
       


uzupelnij_bib()
print(biblioteka)

