def check_duplicates():
    #read user input
    words = []
    quit = "null"

    while quit != "yes":
        word = input("Please give me a word: ")
        if word == "quit":
            quit = "yes"
            continue
        elif word == "":
            for item in words:
                print(item)
            print("")
            continue
        if word not in words and word != "":
            words.append(word)
        for item in words:
            print(item)
        print("")

check_duplicates()
