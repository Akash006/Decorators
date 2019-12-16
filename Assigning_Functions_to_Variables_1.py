#       Assigning Functions to Variables

'''
we create a function that will add one to a number
whenever it is called. We'll then assign the
functionto a variable and use this variable to call
the function.
'''

def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)
