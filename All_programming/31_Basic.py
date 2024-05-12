# shuffle deck of cards
import itertools,random

#make deck of cards
cards = list(itertools.product(['spades','heart','diamond','club'],range(1,14)))

#shuffling the cards
random.shuffle(cards)

# sorting test
deck1 = []
# draw cards
for i in range(13):
    if cards[i][1] == 1:
        print('A','of',cards[i][0])
        card = "A of "+str(cards[i][0])
        deck1.append(card)
    elif cards[i][1] == 11:
        print('J','of',cards[i][0])
        card = "J of "+str(cards[i][0])
        deck1.append(card)
    elif cards[i][1] == 12:
        print('Q','of',cards[i][0])
        card = "Q of "+str(cards[i][0])
        deck1.append(card)
    elif cards[i][1] == 13:
        print('K','of',cards[i][0])
        card = "K of "+str(cards[i][0])
        deck1.append(card)
    else:
        print(cards[i][1],"of",cards[i][0])
        card = str(cards[i][1])+" of "+str(cards[i][0])
        deck1.append(card)
print()
sortDeck = sorted(deck1)
for items in sortDeck:
    print(items)


