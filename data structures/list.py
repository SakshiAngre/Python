"""lists are ordered, mutable (changeable) collections of data."""

num= [1, 2, 3, 4, 5]
lettnum = [10, "hello",False, 3.14]

print(num)
print(lettnum)

#accsessing
print(num[1])
print(lettnum[False])

#slicing
print(num[-4:5])

#list methods
lists = [1, 2, 3]
 
lists.append(4) 
print(lists) 
lists.insert(1, 99) 
print(lists) 
lists.remove(2)     
print(lists) 
lists.pop() #removes last element 
print(lists)        
lists.reverse()
print(lists)     
lists.sort()        