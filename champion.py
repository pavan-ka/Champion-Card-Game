import random
import time
# Labeling the suits, cards, and values

suits = ['Hearts','Diamonds','Spades','Clubs']
cards = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
deck = []

#creating the deck
for suit in suits:
    count = 0
    while count <= 12:
        deck.append([suit,cards[count],values[count]])
        count = count + 1
        
#splitting into 2 decks
random.shuffle(deck)
deck1 = deck[0:26]
deck2 = deck[26:52]

# creating the countdown timer
def countdown(sec):
    while sec > 0:
        print(sec)
        sec = sec - 1
        time.sleep(1)
    print("Let the game begin!")

# game

print("Welcome to champion! The rules are simple. Higher card wins")
print("If the card is the same, sum of values of next 3 cards determines who wins. Else it's a coin flip")
countdown(3)

rtracker = 1

while len(deck1) > 0 and len(deck2) > 0:
    firstcard = deck1.pop(0)
    secondcard = deck2.pop(0)
    print("The first card is ", firstcard[1], " of ", firstcard[0])
    print("The second card is ", secondcard[1], " of ", secondcard[0])
    if firstcard[2] > secondcard[2]:
        print("Deck 1 gets both cards!")
        deck1.append(firstcard)
        deck1.append(secondcard)
    elif firstcard[2] < secondcard[2]:
        print("Deck 2 gets both cards!")
        deck2.append(secondcard)
        deck2.append(firstcard)
    else:
        
        if len(deck1) == 0 or len(deck2) == 0:
            print("Next card")
            deck1.append(firstcard)
            deck2.append(secondcard)
        else:
            d1t1 = deck1.pop(0)
            d2t1 = deck1.pop(1)
        
            print("The tiebreaker card for Deck 1 is ", d1t1[1], " of ", d1t1[0])
            print("The tiebraker card for Deck 2 is ", d2t1[1], " of ", d2t1[0])
        
            sum1 = firstcard[2] + d1t1[2]
            sum2 = secondcard[2] + d2t1[2]
        
            print("The sum of the both cards for Deck 1 is ", sum1)
            print("The sum of the both cards for Deck 2 is ", sum2)
            if sum1 > sum2:
                print("Deck 1 gets the four cards")
                deck1.append(firstcard)
                deck1.append(secondcard)
                deck1.append(d1t1)
                deck1.append(d2t1)
            elif sum1 < sum2:
                print("Deck 2 gets the four cards")
                deck2.append(firstcard)
                deck2.append(secondcard)
                deck2.append(d1t1)
                deck2.append(d2t1)
            else:
                number = random.randint(0,2)
                if number == 0:
                    print("The coin flips in Deck 1's favor!")
                    deck1.append(firstcard)
                    deck1.append(secondcard)
                    deck1.append(d1t1)
                    deck1.append(d2t1)
                else:
                    print("The coin flips in Deck 2's favor!")
                    deck2.append(firstcard)
                    deck2.append(secondcard)
                    deck2.append(d1t1)
                    deck2.append(d2t1)
    
    time.sleep(1)
    print("Deck 1 now has ", len(deck1), " cards and Deck 2 has ", len(deck2), " cards at round ", rtracker)
    rtracker = rtracker + 1
    time.sleep(1)

if len(deck1) == 0:
    print("Deck 2 has won the game!")
else:
    print("Deck 1 has one the game!")

print("Thanks for playing champion! Re-run the file to play again!")