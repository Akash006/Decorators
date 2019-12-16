#   Createing Decorators
'''
create a simple decorator that will convert a sentence to uppercase.
We do this by defining a wrapper inside an enclosed function.
'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())

# Output -> 'HELLO THERE'

'''
Python provides a much easier way for us to apply decorators. 

@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()

'''

