def decorator(func):
    def wrapper():
        print("about to execte a function")
        func()
        print("i have executed this function")
    return wrapper()

@decorator
def say_hello():
    print("Hello!")


"""
say_hello()
f=decorator(say_hello())
f()"""

#decorators with arguments
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def greet(a):
    print(f"hello! {a}")

greet("sakshi") 
