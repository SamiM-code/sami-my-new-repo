def do_factorial(input):
    #convert to int
    myinput = int(input)
    calc = []
    for i in range(1,myinput+1,1):
        calc.append(i)
        if i < myinput:
            calc.append("*")
        #convert list back to string for eval
        #print(calc)
        #convert a list of str and int to string
        my_result_string = ' '.join(map(str,calc))
        #print(my_result_string)
    return eval(my_result_string)

user_input = input("Please give me number from where we will calculate factorial: ")
result = do_factorial(user_input)
print(result)
