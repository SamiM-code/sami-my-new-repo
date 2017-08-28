def check_if_integer():
    user_input = int(input("Please give me an integer: "))
    if user_input % 2 == 0:
        print("The number {} you gave is even number".format(user_input))
    else:
        print("The number {} you gave is odd number: ".format(user_input))

check_if_integer()
