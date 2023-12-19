from cards import deck, StandardDeck
from button import Button
from players import Player
from Poker import Poker
from pygame_textinput import TextInputVisualizer
from pygame_textinput import TextInputManager
import pygame_textinput
import random

import pygame
import tkinter as tk
import sys

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Texas Holdem")

clock = pygame.time.Clock()


#colors
red   = (255,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
white =(255,255,255)

#############################################
#Display card on flop or for players
def display_card(card):

  card_images = {
    "Two of Diamonds": "assets/cards/2ofdiamonds.png",
    "Three of Diamonds": "assets/cards/3ofdiamonds.png",
    "Four of Diamonds": "assets/cards/4ofdiamonds.png",
    "Five of Diamonds": "assets/cards/5ofdiamonds.png",
    "Six of Diamonds": "assets/cards/6ofdiamonds.png",
    "Seven of Diamonds": "assets/cards/7ofdiamonds.png",
    "Eight of Diamonds": "assets/cards/8ofdiamonds.png",
    "Nine of Diamonds": "assets/cards/9ofdiamonds.png",
    "Ten of Diamonds": "assets/cards/10ofdiamonds.png",
    "Jack of Diamonds": "assets/cards/jackofdiamonds.png",
    "Queen of Diamonds": "assets/cards/queenofdiamonds.png",
    "King of Diamonds": "assets/cards/kingofdiamonds.png",
    "Ace of Diamonds": "assets/cards/aceofdiamonds.png",
    "Two of Clubs": "assets/cards/2ofclubs.png",
    "Three of Clubs": "assets/cards/3ofclubs.png",
    "Four of Clubs": "assets/cards/4ofclubs.png",
    "Five of Clubs": "assets/cards/5ofclubs.png",
    "Six of Clubs": "assets/cards/6ofclubs.png",
    "Seven of Clubs": "assets/cards/7ofclubs.png",
    "Eight of Clubs": "assets/cards/8ofclubs.png",
    "Nine of Clubs": "assets/cards/9ofclubs.png",
    "Ten of Clubs": "assets/cards/10ofclubs.png",
    "Jack of Clubs": "assets/cards/jackofclubs.png",
    "Queen of Clubs": "assets/cards/queenofclubs.png",
    "King of Clubs": "assets/cards/kingofclubs.png",
    "Ace of Clubs": "assets/cards/aceofclubs.png",
    "Two of Hearts": "assets/cards/2ofhearts.png",
    "Three of Hearts": "assets/cards/3ofhearts.png",
    "Four of Hearts": "assets/cards/4ofhearts.png",
    "Five of Hearts": "assets/cards/5ofhearts.png",
    "Six of Hearts": "assets/cards/6ofhearts.png",
    "Seven of Hearts": "assets/cards/7ofhearts.png",
    "Eight of Hearts": "assets/cards/8ofhearts.png",
    "Nine of Hearts": "assets/cards/9ofhearts.png",
    "Ten of Hearts": "assets/cards/10ofhearts.png",
    "Jack of Hearts": "assets/cards/jackofhearts.png",
    "Queen of Hearts": "assets/cards/queenofhearts.png",
    "King of Hearts": "assets/cards/kingofhearts.png",
    "Ace of Hearts": "assets/cards/aceofhearts.png",
    "Two of Spades": "assets/cards/2ofspades.png",
    "Three of Spades": "assets/cards/3ofspades.png",
    "Four of Spades": "assets/cards/4ofspades.png",
    "Five of Spades": "assets/cards/5ofspades.png",
    "Six of Spades": "assets/cards/6ofspades.png",
    "Seven of Spades": "assets/cards/7ofspades.png",
    "Eight of Spades": "assets/cards/8ofspades.png",
    "Nine of Spades": "assets/cards/9ofspades.png",
    "Ten of Spades": "assets/cards/10ofspades.png",
    "Jack of Spades": "assets/cards/jackofspades.png",
    "Queen of Spades": "assets/cards/queenofspades.png",
    "King of Spades": "assets/cards/kingofspades.png",
    "Ace of Spades": "assets/cards/aceofspades.png",
    
  }
  
  card_image = pygame.image.load(card_images.get(card,"assets/cards/2ofdiamonds.png")).convert_alpha()
  
  return card_image

def draw_bg(bg_image):
  scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))


