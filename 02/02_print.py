x = 'abrakadabra'
print(len(x)/2)
sr_index = len(x)//2
print(sr_index)
x2 = x[sr_index-1] + x[sr_index] + x[sr_index +1]
print(x2)


s1 = 'ananas'
s2 = 'kajak'
sr = len(s1)//2
s3 = s1[:sr] + s2 + s1[sr:]
print(sr)
print(s3)

quote = 'Honesty is the first chapter in the book of wisdom.'
print(len(quote))
print(quote[-7:-1])
polowa = len(quote)//2
quote[:polowa]
quote[::2]
quote[-1]
print(quote[::-1])
print(quote.replace('wisdom','friendship'))


s1 = 'kajak'
s2 = s1[::-1]
print(s2)
print(s1 == s2)


print('text text {} textt'.format(44))
