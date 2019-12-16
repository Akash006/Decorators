#       Passing Functions as Arguments to other Functions
'''
Functions can also be passed as parameters to
other functions. Let's illustrate that below.
'''

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)

#output -> 6
