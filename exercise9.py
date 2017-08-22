def draw_multiplication_table():
    #Set size of table
    min = 1
    max = 11
    
    #Print column header
    for i in range(min,max,1):
        print("\t{}".format(i),end="")
    print("")
    for row in range(min,max,1):
        #Print row header
        print(row,end ="\t")
        for column in range(min,max,1):
            print("{}".format(row * column),end="\t")
        print("")

draw_multiplication_table()
