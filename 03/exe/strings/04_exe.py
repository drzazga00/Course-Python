tytul = input('Tytul ksiażki?? ')
autor = input('Podaj autora ')
liczba_stron = input('Podaj liczbe stron ')
print(tytul.isalpha())
print(autor.isalpha())
print(liczba_stron.isdigit())
a = tytul.title()
b = autor.title()
c = liczba_stron.title()
#book = tytul.title() + autor.title() + liczba_stron.title()
book = (a+' '+b+' '+c)
print(book)
print(len(book))


