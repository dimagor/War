import random

deck_of_cards = [i for i in range(2,11) for num in range(4)]

Tie_lst = []

random.shuffle(deck_of_cards)
random.seed(42)

class Player(): 
    
    def __init__(self, cards):
        self.cards = cards
              
    def cut_deck(self):
        if self == player1:
            self.cards = [card for index, card in enumerate(deck_of_cards) if index % 2 == 0]
        elif self == player2:
            self.cards = [card for index, card in enumerate(deck_of_cards) if index % 2 == 1] 
     
player1 = Player([]) 
player2 = Player([])    

def compare_cards():
    while len(player1.cards) > 0 and len(player2.cards) > 0:    
            print('Player 1 drew -> {}'.format(player1.cards[0]))
            print('Player 2 drew -> {}'.format(player2.cards[0]))
            if player1.cards[0] > player2.cards[0]:
                player2.cards.append(player1.cards[0])
                del player1.cards[0]
                return 'Player 1 won the round!'
            elif player2.cards[0] > player1.cards[0]:
                player1.cards.append(player2.cards[0])
                del player2.cards[0]
                return 'Player 2 won the round!'
            elif player1.cards[0] == player2.cards[0]:
                tie_lst.append(player1.cards[0])
                del player1.cards[0] and del player2.cards[0]
                
    else:
        if len(player1.cards == 0):
            return "Player 1 lost!"
        elif len(player2.cards == 0):
            return "Player 2 lost!"


Player.cut_deck(player1)
Player.cut_deck(player2)

print(compare_cards())
    
