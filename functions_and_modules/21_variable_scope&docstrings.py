def sum(a,b):
    c=a+b #a,b& c are local variables(inside function)
    global z #This allows functions to change global variables, but excessive use of global is discouraged as it can make debugging harder.
    z=45
    return c
    

z=8 #global variable"""outside function"""
print(z)
print(sum(2,3))
print(z)

"""docstring"""

def sum(a,b):
    """this will sum two numbers"""
    c=a+b
    print(c)

print(sum.__doc__)