#A while loop is used when you don’t know in advance how many times to repeat, and the loop continues until a condition becomes False
"""
#infinite loop
while True:
    print("This will run forever!")"""
# Infinite loops are useful when a program needs to keep running continuously,
# such as in "servers, games, GUIs, embedded systems
"""while True:
    temp = read_sensor()
    if temp > 50:
        print("High temperature warning!")
"""
# They must include a break condition or external stop to avoid resource issues.

i=1;
while i<6:
    print(i)
    i=i+1