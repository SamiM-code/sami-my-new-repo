def check_if_fizz_or_buzz():
    #Set variables
    min = 1
    max = 100

    for i in range(min,max,1):
        if i % 5 == 0 and i % 3 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


check_if_fizz_or_buzz()
