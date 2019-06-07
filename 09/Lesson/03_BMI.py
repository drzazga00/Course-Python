
def bmi():
    h = float(input('Twoj wzrost (m): '))
    if h < 2.5:
        w = float(input('Twoja waga (kg): '))
        bmi = w / (h ** 2)
        print("Your BMI is:", round(bmi, 2))
    else:
        print('Nie jestes raczej tak wysoki')
        print('Sprobujmy jeszcze raz')
        main()
def main():
    try:
        bmi()
    except ValueError:
        print('Wystarczy sama liczba')
        main()


if __name__ == "__main__":
    main()
