#       Debugging Decorators
'''
When you use a decorator, you're replacing one function with another.
In other words, if you have a decorator
'''

from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

print(f.__name__)  # prints 'f'
print(f.__doc__)   # prints 'does some math'
