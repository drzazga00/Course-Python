import os
import modul_03 as f

plik = input('Podaj nazwe pliku: ')


def main():
    f.check(plik)
    f.czy_dodac(plik)
    f.show(plik)
    

if __name__ == "__main__":
    main()
