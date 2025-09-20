"""
#
# Q1 print 1 to 10
for i in range(1,11):
    print(i)

#Q2 print squares from 1 to 10
for i in range(1,11):
    print(i,"^2","=", i**2)

#Q3
list=[10, 20, 30, 40, 50]
for i in list:
    print(i)

#4 Print all even numbers between 1 to 50.
for i in range(1,51):
    if i%2==0:
        print(i)

#5 pattern printing
for i in range(1,6):
    print("*"*i)#inside memory: concatenates the string with itself i times
                #"" + "*" → "*"       # first copy
                #"*" + "*" → "**"     # second copy
                #"**" + "*" → "***"   # third copy

#6 sum of first 100 natural numbers
total=0
for i in range(1,101):
    total +=i
print(total)


#7 each character on a new line.
str="python"

for i in str:
    print(i,"\n")

#8 reverse string
a="hello"
r_text=""

for i in a:
    r_text=i+r_text
print(r_text)

#9 multiplication table of any number entered by the user
num=int(input("enter any number:"))

for i in range(1,11):
    print(num*i)

#10marks = [45, 78, 88, 56, 36], count how many students scored above 50.

marks=[78, 78, 33, 51, 66]
count=0

for i in marks:
    if(i>50):
        count+=1
print("the count of stu, who score 50 is:",count)


#while loop
#1
num=1

while num<11:
    print(num)
    num=num+1 #num+=1
#2
num=10

while num>0:
    print(num)
    num=num-1

#3keep asking the user to enter a number until they enter 0.
"""
"""
#infinite loop:wrong code
while True:
    num=input("enter a num:")

    if num==0:
        print("program ended")
        break
"""       
#right one
"""while True:
    num=int(input("enter a num:"))

    if num==0:
        print("program ended")
        break"""

#sum of digits of a number (e.g., 123 → 1+2+3=6)
num=int(input("enter a num:"))
sum=0

while num>0:
    digit=num%10
    sum += digit
    num //=10 

print(sum)

