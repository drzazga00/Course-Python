listagosci = input('Wprowadz imiona gosci po przecinku: ')
name = listagosci.split(',')
print(name)
for i in name:
    print('Hello', i)
