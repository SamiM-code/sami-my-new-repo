def draw_triangle():
    #Set variables
    min = 1
    max = 10 

    for i in range(min,max,1):
        #print("i is: ",i)
        if i < 6:
            for a in range(0,i,1):
                print("*",end=" ")
        else:
            for a in range(i,max,1):
                print("*",end=" ")
        print("")
draw_triangle()