def starting_screen(name_text_list):
  
  #background image
  bg_image = pygame.image.load("assets/img/42427683-081c-4ae3-b7d7-75acbfbbd19b.jfif").convert_alpha()

  #text settings
  font_obj = pygame.font.Font('freesansbold.ttf', 32)
  text_surface_obj = font_obj.render('Welcome to Texas Holdem Poker v1a', True, green, blue)
  text_rect_obj = text_surface_obj.get_rect()
  text_rect_obj.center = (300, 150)

  name_text_surface_obj = font_obj.render('Enter name, then press enter, then press play to continue', True, green, blue)
  name_rect_obj = name_text_surface_obj.get_rect()
  name_rect_obj.center = (500, 200)


  button_rect = pygame.Rect(220, 700, 140, 50)
  textinput = TextInputVisualizer()
  font = pygame.font.SysFont("Consolas", 55)
  manager = TextInputManager(validator = lambda input: len(input) <= 8)
  textinput_custom = TextInputVisualizer(manager=manager, font_object=font)
  textinput_custom.cursor_width = 4
  textinput_custom.cursor_blink_interval = 400 # blinking interval in ms
  textinput_custom.antialias = False
  textinput_custom.font_color = (0, 85, 170)

  pygame.key.set_repeat(200, 25)
  
  run = True
  while run:

    
    screen.fill("black")

    #Starting screen
    draw_bg(bg_image)

    #drawing text
    screen.blit(text_surface_obj, text_rect_obj)
    screen.blit(name_text_surface_obj, name_rect_obj)


    
    PLAY_BUTTON = Button(image=None, pos=(220, 700), text_input="PLAY", font=font_obj, base_color="#d7fcd4", hovering_color="White", press=False)
    PLAY_BUTTON.update(screen)

    events = pygame.event.get()

    #name box
    textinput.update(events)
    textinput_custom.update(events)
    # Get its surface to blit onto the screen
    screen.blit(textinput_custom.surface, (220, 300))

    #event handler
    for event in events:
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            print(f"User pressed enter! Input so far: {textinput.value}")
            name_text_list.append(textinput.value)
      if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
          PLAY_BUTTON.press = True
      if PLAY_BUTTON.press:
        run = False
    #update display
    
    pygame.display.update()
    
    clock.tick(60)
