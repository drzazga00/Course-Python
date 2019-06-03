import random
my_number = random.randint(0,100)
guess=-1
i = 0
print('Guess my number!')
while i<6 and guess !=my_number :
    guess = int(input())
    if guess==my_number:
        print('brawo, moja liczba to:', my_number)
        i+=1
    elif guess>my_number:
        print('moja liczba jest mniejsza niz', guess)
        i+=1
    elif guess<my_number:
        print('moja liczba jest wieksza niz', guess)
        i+=1
if i == 6:
    print('Wygrywa komputer')


