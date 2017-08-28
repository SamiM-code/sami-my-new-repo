def shopping():

    shopping_list = ["Milk","Bread","Bananas",77]
    item = input("Please enter an integer: ")
    shopping_list.append(item)

    # Comment
    len_of_list = len(shopping_list)
    while len_of_list > 0:
        # len_of_list = len_of_list - 1 is the same as following shorter notation:
        len_of_list -=1
        for item in shopping_list:
            print("item = ",item)

shopping()
