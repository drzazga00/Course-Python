czesci = 75

def czy_ogyginalny(x):
    if x >= czesci:
        print(bool(x))
    else:
        print(not bool(x))
    return x
czy_ogyginalny(75)
