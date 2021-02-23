# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:50:10 2021

@author: tomsc
"""

import random
def createDeck():
    cardfaces =[]
    suits = ["Hearts","Spades","Dimonds","Clubs"]
    royals = ["A","K","Q","J"]
    Deck =[]
   
    
    for i in range(2,11):
       cardfaces.append(str(i))
    
    for j in range(4):
       cardfaces.append(royals[j])

    for k in range(4):
      for l in range(13):
        card = (cardfaces[l] + " of " + suits[k])
        Deck.append(card)
    random.shuffle(Deck)
    return Deck
cardDeck = createDeck()
print(cardDeck)    

class Player:
    def __init__(self,bet,hand =[] , money =500):
        self.hand = hand
        self.money = money
        self.bet = bet
        
        
    def bet(self,amount,money):
        self.money -= amount
        self.bet += amount  
       
        
                  

player1 = input("Player1:Please enter your name." " ") 
player2 = input ("Player2:Please enter your name." " ")
cardDeck = createDeck()

Tom = cardDeck.pop()
print(Tom) 
Bob = cardDeck.pop() 
print(Bob)
Tom = cardDeck.pop()
print(Tom) 
Bob = cardDeck.pop() 
print(Bob)
Tom.bet (100)
print(Tom.money, Tom.bet)
Dealer = cardDeck.pop(),cardDeck.pop(),cardDeck.pop()
print()

print(Tom) 
Dealer = cardDeck.pop()       