


##for i in range(3):
##    sub = input('Podaj przedmiot: ')
##    grade = input('Ocena w sklai 1-6: ')
##    print(sub, grade)
##
##counter = 0
##while counter <3:
##    sub = input('Podaj przedmiot: ')
##    grade = input('Ocena w sklai 1-6: ')
##    print(sub, grade)
##    counter+=1

print('Co zabierzesz na bezludna wyspe?')
elements = []
for i in range(4):
    ele = input('podaj rzecz :')
    elements.append(ele)
    print(i+1, ele)
print('Jestesmy gotowi, zabierzesz ze sobą: ')
for i in elements:
    print(' *',i)



