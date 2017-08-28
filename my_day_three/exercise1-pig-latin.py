import string

vovels = ("a","e","i","o","u")
all_characters_small = string.ascii_lowercase
vovels_set = set(vovels)
all_char_set = set(all_characters_small)
consonants = vovels_set.symmetric_difference(all_char_set)

def convert_str_to_piglatin(input):
    str_list = input.split()
    converted_word_list = []
    #print(str_list)
    for word in str_list:
        movethese = []
        #Convert word str to list of characters
        character_list = list(word)
        #print("Len character_list: ",len(character_list))
        for index in range(0,len(character_list),1):
            if character_list[0] in vovels:
                #Add yay for vowels 
                #print("vovel character is: ",character_list[index])
                character_list.append("yay")
                converted_word_list.append(character_list)
                break	
            if character_list[0] in consonants: 
                #print("Index: ",index)
                movethese.append(character_list.pop(0))
                #print("Consonant appended: ",movethese)
                #loop until all consonants are popped out
                while character_list[0] in consonants and len(character_list) > 1:
                    movethese.append(character_list.pop(0))
                    #print("Consonant added: ",movethese)
                #Add all consonants at the end of word
                character_list.extend(movethese)
                #Append ay after all consonants are moved
                character_list.append("ay")
                #Add converted word to a new list of words
                converted_word_list.append(character_list)
                break
        
    return converted_word_list


print("===================================================")
print("This program will convert given string into pig latin")
print("===================================================")
print("")
print("All ascii characters are: \n",all_characters_small)
print("")
print("All characters in all_char_set are: \n",''.join(all_char_set))
print("")
print("Vovels are: \n",''.join(vovels))
print("")
print("Vovels in vovel_set are: \n",''.join(vovels_set))
print("")
print("Set difference, consonants are: \n",''.join(consonants))
print("===================================================")
print("")

user_input_string = input("Please give me a string to convert to pig latin: ")
result = convert_str_to_piglatin(user_input_string)
print("Converted string: "),
print("")
for list in result:
    print(''.join(list)," ")
