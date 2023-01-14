import random
from BlackjackClasses import Player, Deck

print("Blackjack pays 3:2")
print("Dealer must stand on soft 17\n")

player = Player("player", 2000, 2001, [0,0], 0, 0)
dealer = Player("dealer", 0, 0, [0,0], 0, 0)
cards = Deck()


def start(again):
    if not again or player.money <= 0:
        if player.money <= 0:
            print("You can't play any more because you're broke!")
        return


    choice = ""
    dealer.cards[0] = cards.drawCard()
    dealer.cards[1] = cards.drawCard()
    player.cards[0] = cards.drawCard()
    player.cards[1] = cards.drawCard()
    player.softTotal = 0
    dealer.softTotal = 0
    player.bet = player.money + 1
    playAgain = ""

    

    def dealerOutcome():
        if dealer.softTotal == 0 or dealer.softTotal > 21:
            print("The dealer has " + str(dealer.total))
        else:
            print("The dealer has " + str(dealer.total) + " (Soft " + str(dealer.softTotal) + ")")
        if player.softTotal == 0 or player.softTotal > 21:
            print("You have " + str(player.total))
        else:
            print("You have " + str(player.total) + " (Soft " + str(player.softTotal) + ")")


    def playAgain():
        playChoice = input("\nWould you like to play again? ")
        if str.lower(playChoice) == "yes":
            return True
        elif str.lower(playChoice) == "no":
            return False
        else:
            print("Please type yes or no.")
            return playAgain()


    def stand():
        option = 0
        newDealerCard = 0

        while dealer.total < 17 and dealer.softTotal < 17:
            if option == 0:
                dealerOutcome()
            option = 1
            newDealerCard = cards.drawCard()
            dealer.total += newDealerCard
            if dealer.softTotal > 0:
                dealer.softTotal += newDealerCard

            if newDealerCard == 1 and ((dealer.total + 11) < 22 and (dealer.softTotal + 11) < 22) and dealer.softTotal == 0:
                dealer.softTotal = dealer.total + 11

            if dealer.softTotal > 21:
                dealer.softTotal = 0

            print("The dealer just drew a " + str(newDealerCard))
            dealerOutcome()
        if (dealer.total == 21 or dealer.softTotal == 21) and player.total != 21:
            if option == 0:
                dealerOutcome()
            print("You lose")
            player.moneyCalc("lose")
            playChoice = playAgain()
            start(playChoice)
        elif dealer.total == player.total or (dealer.softTotal == player.total or dealer.total == player.softTotal or dealer.softTotal == player.softTotal and player.softTotal != 0 and dealer.softTotal != 0):
            if option == 0:
                dealerOutcome()
            print("Push")
            playChoice = playAgain()
            start(playChoice)
        elif (dealer.softTotal == 0 and (dealer.total < player.total or dealer.total < player.softTotal)) or (dealer.softTotal > 0 and (dealer.softTotal < player.total or dealer.softTotal < player.softTotal)):
            if option == 0:
                dealerOutcome()
            print("You win!")
            player.moneyCalc("win")
            playChoice = playAgain()
            start(playChoice)
        elif dealer.total > 21:
            print("Dealer busted, you win!")
            player.moneyCalc("win")
            playChoice = playAgain()
            start(playChoice)
        elif (player.softTotal <= 0 and (dealer.total > player.total or dealer.softTotal > player.total)) or (player.softTotal > 0 and (dealer.total > player.softTotal or dealer.softTotal > player.softTotal)):
            if option == 0:
                dealerOutcome()
            print("You lose!")
            player.moneyCalc("lose")
            playChoice = playAgain()
            start(playChoice)


    if (player.cards[0] == 1 and player.cards[1] == 10) or (player.cards[0] == 10 and player.cards[1] == 1):
        player.total = 21
    else:
        player.total = player.cards[0] + player.cards[1]

    if (dealer.cards[0] == 1 and dealer.cards[1] == 10) or (dealer.cards[0] == 10 and dealer.cards[1] == 1):
        dealer.total = 21
    else:
        dealer.total = dealer.cards[0] + dealer.cards[1]


    while player.bet > player.money:
        bet = ""
        while not bet.isdigit():
            if bet != "":
                print("Please enter a whole number")
            bet = input("You have " + str(player.money) + " dollars, how much will you bet: ")
        player.bet = int(bet)
        if player.bet > player.money:
            print("You're too broke!")

    print("Dealer got: " + str(dealer.cards[0]))

    if player.cards[0] == 1 and player.cards[1] < 10:
        player.softTotal = 11 + player.cards[1]
    elif player.cards[1] == 1 and player.cards[0] != 1 and player.cards[0] < 10:
        player.softTotal = 11 + player.cards[0]

    if dealer.cards[0] == 1 and dealer.cards[1] < 10:
        dealer.softTotal = 11 + dealer.cards[1]
    elif dealer.cards[1] == 1 and dealer.cards[0] != 1 and dealer.cards[0] < 10:
        dealer.softTotal = 11 + dealer.cards[0]

    if player.softTotal != 0:
        print("You got: " + str(player.cards[0]) + " and " + str(player.cards[1]) +" (Soft " + str(player.softTotal) + ")")
    else:
        print("You got: " + str(player.cards[0]) + " and " + str(player.cards[1]))

    # Blackjack
    if player.total == 21 and dealer.total != 21:
        print("You win!")
        player.moneyCalc("bj")
        playChoice = playAgain()
        start(playChoice)
    elif player.total == 21 and dealer.total == 21:
        print("Push")
        playChoice = playAgain()
        start(playChoice)
    elif dealer.total == 21 and player.total != 21:
        print("Dealer got blackjack, you lose")
        player.moneyCalc("lose")
        playChoice = playAgain()
        start(playChoice)
    else:
        while choice != "dd" and choice != "hit" and choice != "stand":
            choice = str.lower(input("Would you like to stand, hit, or DD? "))


    # Double Down
    if choice == "dd":
        if (player.bet * 2) > player.money:
            print("You're too broke")
            while choice != "hit" and choice != "stand":
                choice = str.lower(input("Would you like to stand or hit? "))
        else:
            player.bet *= 2
            choice = "dd"

    # Hitting
    elif choice == "hit" or choice == "dd":
        while player.total < 21 and (choice == "hit" or choice == "dd"):
            newPlayerCard = cards.drawCard()
            player.total += newPlayerCard

            if player.softTotal > 0:
                player.softTotal += newPlayerCard

            if newPlayerCard == 1 and ((player.total + 11) < 22 and (player.softTotal + 11) < 22) and player.softTotal == 0:
                player.softTotal = player.total + 11

            if player.softTotal > 21:
                player.softTotal = 0

            print("You got a " + str(newPlayerCard))
            if player.softTotal > 0:
                print("You have " + str(player.total) + " (Soft " + str(player.softTotal) + ")")
            else:
                print("You have " + str(player.total))

            if player.total == 21 or player.softTotal == 21 and dealer.total != 21 and dealer.softTotal != 21:
                choice = "stand"
            elif player.total > 21:
                print("You busted!")
                player.moneyCalc("lose")
                playChoice = playAgain()
                start(playChoice)
            elif player.total < 21:
                if str.lower(choice) == "dd":
                    choice = "stand" 
                else:
                    choice = str.lower(input("Do you want to hit or stand? "))

    # Standing
    if choice == "stand":
        stand()

    
start(True)