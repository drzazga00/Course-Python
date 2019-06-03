import random

with open('cytaty.txt', 'r', encoding='utf-8') as quote:
    q = quote.readlines()

def showquote():
    g = random.choice(q)
    print('TWOJ CYTAT DNIA'.center(130))
    print(g.center(130))

##counter = 0
##while counter < 14:
##    showquote()
##    counter += 1
##
##for i in range(5):
##    print(q[i])

##print(q[:4])

showquote()
