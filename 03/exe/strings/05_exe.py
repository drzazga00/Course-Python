zdanie = input('Wprowadz zdanie: ')
if zdanie == zdanie[::-1]:
    print('Twoje zdanie jest palindromem!')
else:
    print('Niestety twoje zdanie nie jest palindromem :(')
