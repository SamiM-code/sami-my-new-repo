def shift_characters(string,shift):
    #Create a list from string
    mylist = list(string)

    #Convert str to int
    myshift_int = int(shift)
    #Initialize new list
    shifted_list = []
    for i in mylist:
        #print(i)
        #print(ord(i) + myshift_int )
        #print("Shift is: ",myshift_int)
        shifted_list.append(chr(ord(i) + myshift_int))

    #print(shifted_list)
    return(shifted_list)

#help text
print("This program will be performing Ceasar cipher by shifting characters back or forth")

#Collect input
input_string = input("Please give me a message that needs to be encrypted: ")
input_shift = input("Please give me a number, how much to shift characters: ")
print("")

#Check that shift amount if actually a number
status = "null"
while status != "ok":
    try:
        val = int(input_shift)
        status = "ok"
    except:
        print("Please give a number for shift amount!")
        input_shift = input("Please give me a number again: ")
        status = "nok"

#Call shifter function
result = shift_characters(input_string,input_shift)

#Print results
print("Old plain text message was: ")
print(input_string)
print("")
print("Encrypted new message is: ")
print(result)



