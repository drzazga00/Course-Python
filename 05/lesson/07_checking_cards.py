 
def is_visa(number):
    if len(number) not in [16,13]:
        return False
    else:
        if number[0] == '4':
            return True
        else:
            return False

def is_masterCard(number):
    if len(number) != 16:
        return False
    else:
        if int(number[:2]) >= 51 and int(number[:2]) <=55:
            return True
        elif int(number[:4]) >= 2221 and int(number[:4]) <=2720:
            return True
        else:
            return False

def is_american(number):
    if len(number) !=15:
        return False
    else:
        if number[:2] == '34' or number[:2] == '37':
            return True
        else:
            return False                                        

def is_what(number):
    if is_visa(number):
        with open('visa.txt', 'a+') as f:
            f.write(number)
            f.write('\n')
        print(number.center(20), 'to visa')
    elif is_masterCard(number):
        with open('masterCard.txt', '+a') as g:
            g.write(number)
            g.write('\n')
        print(number.center(20), 'to masercard')
    elif is_american(number):
        with open('american.txt', 'a+') as d:
            d.write(number)
            d.write('\n')
        print(number.center(20), 'to american express')
    else:
        print('nie znam')


##FROM LESSON 7
with open('karty.txt', 'r') as numery:
    numer = numery.readlines()
    for i in numer:
        ii = i.replace("\n","")
        is_what(ii)


##number = input('podaj nr karty: ')     
##is_what(number)
input('press enter')
