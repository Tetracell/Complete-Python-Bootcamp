# Create a simple blackjack game with one player and one computer.
import random
import os

# TODO:
#   -Account for the Ace better. Is it possible for its value to change during the hand?

def winning_hand(player, dealer):
    if player.hand_value() > dealer.hand_value():
        return 'player'
    elif player.hand_value() < dealer.hand_value():
        return 'dealer'
    elif player.hand_value() == dealer.hand_value():
        return 'push'


def bet_return(pot,player):
    if player.hand_value() != 21:
        player.chips.add(int(pot + pot*(3/2)))
    else:
        player.chips.add(int(pot + pot*(2/1)))


def play_again():
    answer = raw_input("Would you like to play again? (y/n) :")
    if answer == 'y':
        return True
    else:
        print "See you next time."
        return False


def bust(person):
    if person.hand_value() > 21:
        return True


def dealer_turn(dealer, deck):
    playing = True
    while playing: 
        print "The dealer shows: ", dealer.hand
        if dealer.hand_value() < 17:
            dealer.draw(deck)
            if bust(dealer):
                playing = False
                return 'bust'
            else:
                continue
        elif dealer.hand_value() >= 17 and dealer.hand_value() != 21 and not bust(dealer):
            print "The dealer stands."
            playing = False
        elif dealer.hand_value() == 21:
            print "Dealer has 21. Bets will now be resolved."
            playing = False


def player_turn(player,deck):
    playing = True
    print player.hand
    while playing:
        decision = raw_input("What do you wish to do? (s)tand, (h)it, (su)rrender :")
        if decision == 's':
            print "You have a hand value of",player.hand_value()
            playing = False
        elif decision == 'h':
            player.draw(deck)
            print "You have",player.hand,"in your hand."
            if bust(player):
                playing = False
                return 'bust'


def initial_draw(person):
    person.hand = []
    person.draw(deck)
    person.draw(deck)


def new_game():
    print "Welcome to Blackjack!"
    name = raw_input("What is your name? ")
    player1 = Player(name)
    print "Welcome,",player1.name,". You have",player1.chips.total," chips to bet with."
    return player1


def card_maker(hand):
    for i in hand:
        print ":----------:"
        print ":%s        %s:"%(i[1],i[1])
        print ":          :"
        print ":          :"
        print ":    %s     :"%(i[0]) 
        print ":          :"
        print ":          :"
        print ":%s        %s:"%(i[1],i[1])
        print ":----------:" 
        
           
def value_count(hand):
    ten_points = ['0', 'K', 'Q', 'J']
    hand_total = 0
    for card in hand:
        if card[0] in ten_points:
            hand_total += 10
        elif card[0] == 'A':
            if hand_total >= 11:
                hand_total += 1
            else:
                hand_total += 11
        else:
            hand_total += int(card[0])
    return hand_total   

 
class Chips():
    def __init__(self):
        self.total = 200

    def add(self, amt):
        self.total += amt

    def sub(self, amt):
        self.total -= amt


class Deck():
    def __init__(self):
        self.card_count = 52
        self.cards = ['2','3','4','5','6','7','8','9','0','K','Q','J','A']
        self.suits = ['D','H','C','S']
        self.deck = []
        self.shuffle()
    
    def draw(self):
        drawn_card = list.pop(self.deck)
        self.card_count -= 1
        return drawn_card

    def shuffle(self):
        self.deck = []
        for c in self.cards:
            for s in self.suits:
                self.deck.append(c+s)
        random.shuffle(self.deck)
        self.card_count = 52


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0
        self.chips = Chips()

    def hand_value(self):
        self.value = value_count(self.hand) # What the fuck is going on here.
        return self.value

    def bet(self, bet):
        self.chips.sub(bet)
                
    def draw(self,deck):
        self.hand.append(deck.draw())


class Dealer():
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.value = 0

    def draw(self, deck):
        self.hand.append(deck.draw())

    def hand_value(self):
        self.value = value_count(self.hand)
        return self.value # The old value here was self.hand_value. There is no reference to that anywhere. Fucking, be careful.



deck = Deck()
dealer = Dealer()

#player1 = new_game()
playing = True
player1 = Player("Tom")

# Main game loop

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    print "You have",player1.chips.total,"chips."
    bet = raw_input("How many chips would you like to bet? ")
    pot = int(bet)
    player1.bet(pot)

    print "You have bet",bet,"chips, and have",player1.chips.total,"chips remaning."
    print "The dealer will draw first."
    initial_draw(dealer) # Dealer goes first, draws two cards with hidden hole card
    if dealer.hand_value() == 21:
        print "Dealer shows a Blackjack! Good luck."
    else:
        print "The dealer shows a", dealer.hand[0],"along with his hole card." # The second card is the hole card, not the first

    initial_draw(player1) # Player then does their initial draw of two cards
    player_result = player_turn(player1, deck) # Player's turn shoved into a variable
    if player_result == 'bust':
        print "You've busted."
        playing = play_again()
        if playing:
            continue

    dealer_result = dealer_turn(dealer, deck)
    if dealer_result == 'bust':
        print "The dealer has busted. You win!"
        bet_return(pot, player1)
        playing = play_again()
        if playing:
            continue

    print "Dealer had: ", dealer.hand, "    Player had: ", player1.hand
    result = winning_hand(player1,dealer)
    if result == 'player':
        print "Player wins!"
        bet_return(pot, player1)
    elif result == 'dealer':
        print "Dealer wins! Better luck next time."
    elif result == 'push':
        print "Hand is tied! Bets are returned."
        player1.chips.add(pot)

    playing = play_again()
    if playing:
        continue

    