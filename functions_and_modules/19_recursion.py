#recursion occurs when function calls itself
"""recursion is function calling itself to solve a problem."""





def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(2))  