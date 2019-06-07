import os


def add_new(plik):
    filename = plik + '.txt'
    new = input('Podaj nowa rade: ')
    with open(filename, 'a+') as p:
        p.write('* ' + new + '\n')



def check(plik):
    filename = plik + '.txt'
    
    if os.path.isfile(filename) and os.stat(filename).st_size > 0:
        with open(filename, 'r') as f:
            print('Rady odnosnie', plik,':\n')
            a = f.readline()
            counter = 1
            for a in f:
                print(' ', counter, a)
                counter +=1

    else:
        print('Nie ma takiego pliku')
def czy_dodac(plik):
    add = input('Chcesz dodaj nowa rade?(T/N): ')
    if add.upper() == 'T':
        add_new(plik)


def show(plik):
    filename = plik + '.txt'
    with open(filename, 'r') as f:
        print('Rady odnosnie', plik,':\n')
        a = f.readline()
        counter = 1
        for a in f:
            print(' ', counter, a)
            counter +=1

print('mamy to')
