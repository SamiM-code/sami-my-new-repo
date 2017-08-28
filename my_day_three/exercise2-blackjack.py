import random
import os
import time
import pdb
import sys

shuffle_amount = 1000

class Person:

    def __init__(self,input):
        self.name = input[0]
        self.money = int(input[1])
        self.decks = input[2]
        self.cards = []

class Deck:

    #Define how the deck is going to be printed with "list" method
    def __init__(self,how_many_decks_count):
        self.count = how_many_decks_count 
        self.deck = []
        
    def list(self):
        return self.deck

    def deleteall(self):
        #Remove all items from the deck
        for item in range(len(self.deck)):
            self.deck.pop()

    def draw(self):
        #take a card from the deck, and remove it
        return self.deck.pop()

    def create(self):
        #Set suits and allowed numbers
        suits = ["s","h","d","c"]
        numbers = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        
        #Create as many decks as the user requested
        for item in range(self.count):
            for suit in suits:
                for number in numbers:
                    self.deck.append(suit+number) 
        #return self.deck

    def shuffle(self):
        #Shuffle the deck for X times...
        for i in range(1,shuffle_amount,1):
            #Select which two positions to swap
            #Take cards after 52 as well if there are multiple decks...
            first = random.randint(0,len(self.deck)-1)
            second = random.randint(0,len(self.deck)-1)
            #Swap positions
            self.deck[first],self.deck[second] = self.deck[second],self.deck[first]
        #return self.deck


class Game:

    def __init__(self):
        #Get the amount of money user has
        #how many rounds game has been played
        self.rounds = 0
        self.bet = 0
                        
    def clear(self):          
        #Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')        

    def sumofhand(self,cards):
        self.givencards = cards
        self.sum = 0
        for card in self.givencards:
            if card[1:] == "J" or card[1:] == "Q" or card[1:] == "K":
                self.sum += 10
            elif card[1:] == "A" and self.sum <12:
                self.sum += 11
            elif card[1:] == "A" and self.sum >11:
                self.sum += 1
            else:
                self.sum += int(card[1:])               
        return self.sum
    
    def newround(self):
        #Empty player's and house's cards
        player.cards[:] = [] 
        house.cards[:] = []  
        mydeck.deleteall()
        mydeck.create()
        mydeck.shuffle()
        
        #Main game loop
        quit = "no"

        #Draw initial cards for the house and player    
        player.cards.append(mydeck.draw())
        player.cards.append(mydeck.draw())
        house.cards.append(mydeck.draw())
 
        
    def show_status(self):
        #Clear screen
        os.system('cls' if os.name == 'nt' else 'clear') 
        topbar = ""
        winlose_text = ""
        bottombar = ""
        game_status = "null"
        
        if (mygame.sumofhand(player.cards) == 21 and mygame.sumofhand(house.cards) != 21) or (mygame.sumofhand(player.cards) > mygame.sumofhand(house.cards) and mygame.sumofhand(house.cards) > 16 and mygame.sumofhand(player.cards) < 22) or mygame.sumofhand(house.cards) >21:
            topbar = "============================================================="
            winlose_text = "              YOU WIN! "
            bottombar = "=============================================================" 
            player.money += int(mygame.bet)
            house.money -= int(mygame.bet)
            game_status = "winner"
        elif mygame.sumofhand(player.cards) > 21 or ((mygame.sumofhand(player.cards) <= mygame.sumofhand(house.cards)) and mygame.sumofhand(house.cards) >16):
            topbar = "============================================================="
            winlose_text = "              YOU LOST! "
            bottombar = "=============================================================" 
            game_status = "loser"
            player.money -= int(mygame.bet)
            house.money += int(mygame.bet)
            if player.money <= 0:
                print("You have run out of money!")
                print("Better luck next time")
                exitgame()
            if house.money <= 0:
                print("The House has run out of money, and if filing a bankcrypcy!")
                print("Well played! Congratulations!")
                exitgame()

        else:
            #do nothing
            game_status = "on-going"
            
        print("=============================================================")
        print("                   BLACKJACK GAME                            ")
        print("=============================================================")
        print("")
        print("Player: {:<10} Cards: {:<10} Money: {:<10}".format(player.name,str(player.cards),player.money))
        print("")
        print("               Sum of Hand: ",mygame.sumofhand(player.cards))
        if game_status != "on-going":
            print("{}".format(topbar))
            print("{}".format(winlose_text))
            print("{}".format(bottombar))
        print("")
        print("") 
        print("")
        print("House:  {:<10} Cards: {:<10} Money: {:<10}".format(house.name,str(house.cards),house.money))
        print("")
        print("               Sum of Hand: ",mygame.sumofhand(house.cards))
        print("") 
        print("")
        print("               Bet:         ",mygame.bet)
        print("") 
        print("")
        print("You have done {} actions in total".format(self.rounds))
        
        return game_status
        
    def actions(self):
        self.rounds += 1
        print("")
        print("")
        print("Please select one from the following options: ")
        print("")
        print("    1. add card")
        print("    2. hold")
        print("    3. quit")
        print("")
        user_input_option = input("What is your selection: ")
        while user_input_option.isdecimal() != True:
            print("Please give me a number!")
            user_input_option = input("My selection: ")
        return int(user_input_option)
    
    
    def add(self):
        player.cards.append(mydeck.draw())
     
        
    def hold(self):
        while mygame.sumofhand(house.cards) <= 17:
            house.cards.append(mydeck.draw())

