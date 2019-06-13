import sys
def party_planner(cookies, people):
    leftovers = None
    nun_each = None
    try:
        nun_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as er:
        print('Za mało ludzi :(')
        print(er)

    nun_each = cookies // people
    leftovers = cookies % people
    return(nun_each, leftovers)
