import random
my_number = random.randint(0,20)
secret_num=-1
print('Guess my number!')
while secret_num !=my_number :
    secret_num = int(input())
    if secret_num==my_number:
        print('Nice, my nymber is:', my_number,'!')
##    elif secret_num>my_number:
##        print('moja liczba jest mniejsza niz', guess)
##    elif secret_num<my_number:
##        print('moja liczba jest wieksza niz', guess)
    else:
        print('Try again!')
