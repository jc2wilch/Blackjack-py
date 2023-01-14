import random
import copy

class Player():
    def __init__(self, name, money, bet, hand1, total, softTotal):
        self.name = name
        self.money = money
        self.bet = bet
        self.bet2 = bet
        self.hand1 = hand1
        self.hand2 = []
        self.total = total
        self.total2 = 0
        self.softTotal = softTotal
        self.softTotal2 = 0



    def moneyCalc(self, outcome, hand):
        if str.lower(outcome) == "lose":
            if hand == 1 or hand == 0:
                self.money -= int(self.bet)
            else:
                self.money -= int(self.bet2)
        elif str.lower(outcome) == "win":
            if hand == 1 or hand == 0:
                self.money += int(self.bet)
            else:
                self.money += int(self.bet2)
        elif str.lower(outcome) == "bj": # blackjack
            self.bet *= 0.5
            self.money += int(self.bet)

class Deck():
    def __init__(self):
        self.origCards = [1,1,1,1,
                          2,2,2,2,
                          3,3,3,3,
                          4,4,4,4,
                          5,5,5,5,
                          6,6,6,6,
                          7,7,7,7,
                          8,8,8,8,
                          9,9,9,9,
                          10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        self.newCards = copy.copy(self.origCards)

    def drawCard(self):
        if len(self.newCards) == 0:
            self.newCards = copy.copy(self.origCards)
            print("\nThe deck has been shuffled\n")
            print(len(self.origCards))
            print(len(self.newCards))

        newCardIndex = random.randint(0, len(self.newCards) - 1)
        newCard = self.newCards[newCardIndex]
        self.newCards.pop(newCardIndex)
        return newCard