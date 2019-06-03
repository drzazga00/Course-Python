import random

string_VOWEL = 'aeiouy'
string_CONSONANT = "bcdfghjklmnpqrstvwxz"

def generate_name():
    name_letters = [first_letter]
    letters = 0
    while letters < name_length/2:
        literki = []
        x = random.choice(string_CONSONANT)
        y = random.choice(string_VOWEL)
        literki.append(x)
        literki.append(y)
        random.shuffle(literki)
        name_letters += literki 
        letters = letters + 1 
    name = "".join(name_letters)
    name = name.capitalize()
    return name

first_letter = input("Podaj pierwszą literę imienia bohatera: ")
name_length = int(input("Podaj długość imienia bohatera: "))

created_name = generate_name()

number_list = ["I", "II", "III", "IV", "V"]
number = random.choice(number_list)
title_list = ["Groźny", "Grabieżca", "Nieustraszony", "Parszywy"]
title = random.choice(title_list)


print(created_name + " " + number + " " + title)
