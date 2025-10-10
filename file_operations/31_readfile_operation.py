"""f = open("sakshi.txt",   "r")

content = f.read()

print(content)

f.close()"""

with open("sakshi.txt","r") as d: # with is a context manager
    content=d.read()
    print(content)