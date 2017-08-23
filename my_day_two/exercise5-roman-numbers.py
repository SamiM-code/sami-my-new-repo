#Create dictionary for roman characters and numbers)
romans = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
numbers = 1000,500,100,50,10,5,1
replace_dict = {"IIII":"IV","XIIII":"IX","XXXX":"XL","LXXXX":"XC","CCCC":"CD","DCCCC":"CM"}
search = ("XIIII","IIII","LXXXX","XXXX","DCCCC","CCCC")

def to_roman(input):
    myint = int(input)
    counter = myint
    #print("myint is: ",myint)
    roman_list = []
    for key in numbers: 
        #decrement counter after each loop
        #print("key is: ",key)
        #print(romans[key])
        amount = divmod(counter,key)
        #print(amount)
        #Only goes inside if statement if the checked value actually fits into given int one or more times
        if amount[0] != 0:
            #print("amount inside if: ",amount[0])
            #print("Key is: ",key)
            #romans[key]
            roman_list.append((amount[0] * romans[key]))
            #print(roman_list)
            counter = counter - amount[0] * key
        elif amount[0] == 0 and amount[1] == 0:
            break
    #Check for 4 character combinations, and change those
    #Create string again
    #result_string = ''.join(roman_list)
    #print("Roman characters before 4 set conversion: ",result_string)
    #print(result_string)
    #for replace in search:
    #    print("Replace: ",replace)
    #    print("replace_dict[replace]: ",replace_dict[replace])
    #    result_string = result_string.replace(replace,replace_dict[replace])
    #return result_string
    return roman_list

print("Roman characters are: ")
print("")
for key in romans.keys():
    print(key,"=",romans[key],end=" ")
print("")
user_input = input("Please give me an integer to convert: ")

#Check that input is actually a number
while not user_input.isdecimal():
    print("Please give a number!")
    user_input = input("Please give me an integer to convert: ")
my_roman_characters = to_roman(user_input)

for chr in my_roman_characters:
    print(chr,end="")
print("")
