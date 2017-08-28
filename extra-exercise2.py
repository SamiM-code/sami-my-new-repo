import random

shuffle_amount = 1000

def createDeck():

    #Set suits and allowed numbers
    suits = ["s","h","d","c"]
    numbers = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

    deck = []

    for suit in suits:
        for number in numbers:
            deck.append(suit+number) 
    return deck

def shuffle(deck):
    #Shuffle the deck for X times...
    for i in range(1,shuffle_amount,1):
        #Select which two positions to swap
        first = random.randint(0,51)
        second = random.randint(0,51)
        #print(first)
        #print(second)
        #Swap positions
        deck[first],deck[second] = deck[second],deck[first]
    return deck

new_deck = createDeck()
print("Created card deck is:")
print(new_deck)
#print("Length of card deck is: ",len(new_deck))
shuffled_new_deck = shuffle(new_deck)
print("")
print("Shuffled card deck is:")
print(shuffled_new_deck)
#print("Length of shuffled card deck is: ",len(shuffled_new_deck))

