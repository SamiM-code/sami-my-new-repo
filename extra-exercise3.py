import random

def create_lottery_numbers():
    max_numbers = 6
    lottery_list = []
    numbers_so_far = 0
    while numbers_so_far < max_numbers:
        new_number = random.randint(1,49) 
        if new_number not in lottery_list:
            lottery_list.append(new_number)
            numbers_so_far +=1

    return lottery_list

lottery = create_lottery_numbers()
print(lottery)
