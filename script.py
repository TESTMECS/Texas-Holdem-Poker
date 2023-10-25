from cards import deck
from players import Player
import random
class Game(object):
    def init(self, pot, cards):
        self.pot = pot
        self.cards = []

print("Welcome to Texas Holdem Poker!")
print("The game is played with a standard deck of 52 cards.")
print("Each player is dealt two cards, face down.")
print("Five cards are dealt face up on the table.")
print("The player with the best hand wins.")
print("Enter your name")
name = input("Press enter to continue...")
print("How many chips would you like to start with?")
chips = int(input("Press enter to continue..."))

print("Ready to play? Y/n")
start = input("Press enter to continue...")
if start == "Y" or start == "y":
    print("Let's play!")

    Game = Game()
    Game.pot = 0
    Game.cards = []
    player = Player(name, chips, "human")
    computer = Player("Computer", chips, "computer")
    game_deck = deck
    game_deck.shuffle()
    player.cards.append(game_deck.pop())
    player.cards.append(game_deck.pop())
    computer.cards.append(game_deck.pop())
    computer.cards.append(game_deck.pop())
    print("Your cards are:")
    for card in player.cards:
        print(card)
    print("Choose your action:")
    options = ["Fold", "Check", "Bet"]
    for i in range(len(options)):
        print(str(i) + ": " + options[i])
    action = int(input("Press enter to continue..."))
    if action == 0:
        player.fold = True
    elif action == 1:
        print("You checked.")
    elif action == 2:
        print("How much would you like to bet?")
        bet = int(input("Press enter to continue..."))
        player.chips -= bet
        Game.pot += bet
        print("You bet " + str(bet) + " chips.")
    if player.fold != True:
        print("computer's turn")
        random_action = random.randint(1, 2)
        if random_action == 1:
            print("Computer checked.")
        elif random_action == 2:
            random_bet = random.randint(1, 150)
            print("Computer bet " + str(random_bet) + " chips.")
            computer.chips -= random_bet
            Game.pot += random_bet
    print("The pot is now " + str(Game.pot) + " chips.")

    if player.fold != True:
        print("The flop is:")
        for i in range(3):
            Game.cards.append(game_deck.pop())
        for card in Game.cards:
            print(card)

        print("Choose your action:")
        for i in range(len(options)):
            print(str(i) + ": " + options[i])
        action = int(input("Press enter to continue..."))
        if action == 0:
            player.fold = True
        elif action == 1:
            print("You checked.")
        elif action == 2:
            print("How much would you like to bet?")
            bet = int(input("Press enter to continue..."))
            player.chips -= bet
            Game.pot += bet
            print("You bet " + str(bet) + " chips.")
        if player.fold != True:
            print("computer's turn")
            random_action = random.randint(1, 2)
            if random_action == 1:
                print("Computer checked.")
            elif random_action == 2:
                random_bet = random.randint(1, 150)
                print("Computer bet " + str(random_bet) + " chips.")
                computer.chips -= random_bet
                Game.pot += random_bet
        print("The pot is now " + str(Game.pot) + " chips.")

    if player.fold != True:
        print("The turn is:")
        Game.cards.append(game_deck.pop())
        for card in Game.cards:
            print(card)

        print("Choose your action:")
        for i in range(len(options)):
            print(str(i) + ": " + options[i])
        action = int(input("Press enter to continue..."))
        if action == 0:
            player.fold = True
        elif action == 1:
            print("You checked.")
        elif action == 2:
            print("How much would you like to bet?")
            bet = int(input("Press enter to continue..."))
            player.chips -= bet
            Game.pot += bet
            print("You bet " + str(bet) + " chips.")
        if player.fold != True:
            print("computer's turn")
            random_action = random.randint(1, 2)
            if random_action == 1:
                print("Computer checked.")
            elif random_action == 2:
                random_bet = random.randint(1, 150)
                print("Computer bet " + str(random_bet) + " chips.")
                computer.chips -= random_bet
                Game.pot += random_bet
        print("The pot is now " + str(Game.pot) + " chips.")
    
    if player.fold != True:
        print("The river is:")
        Game.cards.append(game_deck.pop())
        for card in Game.cards:
            print(card)
        
        print("Choose your action:")
        for i in range(len(options)):
            print(str(i) + ": " + options[i])
        action = int(input("Press enter to continue..."))
        if action == 0:
            player.fold = True
        elif action == 1:
            print("You checked.")
        elif action == 2:
            print("How much would you like to bet?")
            bet = int(input("Press enter to continue..."))
            player.chips -= bet
            Game.pot += bet
            print("You bet " + str(bet) + " chips.")
        if player.fold != True:
            print("computer's turn")
            random_action = random.randint(1, 2)
            if random_action == 1:
                print("Computer checked.")
            elif random_action == 2:
                random_bet = random.randint(1, 150)
                print("Computer bet " + str(random_bet) + " chips.")
                computer.chips -= random_bet
                Game.pot += random_bet
        print("The pot is now " + str(Game.pot) + " chips.")
    
    if player.fold != True:
        print("The showdown is:")
        for card in Game.cards:
            print(card)
        print("Your cards are:")
        for card in player.cards:
            print(card)
        print("Computer's cards are:")
        for card in computer.cards:
            print(card)
    
    print("Did you win? Y/n")
    win = input("Press enter to continue...")
    if win == "Y" or win == "y":
        print("You won " + str(Game.pot) + " chips!")
        player.chips += Game.pot


        

    

    

