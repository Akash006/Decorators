#       Decorator Use Cases

# Decorators can be useful to add functionality to a function.

def decorate_message(fun): 
    def addWelcome(site_name): 
        return "Welcome to " + fun(site_name) 

    return addWelcome 
  
@decorate_message
def site(site_name): 
    return site_name; 

print(site("Google"))

# Decorators can also be useful to attach data (or add attribute) to functions.

def attach_data(func): 
       func.data = 3
       return func 
  
@attach_data
def add (x, y): 
       return x + y
  
print(add.data) 
