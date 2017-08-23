def check_if_anagram(input1,input2):
    #Convert str to list
    mylist1 = list(input1)
    mylist2 = list(input2)
    #convert str to list
    print(mylist1)
    print(mylist2)

    #check that all characters from mylist1 can be found from mylist2
    if len(mylist1) != len(mylist2):
        return False

    for i in mylist1:
        if i in mylist2:
            continue
        else:
            #A single non-matching character will render result to False
            return False
        #Return true is the character compasion is able to finish

    #check that all characters from mylist2 can be found from mylist1
    for i in mylist2:
        if i in mylist1:
            continue
        else:
            #A single non-matching character will render result to False
            return False
    
    #Return true is the character comparison is able to finish both tests until this point
    return True

print("Please give me two words, I will check them if they are anagrams (containing exactly the same characters")
user_input1 = input("Please give me the first word: ")
print(user_input1)
user_input2 = input("Please give me the second word: ")
result = check_if_anagram(user_input1,user_input2)
if result == True:
    print("The given words",user_input1,"and",user_input2,"are anagrams")
else:
    print("The given words",user_input1,"and",user_input2,"are NOT anagrams")

