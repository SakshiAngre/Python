#functions help in reusability and modularity
#without fuunction
"""a=4
b=4
c=5

average=(a+b+c)/3
print(average)

a=5
b=9
c=50

average=(a+b+c)/3
print(average)"""



def average(a,b,c): #function defining
    avg =(a+b+c)/3
    print(avg)

average(3,3,3) #function calling
average(5,5,5)

#or  
def average1(a1,b1,c1):
    avg1= (a1+b1+c1)/3
    return avg1  #while we want to print message with it we need return

av1=average1(5,6,7)
av2=average1(4,5,6)

print("avrage is",av1)
print("avrage is:",av2)

