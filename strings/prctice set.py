"""name="sakshi"

print(name[0])# first character
print(len(name))# last charachter
print(name[5])# length of string

#concatination python doesn't have any concat() function
a="hello"
b="world!"
print(a+" "+b)

#2. String Slicing and Indexing
text="Python Programming"

print(text[0:6])#first 6 characters
print(text[12:18])#last 6 characters
print(text[0:18:2])#every second character

print(text[::-1])#step = -1 tells Python to take characters from the end toward the beginning"""
"""
#3. String Methods and Functions
str="  i love python programming  "

print(str.strip())
print(str.title())
print(str.count("o"))

str1="abc123"

print(str1.isalnum())

#4. String Formatting and f-Strings

name="ravi"
age=56

p="the name is {} and {} is".format(name,age)
print(p)

print(f"the name is {name} and the age is {age}")

#5. String Manipulation Challenges
stri="Coding in Python is fun"
print(stri.replace("fun","awesome"))

print(stri.find("Python"))
"""
#my approach
word=input("enter a word:")
re= word[::-1]

if word == re:
    print("the word is palindrome")
else:
    print("not palindrome")    

#better approach by chatgpt
word=input("enter a word: ")
if word=="".join(reversed(word)):
    print("the word is palindrome")
else:
    print("not a palindrome")

#or

word=input("Enter a word: ")
palindrome=True

for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        palindrome = False
        break

if palindrome:
    print("The word is a palindrome")
else:
    print("Not a palindrome")


