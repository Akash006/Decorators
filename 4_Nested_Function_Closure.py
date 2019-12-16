#   Nested Functions have access to the Enclosing Function's Variable Scope
'''
Python allows a nested function to access the outer scope of the enclosing
function. This is a critical concept in decorators -- this pattern is known
as a Closure.
'''

def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")
