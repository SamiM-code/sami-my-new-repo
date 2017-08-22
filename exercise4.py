def check_vowels():

    #Set vowels list
    vowels = ["a","e","i","o","u"]

    #Collect user input
    user_input_character = input("Please insert a character for checking: ")
    while len(user_input_character) > 1:
        print("Please give a single character only!")
        user_input_character = input("Please insert a character for checking: ")

    #Check if the given character is a vowel

    if user_input_character in vowels:
         print("Given character {} is vowel".format(*user_input_character))
    elif user_input_character == "y":
         print("You gave \"y\" character, sometimes y character is a consonant, sometimes a vovel")
    else:
         print("Given character {} is a consonant".format(*user_input_character))

check_vowels()