def raise_handler(chips, pot):
    # draw the buttons for 1/4 1/2 3/4 and all in
    # allow the user to click on them and then return how much they bet. 
    font_obj = pygame.font.Font('freesansbold.ttf', 16)
    QUART_BUTTON = Button(image=None, pos=(220, 700), text_input="Raise 1/4", font=font_obj, base_color="#d7fcd4", hovering_color="White", press=False)
    QUART_BUTTON.update(screen)
    HALF_BUTTON = Button(image=None, pos=(500, 700), text_input="Raise 1/2", font=font_obj, base_color="#d7fcd4", hovering_color="Blue", press=False)
    HALF_BUTTON.update(screen)
    THIRD_BUTTON = Button(image=None, pos=(700, 700), text_input="Raise 3/4", font=font_obj, base_color="#d7fcd4", hovering_color="Blue", press=False)
    THIRD_BUTTON.update(screen)
    ALLIN_BUTTON = Button(image=None, pos=(900, 700), text_input="ALLIN", font=font_obj, base_color="#d7fcd4", hovering_color="Blue", press=False)
    ALLIN_BUTTON.update(screen)
    pygame.display.flip()
    
    while True:
      events = pygame.event.get()
      for event in events:
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if QUART_BUTTON.checkForInput(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
              if chips > int(pot // 4):
                return int(pot // 4)
              else:
                  continue
          if HALF_BUTTON.checkForInput(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
              if chips > int(pot // 2):
                return int(pot // 2)
              else:
                  continue
          if THIRD_BUTTON.checkForInput(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
              if chips > int(pot // (4/3)):
                return int(pot // (4/3))
              else:
                 continue
          if ALLIN_BUTTON.checkForInput(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
              if chips > 0:
                return int(chips)
              else: 
                continue
          if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
              return 0      
  
def show_controls():
  font_obj = pygame.font.Font('freesansbold.ttf', 24)
  text_surface_obj = font_obj.render("Controls: Press r to Raise | Press f to fold | Press c to check", True, green, blue)
  text_rect_obj = text_surface_obj.get_rect()
  text_rect_obj.center = (500, 600)
  screen.blit(text_surface_obj, text_rect_obj)
       
def showdown(Player1, Player2, Player3, Dealer):
  game = Poker(Player1, Player2, Player3, Dealer)
  #Player1 Cards
  for i in Dealer.cards:
      #give players all 7 cards
      Player1.cards.append(i)
      Player2.cards.append(i)
      Player3.cards.append(i)
  player_score = game.get_score(Player1.cards)
  computer_score = game.get_score(Player2.cards)
  if player_score > computer_score:
     Player1.win = True
  else:
     Player1.win = False

def update_pot(dealer, turn):
  font_obj = pygame.font.Font('freesansbold.ttf', 32)
  pot_text = font_obj.render(f"Pot: {dealer.chips}", True, (255, 255, 255))
  dealer.attribute = pot_text
  x = 0
  if turn == 0:
    screen.blit(dealer.attribute, (10, 10+x))
    pygame.display.flip()
  else:
    for i in range(turn+1):
      x = i * 100
    screen.blit(dealer.attribute, (10, 10+x))
    pygame.display.flip()

  
def game_screen(Player1, Player2, Player3, Dealerr):
   screen.fill("black")
   bg_image = pygame.image.load('assets/img/img_gen_597979_xNOYkB.png').convert_alpha()
   draw_bg(bg_image)
   font_obj = pygame.font.Font('freesansbold.ttf', 32)
   hand = True

   option = False
   #show controls
   show_controls()

   #setup players
   screen.blit(font_obj.render(Player1.name, True, green, blue), (400, 0))
   while hand:
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      #blinds put in the call 
      for player in [Player1, Player2, Player3]:
        if player.attribute == "SB":
          player.chips -= 1
        if player.attribute == "BB":
          player.chips -= 2
      Dealerr.chips += 3      
      #deal cards
      deck.shuffle()
      
      deck.deal(Player1)
      deck.deal(Player1)
      deck.burn()

      deck.deal(Player2)
      deck.deal(Player2)
      deck.burn()

      deck.deal(Player3)
      deck.deal(Player3)
      #display two cards for the players
      print(Player1.cards[0])
      print(Player1.cards[1])
      card1 = display_card(Player1.cards[0].get_card_name())
      card2 = display_card(Player1.cards[1].get_card_name())
      screen.blit(card1, (300, 100))
      screen.blit(card2, (400, 100))
      #display pot
      update_pot(Dealerr, 0)
      pygame.display.flip()
      #PREFLOP
      option = True
      while option:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                #Raise
                print("Raise")
                amt = raise_handler(Player1.chips, Dealerr.chips)
                print("You Raised", amt)
                Dealerr.chips += amt
                Player1.chips -= amt
                option = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                #Fold
                Player1.fold = True
                option = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                #Check
                print("Check")
                option = False
      #COMPUTER OPTION
      computer_act = random.randint(1, 2)
      if computer_act == 1:
         #check
          print("Computer checked")
      if computer_act == 2:
          #raise
          print("Computer raised")
          amt = random.randint(1, 100)
          Dealerr.chips += amt
          Player2.chips -= amt
      update_pot(Dealerr, 1)
      #FLOP
      deck.burn()
      deck.deal(Dealerr)
      deck.deal(Dealerr)
      deck.deal(Dealerr)
      flop1 = display_card(Dealerr.cards[0].get_card_name())
      flop2 = display_card(Dealerr.cards[1].get_card_name())
      flop3 = display_card(Dealerr.cards[2].get_card_name())
      screen.blit(flop1, (300, 300))
      screen.blit(flop2, (400, 300))
      screen.blit(flop3, (500, 300))
      pygame.display.flip()

      #PLAYER OPTION
      if Player1.fold != True:
        option = True
        while option:
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                  #Raise
                  print("Raise")
                  amt = raise_handler(Player1.chips, Dealerr.chips)
                  Dealerr.chips += amt
                  Player1.chips -= amt
                  option = False
          if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                  #Fold
                  Player1.fold = True
                  option = False
          if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                  #Check
                  print("Check")
                  option = False
      #COMPUTER OPTION
      computer_act = random.randint(1, 2)
      if computer_act == 1:
         #check
          print("Computer checked")
      if computer_act == 2:
          #raise
          print("Computer raised")
          amt = random.randint(1, 100)
          Dealerr.chips += amt
          Player2.chips -= amt
      update_pot(Dealerr, 2)
      #TURN
      deck.burn()
      deck.deal(Dealerr)
      turn = display_card(Dealerr.cards[3].get_card_name())
      screen.blit(turn, (600, 300))
      pygame.display.update()
      #PLAYER OPTION
      if Player1.fold != True:
        option = True
        while option:
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                  #Raise
                  print("Raise")
                  amt = raise_handler(Player1.chips, Dealerr.chips)
                  Dealerr.chips += amt
                  Player1.chips -= amt
                  option = False
          if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                  #Fold
                  Player1.fold = True
                  option = False
          if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                  #Check
                  print("Check")
                  option = False
      #COMPUTER OPTION
      computer_act = random.randint(1, 2)
      if computer_act == 1:
         #check
          print("Computer checked")
      if computer_act == 2:
          #raise
          print("Computer raised")
          amt = random.randint(1, 100)
          Dealerr.chips += amt
          Player2.chips -= amt
      update_pot(Dealerr, 3)
      #RIVER
      deck.burn()
      deck.deal(Dealerr)
      river = display_card(Dealerr.cards[4].get_card_name())
      screen.blit(river, (700, 300))
      pygame.display.flip()
      #PLAYER OPTION
      if Player1.fold != True:
        option = True
        while option:
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                  #Raise
                  print("Raise")
                  amt = raise_handler(Player1.chips, Dealerr.chips)
                  Dealerr.chips += amt
                  Player1.chips -= amt
                  option = False
          if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                  #Fold
                  Player1.fold = True
                  option = False
          if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                  #Check
                  print("Check")
                  option = False
      #COMPUTER OPTION
      computer_act = random.randint(1, 2)
      if computer_act == 1:
         #check
          print("Computer checked")
      if computer_act == 2:
          #raise
          print("Computer raised")
          amt = random.randint(1, 100)
          Dealerr.chips += amt
          Player2.chips -= amt
      update_pot(Dealerr, 4)
      #SHOWDOWN
      if Player1.fold == True:
        print("You folded")
        Player1.fold = False
      else:
        showdown(Player1, Player2, Player3, Dealerr)
        print("Player2")
        print(Player2.cards[0])
        print(Player2.cards[1])
        if Player1.win:
          Player1.chips += Dealerr.chips
          print("You won!")
        print("Your Chips:")
        print(Player1.chips)
      
      clock.tick(60)
      hand = False



def play_again():
   screen.fill((0,0,0))
   font_obj = pygame.font.Font('freesansbold.ttf', 16)
   PLAYAGAIN_BUTTON = Button(image=None, pos=(500, 500), text_input="play again", font=font_obj, base_color="#d7fcd4", hovering_color="Blue", press=False)
   PLAYAGAIN_BUTTON.update(screen)
   events = pygame.event.get()
   for event in events:
    if PLAYAGAIN_BUTTON.checkForInput(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
       return True
    if event.type == pygame.QUIT:
       return False
      
   

run_game = True

def main_loop():
  global deck 
  name_text = []
  chip_init = 1000

  

  starting_screen(name_text)
  name_text_init = name_text
  Player1 = Player(name_text_init[0], chip_init, "D")
  Player2 = Player("Player2", chip_init, "SB")
  Player3 = Player("Player3", chip_init, "BB")
  Dealer = Player("Dealer", 0, "DD")

  bool = True
  while bool:
    game_screen(Player1, Player2, Player3, Dealer)
    Dealer.chips = 0
    Player1.cards = []
    Player2.cards = []
    Player3.cards = []
    Dealer.cards = []
    
    deck = StandardDeck()
    deck.shuffle()
    
  
  
  
    for event in pygame.event.get():  
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
    pygame.display.update()


      
main_loop()

#exit pygame
if not run_game:
  pygame.quit()


