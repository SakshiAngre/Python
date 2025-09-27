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