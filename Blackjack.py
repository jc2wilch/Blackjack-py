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

    dealer.hand1 = [0,0]
    player.hand1 = [0,0]



    choice = ""
    dealer.hand1[0] = cards.drawCard()
    dealer.hand1[1] = cards.drawCard()
    player.hand1[0] = cards.drawCard()
    player.hand1[1] = cards.drawCard()
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
            if len(player.hand2) == 0:
                print("You have " + str(player.total))
            else:
                print("You have " + str(player.total) + " in hand 1 and " + str(player.total2) + " in hand 2")
        else:
            if len(player.hand2) == 0:
                print("You have " + str(player.total) + " (Soft " + str(player.softTotal) + ")")
            else:
                print("You have " + str(player.total) + " (Soft " + str(player.softTotal) + ") in hand 1 and " + str(player.total2) + " (Soft " + str(player.softTotal2) + ") in hand 2")


    def playAgain():
        playChoice = input("\nWould you like to play again? ")
        if str.lower(playChoice) == "yes":
            return True
        elif str.lower(playChoice) == "no":
            return False
        else:
            print("Please type yes or no.")
            return playAgain()


    def stand(split, hand1, hand2): # boolean values for each; split is for if the deck's been split, hand 1 and 2 determine which hands the player is standing on
        option = 0 # loop flag / a way to display the dealer outcome messages if they havent already been displayed
        newDealerCard = 0

        def outcome(hand):
            playerTotal = player.total
            playerSoftTotal = player.softTotal

            if hand == 1:
                ordinalNum = "first"
            elif hand == 2:
                ordinalNum = "second"
                playerTotal = player.total2
                playerSoftTotal = player.softTotal2

            if (dealer.total == 21 or dealer.softTotal == 21) and playerTotal != 21:
                if hand == 0:
                    print("You lose")
                else:
                    print("Your " + ordinalNum + " hand lost")
                player.moneyCalc("lose", hand)

            elif dealer.total == playerTotal or ((dealer.softTotal == playerTotal or dealer.total == playerSoftTotal or dealer.softTotal == playerSoftTotal) and (playerSoftTotal != 0 and dealer.softTotal != 0)):
                if hand == 0:
                    print("Push")
                else:
                    print("Push with your " + ordinalNum + " hand")

            elif (dealer.softTotal == 0 and (dealer.total < playerTotal or dealer.total < playerSoftTotal)) or (dealer.softTotal > 0 and (dealer.softTotal < playerTotal or dealer.softTotal < playerSoftTotal)):
                if hand == 0:
                    print("You win!")
                else:
                    print("You won your " + ordinalNum + " hand")
                player.moneyCalc("win", hand)

            elif dealer.total > 21:
                if hand == 0:
                    print("Dealer busted, you win!")
                else:
                    print("Your " + ordinalNum + " hand won! Dealer busted!")
                player.moneyCalc("win", hand)

            elif (playerSoftTotal <= 0 and (dealer.total > playerTotal or dealer.softTotal > playerTotal)) or (playerSoftTotal > 0 and (dealer.total > playerSoftTotal or dealer.softTotal > playerSoftTotal)):
                if hand == 0:
                    print("You lose!")
                else:
                    print("Your " + ordinalNum + " hand lost")
                
                player.moneyCalc("lose", hand)



        while dealer.total < 17 and dealer.softTotal < 17:
            if option == 0:
                print("")
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

        if option == 0 and dealer.total <= 21:
            dealerOutcome()

        if split:
            if hand1:
                outcome(1)
            if hand2:
                outcome(2)
        else:
            outcome(0)


    player.hand1[0] = 1
    player.hand1[1] = 1


    if (player.hand1[0] == 1 and player.hand1[1] == 10) or (player.hand1[0] == 10 and player.hand1[1] == 1):
        player.total = 21
    else:
        player.total = player.hand1[0] + player.hand1[1]

    if (dealer.hand1[0] == 1 and dealer.hand1[1] == 10) or (dealer.hand1[0] == 10 and dealer.hand1[1] == 1):
        dealer.total = 21
    else:
        dealer.total = dealer.hand1[0] + dealer.hand1[1]


    while player.bet > player.money:
        bet = ""
        while not bet.isdigit():
            if bet != "":
                print("Please enter a whole number")
            bet = input("You have " + str(player.money) + " dollars, how much will you bet: ")
        player.bet = int(bet)
        if player.bet > player.money:
            print("You're too broke!")

    print("Dealer got: " + str(dealer.hand1[0]))

    if player.hand1[0] == 1 and player.hand1[1] < 10:
        player.softTotal = 11 + player.hand1[1]
    elif player.hand1[1] == 1 and player.hand1[0] != 1 and player.hand1[0] < 10:
        player.softTotal = 11 + player.hand1[0]

    if dealer.hand1[0] == 1 and dealer.hand1[1] < 10:
        dealer.softTotal = 11 + dealer.hand1[1]
    elif dealer.hand1[1] == 1 and dealer.hand1[0] != 1 and dealer.hand1[0] < 10:
        dealer.softTotal = 11 + dealer.hand1[0]

    if player.softTotal != 0:
        print("You got: " + str(player.hand1[0]) + " and " + str(player.hand1[1]) +" (Soft " + str(player.softTotal) + ")")
    else:
        print("You got: " + str(player.hand1[0]) + " and " + str(player.hand1[1]))

    # Blackjack
    if player.total == 21 and dealer.total != 21:
        print("You win!")
        player.moneyCalc("bj", 1)
        playChoice = playAgain()
        start(playChoice)
        return
    elif player.total == 21 and dealer.total == 21:
        print("Push")
        playChoice = playAgain()
        start(playChoice)
        return
    elif dealer.total == 21 and player.total != 21:
        print("Dealer got blackjack, you lose")
        player.moneyCalc("lose", 1)
        playChoice = playAgain()
        start(playChoice)
        return
    else:
        if player.hand1[0] == player.hand1[1]:
            while  choice != "dd" and choice != "hit" and choice != "stand" and choice != "split":
                choice = str.lower(input("Would you like to stand, hit, split, or double down(dd)? "))
                if choice == "split":
                    if (player.bet * 2) > player.money:
                        print("You don't have enough money to split!")
                        choice = ""
        else:
            while choice != "dd" and choice != "hit" and choice != "stand":
                choice = str.lower(input("Would you like to stand, hit, or double down(dd)? "))


    # Double Down
    if choice == "dd":
        if (player.bet * 2) > player.money:
            print("You're too broke")
            while choice != "hit" and choice != "stand":
                choice = str.lower(input("Would you like to stand or hit? "))
        else:
            player.bet *= 2

    # Hitting
    if choice == "hit" or choice == "dd":
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

            if (player.total == 21 or player.softTotal == 21) and dealer.total != 21 and dealer.softTotal != 21:
                choice = "stand"
            elif player.total > 21:
                print("You busted!")
                player.moneyCalc("lose", 1)
                playChoice = playAgain()
                start(playChoice)
                return
            elif player.total < 21:
                if str.lower(choice) == "dd":
                    choice = "stand" 
                else:
                    choice = str.lower(input("Do you want to hit or stand? "))


    def splitStuff(hand):
        #placeholder name
        if hand == 1:
            ordinalNum = "first"
            playerHand = player.hand1
            playerTotal = int(player.total / 2)
            if player.hand1[0] == 1:
                playerSoftTotal = 11
        else:
            ordinalNum = "second"
            playerHand = player.hand2
            playerTotal = player.hand2[0]
            if player.hand2[0] == 1:
                playerSoftTotal = 11

        print("In your " + ordinalNum + " hand you have a " + str(playerHand[0]))
        choice = ""
        while choice != "dd" and choice != "hit" and choice != "stand":
            choice = str.lower(input("Would you like to stand, hit, or double down(dd) on your " + ordinalNum + " hand? "))
        if choice == "dd":
            if hand == 1:
                if (player.bet * 3) > player.money: # for the total amount from split(2 times) and the additional double down (1.5 times).
                    print("You're too broke")
                    while choice != "hit" and choice != "stand":
                        choice = str.lower(input("Would you like to stand or hit? "))
                else:
                    player.bet *= 2

            else:
                if ((player.bet2 * 2) + player.bet) > player.money: # double down bet (2 times) + the bet from hand 1
                    print("You're too broke")
                    while choice != "hit" and choice != "stand":
                        choice = str.lower(input("Would you like to stand or hit? "))
                else:
                    player.bet2 *= 2
        if choice == "hit" or choice == "dd":
            while playerTotal < 21 and (choice == "hit" or choice == "dd"):
                newPlayerCard = cards.drawCard()
                playerTotal += newPlayerCard

                if playerSoftTotal > 0:
                    playerSoftTotal += newPlayerCard

                if newPlayerCard == 1 and ((playerTotal + 11) < 22 and (playerSoftTotal + 11) < 22) and playerSoftTotal == 0:
                    playerSoftTotal = playerTotal + 11

                if playerSoftTotal > 21:
                    playerSoftTotal = 0

                print("You got a " + str(newPlayerCard))
                if playerSoftTotal > 0:
                    print("You have " + str(playerTotal) + " (Soft " + str(playerSoftTotal) + ") in your " + ordinalNum + " hand")
                else:
                    print("You have " + str(playerTotal) + " in your " + ordinalNum + " hand")

                if hand == 1:
                    player.total = playerTotal
                    player.softTotal = playerSoftTotal
                elif hand == 2:
                    player.total2 = playerTotal
                    player.softTotal2 = playerSoftTotal


                if playerTotal == 21 or playerSoftTotal == 21 and dealer.total != 21 and dealer.softTotal != 21:
                    return "stand"
                elif playerTotal > 21:
                    print("You busted!")
                    player.moneyCalc("lose", hand)
                    return "lose"
                elif playerTotal < 21:
                    if str.lower(choice) == "dd" or player.hand1[0] == 1: # No hitting more than once when splitting aces cuz i cant be losing too much meaningless virtual money
                        return "stand" 
                    else:
                        choice = ""
                        while choice != "hit" and choice != "stand":
                            choice = str.lower(input("Do you want to hit or stand? "))
                        if choice == "stand":
                            return choice
                        



    if choice == "split":
        player.hand2.append(player.hand1[1])
        player.hand1.pop(1)

        player.bet2 = player.bet
        choice = splitStuff(1)

        if choice == "stand":
            choice = splitStuff(2)
            if choice == "stand":
                stand(True, True, True)
                playChoice = playAgain()
                start(playChoice)
                return
            else:
                stand(False, False, False)
                playChoice = playAgain()
                start(playChoice)
                return
        else:
            choice = splitStuff(2)
            if choice == "stand":
                stand(True, False, True)
                playChoice = playAgain()
                start(playChoice)
                return
            else:
                stand(False, False, False)
                playChoice = playAgain()
                start(playChoice)
                return


    # Standing
    if choice == "stand":
        stand(False, False, False)
        playChoice = playAgain()
        start(playChoice)
        return

    
start(True)
