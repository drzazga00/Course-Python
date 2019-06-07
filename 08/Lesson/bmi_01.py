##wzrost = float(input('Wzrost w m'))
##waga = int(input('Waga w kg'))
##BMI = (waga/wzrost**2)
##print('Twoje BMI wynosi:',round(BMI,2))
##print('---------')
##def wzrostt():
##    wzrost = float(input('Wzrost w m: '))
##    return wzrost
##
##
##def wagaa():
##    waga = int(input('Waga w kg: '))
##    return waga

def bmi_cal(waga,wzrost):
    BMI = (waga/wzrost**2)
    print('Twoje BMI wynosi:',round(BMI,2))

    if BMI < 18.5:
        print('NIEDOWAGA')
        with open('niedowaga.txt', 'r') as nie:
            print(nie.readline())
    if 18.5 < BMI < 25:
        print('WARTOSC PRAWIDLOWA')
        
        with open('prawidlowa.txt', 'r') as pr:
            print(pr.readline())
    if BMI >25:
        print('NADWAGA')
        with open('nadwaga.txt', 'r') as nad:
            print(nad.readline())

def main():
    bmi_cal(80, 2.1)

if __name__ == "__main__":
    main()
else:
    print("jak modlu")

