for i in range(5, 20, 2):
    print(i)

print('------------------------------')

list = ['Ada', 'Julia', 'Ruby']
for i in range(3):
    print(i, ':', list[i])

print('------------------------------')

password = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    password = password + str(num) + magic[num]
    print(password)
print('------------------------------')
