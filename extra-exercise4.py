def read_string():
    string = input("Please give me a list of things, separated by commas: ")
    status = "null"
    while status != "ok":
        if "," not in string:
            status = "nok"
            string = input("Please give me a list of things, separated by commas: ")
        else:
           status = "ok"
        continue
    return string

def print_list(my_string):
    list = my_string.split(",")
    print("List is: ",list)
    size_of_list = len(list)
    print("Size of list is: ",size_of_list)
    for item in range(len(list)):
        if size_of_list == 1:
            print(list[item],end="")
        elif item == (size_of_list - 2):
            print(list[item],"and",list[item + 1],end="")
            #No need to proceed to final loop, item + 1 was printed already
            break
        else:
            print(list[item],end=",")
       
    print("")
my_string = read_string()
print_list(my_string)

