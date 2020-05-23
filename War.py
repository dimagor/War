import random

deck_of_cards = [i for i in range(2,11) for num in range(4)]

loser_deck = []

#random.seed(42)
random.shuffle(deck_of_cards)

player1_cards = [card for index, card in enumerate(deck_of_cards) if index % 2 == 0]
player2_cards = [card for index, card in enumerate(deck_of_cards) if index % 2 == 1] 
     
print(player1_cards, 'P1 cards')
print(player2_cards, 'P2 cards')
print('')

while len(player1_cards) > 0 and len(player2_cards) > 0:    
    print('Player 1 drew -> {}'.format(player1_cards[0]))
    print('Player 2 drew -> {}'.format(player2_cards[0]))
    if player1_cards[0] > player2_cards[0]:         
        loser_deck.append(player1_cards[0]) 
        loser_deck.append(player2_cards[0])
        for i in loser_deck:             
            player2_cards.append(i)                            
        del player1_cards[0]
        del player2_cards[0] 
        #print(loser_deck, 'loser deck')
        loser_deck = []               
        print('Player 1 won the round!')
    elif player2_cards[0] > player1_cards[0]:          
        loser_deck.append(player2_cards[0])
        loser_deck.append(player1_cards[0])
        for i in loser_deck:
            player1_cards.append(i)          
        del player2_cards[0]   
        del player1_cards[0]
        #print(loser_deck, 'loser deck')            
        loser_deck = []      
        print('Player 2 won the round!')
    elif player1_cards[0] == player2_cards[0]:
        loser_deck.append(player1_cards[0])
        loser_deck.append(player2_cards[0])
        del player1_cards[0] 
        del player2_cards[0]         
        #print(loser_deck, 'loser deck')                  
if len(player1_cards) == 0:
    print('')
    print("Player 2 won the game!")
elif len(player2_cards) == 0:
    print('')
    print("Player 1 won the game!")
