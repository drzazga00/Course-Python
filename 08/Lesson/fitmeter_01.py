from bmi_01 import bmi_cal as m
def main():
    wzrost = float(input('Wzrost w m: '))
    waga = int(input('Waga w kg: '))
    BMI = (waga/wzrost**2)
    m(waga,wzrost)

if __name__ == "__main__":
    main()
