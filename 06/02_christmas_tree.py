s = int(input('Choose size of the Christmas tree: '))


def print_segment(n, szer):
    for size in range(1, n+1, 2):
        print((size * "*").center(szer))

def print_xtree(size):
    for i in range(3, size+1,2):
        print_segment(i, size)

print_xtree(s)