def exitgame():
    print("")
    print("")
    print("==============================")
    print("Thank you for playing the game!")
    print("Exiting...")
    print("==============================")
    sys.exit(0)


def start_game():

    os.system('cls' if os.name == 'nt' else 'clear')  
    print("=============================================================")
    print("                   BLACKJACK GAME                            ")
    print("=============================================================")
    print("")
    name = input("What is your name: ")
    user_input_money = input("Please give me the amount of money you have for play: ")
    while user_input_money.isdecimal() == False:
        print("")
        print("Please give me a number only!")
        user_input_money = input("My money: ")
              
    user_input_decks = input("Give me amount of card decks: ")
    while user_input_decks.isdecimal() == False:
        print("")
        print("Please give me a number only!")
        user_input_decks = input("Count of decks: ")
    return name,user_input_money,user_input_decks

              

if __name__ == "__main__":

    #pdb.set_trace()

    #Start the game, create person object
    player = Person(start_game())
    
    #Create house person object with some money
    house = Person(("House",1000,1))

    #Init mydeck, with the amount of decks user gave
    mydeck = Deck(int(player.decks))    

    #Create deck
    mydeck.create()
    
    #Shuffle deck
    mydeck.shuffle()

    #Main game loop
    quit = "no"
    
    #Draw initial cards for the house and player    
    player.cards.append(mydeck.draw())
    player.cards.append(mydeck.draw())
    house.cards.append(mydeck.draw())

    mygame = Game()
    mygame.bet = input("Please give initial bet (up to {} dollars): ".format(player.money))
    while mygame.bet.isdecimal() == False or (int(mygame.bet) > player.money):
        print("")
        print("Please give me a number only, up to {} dollars: ".format(player.money))
        mygame.bet = input("Bet: ")

    while quit != "yes":
        game_result = mygame.show_status()  
        if game_result == "winner" or game_result == "loser":
            user_input_answer = input("Would you like to have a new game (Y/N)?: ")
            while user_input_answer != "N" and user_input_answer != "n" and user_input_answer != "Y" and user_input_answer != "y" and user_input_answer !="":
                user_input_answer = input("New game (Y/N)?: ")     
            if user_input_answer == "N" or user_input_answer == "n":
                quit = "yes"
                continue
            else:
                #init cards again
                mygame.newround()
                quit = "no"
                continue 
        
        result = mygame.actions()  
        if result == 1:
            mygame.add()
        if result == 2:
            mygame.hold()
        if result == 3:
            quit = "yes"
            exitgame()
            
    
    










