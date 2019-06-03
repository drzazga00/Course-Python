rocznikk = 1910
samochod = {'audi' : 'A4' , 'bmw' : 'M6', 'mercedes' : 's63'}
##
##a = input('podaj marke samochodu: ')
##if a in samochod:
##    b = input('podaj model auta: ')
##    if samochod[a] == b:
##        c = int(input('podaj rocznik auta: '))
##        if c < rocznik:
##            print('samochod moze byc zabytkiem')
##        else:
##            print('Twoj samochod jest za mlody')
##            
##    else:
##        print('Twojego modelu nie ma na liscie')
##        
##else:
##    print('Twojej marki nie ma na liscie')
##    
def marka():
    auto = input('podaj marke samochodu: ')
    return auto

bb = marka()

def model():
    mod = input('podaj model auta: ')
    return mod

aa = model()

def rocznik():
    rok = int(input('podaj rocznik swojego auta: '))
    return rok

cc = rocznik()

def czy_oryginalny():
    x = int(input('podaj w % ile czesci oryginalnych w twoim aucie: '))
    if x >= 75:
        print(bool(x))
    else:
        print(not bool(x))
    return x

dd = czy_oryginalny()

if bb in samochod:
    if samochod[bb] == aa:
        if cc < rocznikk:
            if dd > 75:
                print('Zólte tablice czekaja')
            else:
                print('za malo oryginalnych czesci')
        else:
            print('Twoj samochod jest za mlody')
            
    else:
        print('Twojego modelu nie ma na liscie')
        
else:
    print('Twojej marki nie ma na liscie')

