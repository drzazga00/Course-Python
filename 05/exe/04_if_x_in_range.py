zakres = range(1,99)

def is_num_x_in_range(x,zakres):
    if x in zakres:
        print('tak, liczba',x, 'znajduje się w zadanym zakresie')
    else:
        print('nie, liczba',x, 'jest z poza zakresu')
    
is_num_x_in_range(6,zakres)




