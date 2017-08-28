def convert_to_normal(input):
    mylist = list(input)
    print("Given string in list format:")
    print(mylist)
    for i,item in enumerate(mylist):
        #print(i)
        #look head, check if there is a space and ignore it
        if mylist[i+1] == " ":
            if mylist[i+2] == "/" or mylist[i+2] == "*" or mylist[i+2] == "+" or mylist[i+2] == "-":
                #print(mylist[i+2])
                mylist[i],mylist[i+2] = mylist[i+2],mylist[i] 
        #Check if coming to an end
        if mylist[i+1] == " " and mylist[i+2] == "=":
            return mylist
        else:
            if mylist[i+1] == "/" or mylist[i+1] == "*" or mylist[i+1] == "+" or mylist[i+1] == "-":
                #print(mylist[i+1])
                mylist[i],mylist[i+1] = mylist[i+1],mylist[i]

    return mylist


user_input = input("Please give me polish notation: ")
result = convert_to_normal(user_input)
print("")
print("Converted normal format is: ")
#Convert list back to string
result_string = ''.join(result)
print(result_string)
print("Calculating result of the string:")
head, sep, tail = result_string.partition("=")
print('Equation after removing the "=" and result is: ',head)
print("Result of the arithmetic is:")
print (eval(head))
