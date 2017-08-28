# Credit card vendors variables
Credit_Card_Vendors_Dict = {"VISA": [4], "MASTERCARD": [51, 52, 53, 54, 55], "AMEX": [34, 37],"DISCOVER":[60]}

# VISA = 4   -->16 numbers
# MASTERCARD = (51, 52, 53, 54, 55)  -->16 numbers
# AMEX = (34,37) -->15 numbers

class CreditCard:
    def __init__(self, card_number):
        pass
        self.card_number = str(card_number)
        self.card_type = ""
        self.valid = False
        print("========================================")
        print("Testing credit card: ", self.card_number)

        self.check_length()
        if self.valid == True:
            self.determine_card_type()
            if self.valid == True:
                self.validate()
                print("Vendor: ",self.card_type)
                print("Number: ",self.card_number)
                print("Valid:  ",self.valid)

    def determine_card_type(self):
        # Set default value for card type

        #Set default values for type and validity, if nothing from the Vendors dict will match, these values will be
        #retained
        self.card_type = "INVALID"
        self.valid = False

        for vendor, value in Credit_Card_Vendors_Dict.items():
            # print("vendor",vendor,"value:",value)
            # print("card number is: ",self.card_number[0:2])
            if self.card_number[0:1] == "4":
                self.card_type = "VISA"
                self.valid = True
            elif int(self.card_number[0:2]) in value:
                self.card_type = vendor
                self.valid = True

        #If value is still INVALID, the card failed vendor check
        if self.card_type == "INVALID":
            print("Card failed vendor check")
            print("Number:  ",self.card_number)
            print("Vendor:  ",self.card_type)
            print("Valid:  ",self.valid)

    def check_length(self):
        if len(self.card_number) == 15 or len(self.card_number) == 16:
            self.valid = True
        else:
            self.valid = False
            self.card_type = "INVALID"
            print("Card failed length check")
            print("Number:  ",self.card_number)
            print("Valid:  ",self.valid)

    def validate(self):
        number_adjusted = list(self.card_number)
        # print(number_adjusted)
        # even numbers from the back
        for index in range(len(number_adjusted) - 2, -1, -2):
            #print("starting point: ", index, "number", number_adjusted[index])
            # print("credit card number is: ",self.card_number)
            # print("BEFORE: index is",index,"number is: ",number_adjusted[index])
            number_adjusted[index] = str(int(number_adjusted[index]) * 2)
            # print("AFTER: index is", index, "number is: ", number_adjusted[index])
        # print("Doubled number_str is: ",number_adjusted)
        for index, val in enumerate(number_adjusted):
            # print(index, val)
            if int(val) > 9:
                # print("Found number > 10 at index: ",index,"number is: ",number_adjusted[index])
                # extract 1st number
                temp_number1 = number_adjusted[index][0:1]
                # print("temp number1: ",temp_number1)
                # extract 2nd number
                temp_number2 = number_adjusted[index][1:2]
                # print("temp number2: ",temp_number2)
                # remove current double digit value
                number_adjusted.pop(index)
                # insert in the following order as the queue moves rigth
                number_adjusted.insert(index, temp_number2)
                number_adjusted.insert(index, temp_number1)

        # print("Original number: ",list(self.card_number))
        # print("Final adjusted credit card number: ",number_adjusted)

        totalSum = 0
        for item in number_adjusted:
            totalSum += int(item)

        print("Total Sum:",totalSum)
        print("Modulo % 10 is: ", totalSum % 10)

        if totalSum % 10 == 0:
            self.valid = True
        else:
            self.valid = False
            self.card_type = "INVALID"
            print("Card failed mod10 test")


#do not modify assert statements

cc = CreditCard('5515460934365316')
assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('4440')
assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')
assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')
assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')
assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')
assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')
assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')
assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"