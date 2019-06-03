##def mood():
##    print('How are you?')
##
##mood()

##def my_mood(answear):
##    print('My mood today: ')
##    print(answear)
##
##resp = input('How are you?')
##my_mood(resp)
##

def my_mood(answear):
    return answear

resp = input('How are you?')
twiced = my_mood(resp)
print('My mood is like', twiced)
my_mood(resp)

print(my_mood(2))
