data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

def add_zero(day):
    if len(str(day)) == 2:
        print(day, end=' ')
    else:
        print("0" + str(day), end=' ')
    
counter = 1
while counter < 12:
    print('\n',data[counter][0],'\n')
    for i in (data[counter][1]):
        if (i+1) % 7 == 0:
            add_zero(i)
            print()
        else:
            add_zero(i)

        
    counter+=1

 
