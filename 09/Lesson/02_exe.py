import sys

def change(var):
    i = int(input('podaj liczbe od 1-10: '))
    index = i-1
    wartosc = input('podaj nowa wartosc: ')
    print(var)
    var[index] = wartosc
    print(var)
    
def conver(var):
    k = list(var)
    return k

def catch_err(var):
    try:
        change(var)
    except TypeError as er:
        print(er)
        prze = conver(var)
        catch_err(prze)

def main():
    krotka = (1,2,3,4,5,6,7,8,9,10)
    catch_err(krotka)
        
        


main()
