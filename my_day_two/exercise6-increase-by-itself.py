def eval_how_many_times(input1,input2):
    #convert to int
    myinput1 = int(input1)
    myinput2 = int(input2)
    counter = 1
    while True:
        output = divmod((myinput1 * counter),myinput2)
        #print("output[1] is: ",output[1])
        if output[1] == 0:
            return output[0]
        else:
            counter += 1

#Print help text
print("Please give me two numbers, and I will check how many times the first number needs to be increased by itself in order to be divided by the other number without any remainder")

#Collect user input
user_input1 = input("Please give me the first number: ")
user_input2 = input("Please give me the second number: ")

#Run function
result = eval_how_many_times(user_input1,user_input2)
print("Smallest multiplier is:",result)
print("This will make: ",int(result) * int(user_input2))
