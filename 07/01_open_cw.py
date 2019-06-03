filename = 'kurs_tadzio.txt'


with open(filename, 'r', encoding = 'utf-8') as f:
        g = f.readlines()
for i in g:
    print('*', i)
