##wzrost = float(input('Wzrost w m'))
##waga = int(input('Waga w kg'))
##BMI = (waga/wzrost**2)
##print('Twoje BMI wynosi:',round(BMI,2))

def wzrostt():
    wzrost = float(input('Wzrost w m'))
    return wzrost


def wagaa():
    waga = int(input('Waga w kg'))
    return waga

def main():
    wg = wagaa()
    wz = wzrostt()
    BMI = (wg/wz**2)
    print('Twoje BMI wynosi:',round(BMI,2))

    if BMI < 18.5:
        print('NIEDOWAGA')
    if 18.5 < BMI < 25:
        print('WARTOSC PRAWIDLOWA')
    if BMI >25:
        print('NADWAGA')


if __name__ == "__main__":
    main()
