#!/usr/bin/env python
# coding: utf-8

# In[1]:


class simulate_round:
    '''
    Creating an instance of this class will return a -1 for a player loss, 0 for a tie, and 1 for a player win
    Pass in the player hand, dealer hand, and shuffled deck
    '''
    
    def __calc_hand_value(self, hand):
        '''
        Local function that calculates the value of a hand.
        This can be calculated for a hand of any amount of cards. 
        It attempts to give the highest possible point value without going over 21
        '''
        hand_value = 0
        ace_count = 0
        for card in hand:
            hand_value += card[1] #add card value to hand value
            if card[0][:3] == 'Ace': #count if card is an Ace
                ace_count += 1
        while hand_value > 21 and ace_count > 0: #If hand has an Ace and hand value above 21, count Ace as 1 point
            hand_value -= 10
            ace_count -= 1
        return hand_value
    
    def __init__(self, player_hand, dealer_hand, deck):
        '''
        Define instance variables
        '''
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
        self.deck = deck
        self.player_hand_value = self.__calc_hand_value(player_hand)
        self.dealer_hand_value = self.__calc_hand_value(dealer_hand)
    
    def strategy_hard(self, hit_thresh):
        '''
        This class function executes a player strategy where as long as the player's hand is below hit_thresh points,
            they hit, where an Ace is worth 1 point.
        This spits out a result of the strategy on a given hand.
        '''
        
        player_hand = self.player_hand
        dealer_hand = self.dealer_hand
        player_hand_value = self.player_hand_value
        dealer_hand_value = self.dealer_hand_value
        deck = self.deck

        #print('player:', player_hand, '____ value:', player_hand_value)
        while player_hand_value < hit_thresh: #while hand value of player is <hit_thresh, 'hit'
            next_card = deck[0]
            deck.pop(0) #remove drawn card from deck
            player_hand.append(next_card) #add card to player hand
            if next_card[0][:3] != 'Ace': #if card not an Ace, add the card value to player hand value
                player_hand_value += next_card[1]
            else: #if card is an Ace
                player_hand_value += 1

        #print('dealer:', dealer_hand, '____ value:', dealer_hand_value)
        while dealer_hand_value < 17: #dealer uses consistent "hard 17" rules
            next_card = deck[0]
            deck.pop(0)
            dealer_hand.append(next_card)
            dealer_hand_value += next_card[1]

        player_hand_value = self.__calc_hand_value(player_hand) #calculate resulting hand values for player and dealer
        dealer_hand_value = self.__calc_hand_value(dealer_hand)
        #print('player:', player_hand, '____ value:', player_hand_value)
        #print('dealer:', dealer_hand, '____ value:', dealer_hand_value)

        result = 0 #result if tie
        if dealer_hand_value > 21: #if dealer hand is over 21, player wins
            result = 1
        elif player_hand_value > 21: #if player hand is over 21 and dealer hand is not over 21, dealer wins
            result = -1
        elif player_hand_value > dealer_hand_value: #if neither is over 21 and player hand is higher value, player wins
            result = 1
        elif player_hand_value < dealer_hand_value: #if neither is over 21 and dealer hand is higher value, dealer wins
            result = -1
        return result
    
    def strategy_soft(self, hit_thresh):
        '''
        This class function executes a player strategy where as long as the player's hand is below hit_thresh points,
            they hit, where an Ace is worth 11 points.
        This spits out a result of the strategy on a given hand.
        '''
        
        player_hand = self.player_hand
        dealer_hand = self.dealer_hand
        player_hand_value = self.player_hand_value
        dealer_hand_value = self.dealer_hand_value
        deck = self.deck

        #print('player:', player_hand, '____ value:', player_hand_value)
        while player_hand_value < hit_thresh: #while hand value of player is <hit_thresh, 'hit'
            next_card = deck[0]
            deck.pop(0) #remove drawn card from deck
            player_hand.append(next_card) #add card to player hand
            player_hand_value += next_card[1] #add value of card to player hand value

        #print('dealer:', dealer_hand, '____ value:', dealer_hand_value)
        while dealer_hand_value < 17: #dealer uses consistent "hard 17" rules
            next_card = deck[0]
            deck.pop(0)
            dealer_hand.append(next_card)
            dealer_hand_value += next_card[1]

        player_hand_value = self.__calc_hand_value(player_hand) #calculate resulting hand values for player and dealer
        dealer_hand_value = self.__calc_hand_value(dealer_hand)
        #print('player:', player_hand, '____ value:', player_hand_value)
        #print('dealer:', dealer_hand, '____ value:', dealer_hand_value)

        result = 0 #result if tie
        if dealer_hand_value > 21: #if dealer hand is over 21, player wins
            result = 1
        elif player_hand_value > 21: #if player hand is over 21 and dealer hand is not over 21, dealer wins
            result = -1
        elif player_hand_value > dealer_hand_value: #if neither is over 21 and player hand is higher value, player wins
            result = 1
        elif player_hand_value < dealer_hand_value: #if neither is over 21 and dealer hand is higher value, dealer wins
            result = -1
        return result
    
    def strategy_base(self):
        '''
        This class function executes a player strategy under some of the "basic" strategy rules.
        This spits out a result of the strategy on a given hand.
        '''
        
        player_hand = self.player_hand
        dealer_hand = self.dealer_hand
        dealer_upcard = dealer_hand[-1]
        player_hand_value = self.player_hand_value
        dealer_hand_value = self.dealer_hand_value
        deck = self.deck

        #print('player:', player_hand, '____ value:', player_hand_value)
        break_flag = 1
        while break_flag and player_hand_value<=21: 
            if any(c[1]==11 for c in player_hand): #soft hand, has an ace
                if 19<=player_hand_value<=21:
                    break_flag = 0
                elif player_hand_value==18 and 9<=dealer_upcard[1]<=11:
                    break_flag = 0   
                else:
                    next_card = deck[0]
                    deck.pop(0) #remove drawn card from deck
                    player_hand.append(next_card) #add card to player hand
                    player_hand_value += next_card[1] #add value of card to player hand value
                    continue
            elif all(c[1]!=11 for c in player_hand): #hard hand, no aces
                if 17<=player_hand_value<=21:
                    break_flag = 0
                elif 13<=player_hand_value<=16 and 2<=dealer_upcard[1]<=6:
                    break_flag = 0
                elif player_hand_value==12 and 4<=dealer_upcard[1]<=6:
                    break_flag = 0
                else:
                    next_card = deck[0]
                    deck.pop(0) #remove drawn card from deck
                    player_hand.append(next_card) #add card to player hand
                    player_hand_value += next_card[1] #add value of card to player hand value
                    continue

        #print('dealer:', dealer_hand, '____ value:', dealer_hand_value)
        while dealer_hand_value < 17: #dealer uses consistent "hard 17" rules
            next_card = deck[0]
            deck.pop(0)
            dealer_hand.append(next_card)
            dealer_hand_value += next_card[1]

        player_hand_value = self.__calc_hand_value(player_hand) #calculate resulting hand values for player and dealer
        dealer_hand_value = self.__calc_hand_value(dealer_hand)
        #print('player:', player_hand, '____ value:', player_hand_value)
        #print('dealer:', dealer_hand, '____ value:', dealer_hand_value)

        result = 0 #result if tie
        if dealer_hand_value > 21: #if dealer hand is over 21, player wins
            result = 1
        elif player_hand_value > 21: #if player hand is over 21 and dealer hand is not over 21, dealer wins
            result = -1
        elif player_hand_value > dealer_hand_value: #if neither is over 21 and player hand is higher value, player wins
            result = 1
        elif player_hand_value < dealer_hand_value: #if neither is over 21 and dealer hand is higher value, dealer wins
            result = -1
        return result


# In[2]:


class LCG:
    '''
    To create an LCG instance you pass in a seed. You pass in other parameters to create a different LCG, 
        but the default is the same one as used by the POSIX rand() function
    '''
    def __init__(self, seed, a=1103515245, c=12345, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next_seed(self): #return a new seed
        self.state = (self.a * self.state + self.c) % self.m
        return self.state
    
    def next_prob(self): #return a probability
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m


# In[ ]:




