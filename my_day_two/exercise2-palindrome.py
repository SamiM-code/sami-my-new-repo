def check_palindrome(input):
    orig_list = list(input)
    print(orig_list)
    reverse_list = []
    for i in orig_list[::-1]:
        print(i)
        reverse_list.append(i)
    print(reverse_list)
    if orig_list == reverse_list:
        return True
    else:
        return False

user_input = input("Please give me a word and I will check if it a palindrome word: ")
test = check_palindrome(user_input.lower())

if test == True:
    print("The word",user_input,"is a palindrome")
else:
    print("The word",user_input,"is NOT palindrome")
