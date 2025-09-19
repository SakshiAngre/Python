num=int(input("Enter a number to try your luck:"))

match num:
    case(2):
        print("you won AUDI!!!")
    case(5):
        print("you won camera!")
    case(8):
        print("you won 20$!")
    case _:
        print("better luck next time")