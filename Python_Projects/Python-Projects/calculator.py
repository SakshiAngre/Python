try:
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))

    o = input("Enter operation that you want to perform:")

    match o:
        case "+":
            print(f"result is: {a+b}")
        case "-":
            print(f"result is: {a-b}")
        case "*":
            print(f"result is: {a*b}")
        case "/":
            print(f"result is: {a/b}")
        case default:
            print(f"There was an error")


except Exception as e:
    print("invalid Input")

    