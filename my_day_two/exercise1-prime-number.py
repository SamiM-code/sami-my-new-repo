def check_if_prime_number(number):
    for i in range(2,number,1):
        if number % i == 0:
            return False
            break
        else:
            continue
    return True
    
user_input = int(input("Please give me a number, and I will check if it is a prime number or not: "))
result = check_if_prime_number(user_input)
if result == True:
    print("The number",user_input,"is a prime number")
else:
    print("The number",user_input,"is not a prime number")


