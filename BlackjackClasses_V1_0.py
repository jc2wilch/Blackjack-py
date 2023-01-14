import random

class Player():
    def __init__(self, name, money, bet, cards, total, softTotal):
        self.name = name
        self.money = money
        self.bet = bet
        self.cards = cards
        self.total = total
        self.softTotal = softTotal

    def moneyCalc(self, outcome):
        if str.lower(outcome) == "lose":
            self.money -= int(self.bet)
        elif str.lower(outcome) == "win":
            self.money += int(self.bet)
        elif str.lower(outcome) == "bj":
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
        self.newCards = self.origCards

    def drawCard(self):
        if len(self.newCards) == 0:
            self.newCard = self.origCards

        newCardIndex = random.randint(0, len(self.newCards) - 1)
        newCard = self.newCards[newCardIndex]
        self.newCards.pop(newCardIndex)
        return newCard