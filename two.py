def shopping():

    #Check if a number is odd or even using modulus
    for i in range(1,55):
        if i % 2 == 0:
            print("Even {}".format(i))
        elif i % 2 != 0:
            print("Not even {}".format(i))
        else:
            #pass is a placeholder, won't break your code
            pass

shopping()
