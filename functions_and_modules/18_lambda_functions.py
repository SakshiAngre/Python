""" Lambda functions are anonymous(not known), inline(oneliner) functions. """
square= lambda x:x*x
print("square is:",square(5))

sum= lambda x,y:x+y
print("sum is:",sum(4,4))

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  
