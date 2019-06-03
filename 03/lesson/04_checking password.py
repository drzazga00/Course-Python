password = input('Your password: ')

dl = len(password) > 7
print('Password length - ', dl)
print('correct_allnum - ',password.isalnum() and not password.isalpha() and not password.isdigit() )

print('one_upper -', not password.isupper() and not password.islower())

correct_allnum = password.isalnum() and not password.isalpha() and not password.isdigit()
one_upper = not password.isupper() and not password.islower()

if dl and correct_allnum and one_upper:
    print('Password correct')
else:
    print('Change your password')
