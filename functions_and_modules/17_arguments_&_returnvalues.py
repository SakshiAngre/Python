def add(a,b,plus=0): #plus=0 is default argument
    return a+b+plus

sum=add(4,4,2)#actual passed values are known as aruments
print(sum)

sum1=add(a=6,b=6)#keyword argument
print(sum1)

#one of the example of default argument
def greet(name="Guest"):
    return f"Hello, {name}!"
 
print(greet())

