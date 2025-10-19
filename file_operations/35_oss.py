import os

a= os.listdir("directory")
print(a)
#
print(os.getcwd())
print(os.path.exists("directory")) 
os.remove("sample.txt")
os.rmdir("dir")