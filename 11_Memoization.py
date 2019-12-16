#       Memoization using decorators

'''
Memoization is a technique of recording the intermediate results
so that it can be used to avoid repeated calculations and speed up
the programs.
It can be used to optimize the programs that use recursion.
In Python, memoization can be done with the help of function decorators.
'''

def memoize_factorial(f): 
    memory = {}
    def inner(num): 
        if num not in memory:          
            memory[num] = f(num) 
        return memory[num] 
  
    return inner 
      
@memoize_factorial
def facto(num): 
    if num == 1: 
        return 1
    else: 
        return num * facto(num-1) 
  
print(facto(5)) 
