#       Functions Returning other Functions
'''
A function can also generate another function.
We'll show that below using an example.
'''

def hello_function():
    def say_hi():
        print('cool')
        return "Hi"
    return say_hi

hello = hello_function()
hello()
