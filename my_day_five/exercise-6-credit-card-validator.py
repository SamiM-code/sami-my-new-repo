
#Credit card vendors variables
Credit_Card_Vendors_Dict = {"VISA":[4],"MASTERCARD":[51,52,53,54,55],"AMEX":[34,37]}
#VISA = 4   -->16 numbers
#MASTERCARD = (51, 52, 53, 54, 55)  -->16 numbers
#AMEX = (34,37) -->15 numbers

class CreditCard:
    def __init__(self, card_number):
        self.card_number = str(card_number)
        self.card_type = ""
        self.valid = ""

        self.check_length()
        if self.valid != "False":
            self.determine_card_type()
        self.validate()


    def determine_card_type(self):
        #Set default value for card type
        self.card_type = "un-recognized"
        for vendor,value in Credit_Card_Vendors_Dict.items():
            #print("vendor",vendor,"value:",value)
            #print("card number is: ",self.card_number[0:2])
            if self.card_number[0:1] == "4":
                self.card_type = "VISA"
            elif int(self.card_number[0:2]) in value:
               self.card_type = vendor
        return self.card_type

    def check_length(self):
        if len(self.card_number) != "15" or len(self.card_number) != "16":

            self.valid = True
        else:
            self.valid = False

    def validate(self):
        number_adjusted = list(self.card_number)
        #print(number_adjusted)
        #even numbers from the back
        for index in range(len(number_adjusted)-2,-1,-2):
            print("starting point: ",index,"number",number_adjusted[index])
            #print("credit card number is: ",self.card_number)
            #print("BEFORE: index is",index,"number is: ",number_adjusted[index])
            number_adjusted[index] = str(int(number_adjusted[index]) * 2)
            #print("AFTER: index is", index, "number is: ", number_adjusted[index])
        #print("Doubled number_str is: ",number_adjusted)

        #for index in range(0,len(number_adjusted)-1,1):
        #    print("Checking > 10 numbers: ",index,"number is",number_adjusted[index])
        #    if int(number_adjusted[index]) > 9:
        #        print("Found number > 10 at index: ",index,"number is: ",number_adjusted[index])
        #        # extract 1st number
        #        temp_number1 = number_adjusted[index][0:1]
        #        #print("temp number1: ",temp_number1)
        #        #extract 2nd number
        #        temp_number2 = number_adjusted[index][1:2]
        #        #print("temp number2: ",temp_number2)
        #        # remove current double digit value
        #        number_adjusted.pop(index)
        #        # insert in the following order as the queue moves rigth
        #        number_adjusted.insert(index,temp_number2)
        #        number_adjusted.insert(index,temp_number1)

        for index, val in enumerate(number_adjusted):
            #print(index, val)
            if int(val) > 9:
                #print("Found number > 10 at index: ",index,"number is: ",number_adjusted[index])
                # extract 1st number
                temp_number1 = number_adjusted[index][0:1]
                #print("temp number1: ",temp_number1)
                #extract 2nd number
                temp_number2 = number_adjusted[index][1:2]
                #print("temp number2: ",temp_number2)
                # remove current double digit value
                number_adjusted.pop(index)
                # insert in the following order as the queue moves rigth
                number_adjusted.insert(index,temp_number2)
                number_adjusted.insert(index,temp_number1)

        #print("Original number: ",list(self.card_number))
        #print("Final adjusted credit card number: ",number_adjusted)

        totalSum = 0
        for item in number_adjusted:
            totalSum += int(item)

        print("total Sum",totalSum,"modulo: ",totalSum % 10)

        if totalSum % 10 == 0:
            self.valid = True
        else:
            self.valid = False

        print("card validity is: ",self.valid)

mycard = CreditCard(4388540047537575)
result = mycard.determine_card_type()
mycard.check_length()
print("Card type is: ",result)
mycard.validate()

#length -> algorithm -> credit card type
