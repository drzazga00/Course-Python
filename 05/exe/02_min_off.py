a = int(input('podaj a: '))
b = int(input('podaj b: '))
c = int(input('podaj c: '))

def min_off2(x,y):
    return x if x<y else y

def minimum_of(num1, num2, num3):
    return min_off2(min_off2(num1, num2), num3)

print(minimum_of(a,b,c))
