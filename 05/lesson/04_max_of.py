a = int(input('podaj a: '))
b = int(input('podaj b: '))
c = int(input('podaj c: '))

def max_off2(x,y):
    return x if x>y else y

def maximum_of(num1, num2, num3):
    return max_off2(max_off2(num1, num2), num3)

max_off2(a,b)
max_of_3 = maximum_of(a,b,c)
print(max_of_3)

