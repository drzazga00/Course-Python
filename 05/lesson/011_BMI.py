##wzrost = float(input('Wzrost w m'))
##waga = int(input('Waga w kg'))
##BMI = (waga/wzrost**2)
##print('Twoje BMI wynosi:',round(BMI,2))

def wzrostt():
    wzrost = float(input('Wzrost w m'))
    return wzrost
wz = wzrostt()
print(wz)

def wagaa():
    waga = int(input('Waga w kg'))
    return waga

wg = wagaa()

BMI = (wg/wz**2)
print('Twoje BMI wynosi:',round(BMI,2))

if BMI < 18.5:
    print('NIEDOWAGA')
if 18.5 < BMI < 25:
    print('WARTOSC PRAWIDLOWA')
if BMI >25:
    print('NADWAGA')
