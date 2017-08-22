def calculate_refund():
    print("Now we will calculate the refund money for small and large bottles")

    #Set refund rates for bottles
    refund_small_bottle = 0.10
    refund_large_bottle = 0.25
    print("Refund for small bottles is %.2f" %refund_small_bottle,"dollars")
    print("Refund for large bottles is ",refund_large_bottle,"dollars")

    #Collect user input
    small_bottles = input("Please give me amount of small bottles you have: ")
    large_bottles = input("Please give me amount of large bottles you have: ")

    #Calculate total refund
    total_refund = int(small_bottles) * refund_small_bottle + int(large_bottles) * refund_large_bottle

    #Print refund
    print("")
    #print("Your total refund will be: $%.2f" %total_refund)
    print("Your total refund will be: ${:.2f}".format(total_refund))

calculate_refund()
