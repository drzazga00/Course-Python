print('~-~-~-~-~-~-~-FOR~-~-~-~-~-~-~-~-~-~')

fahr = range(0,200,20)
for f in fahr:
    print(f,'F \t~~', int(5/9 * (f - 32)), '\tC')

print('~-~-~-~-~-~-~-WHILE~-~-~-~-~-~-~-~-~-~')
f = 0
while f < 200:
    print(f,'F \t~~', int(5/9 * (f - 32)), '\tC')
    f+=20
