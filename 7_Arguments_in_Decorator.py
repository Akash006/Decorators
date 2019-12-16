#   Accepting Arguments in Decorator Functions

'''
To define a decorator that accepts arguments.
We achieve this by passing the arguments to the wrapper function.
The arguments will then be passed to the function that is being
decorated at call time.
'''

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Delhi", "Chandigarh")
