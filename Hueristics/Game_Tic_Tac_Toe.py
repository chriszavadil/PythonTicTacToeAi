# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:43:45 2020
This was a project I worked on during the Python A-Z AI Bootcamp using Negamax
@author: Chris Zavadil
"""

# Brining in easyAI Assets
from easyAI import TwoPlayersGame, AI_Player, Negamax
from easyAI.Player import Human_Player


# Creating our game controller with necessary game methods
class GameController(TwoPlayersGame):
    def __init__(self, players):
        
        # Setting up our players
        self.players = players

        # Designating who goes first
        self.nplayer = 1 

        # Creating a 3x3 board that is numbered 1-9
        self.board = [0] * 9
    
    # Defining all possible moves
    def possible_moves(self):
        return [a + 1 for a, b in enumerate(self.board) if b == 0]
    
    # Adjusting the game board after a move has been made
    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    # End game loss condition 
    def loss_condition(self):
        possible_combinations = [[1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

        return any([all([(self.board[i-1] == self.nopponent)
                for i in combination]) for combination in possible_combinations]) 
        
    # Check if the game is over with a loss or tie
    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()
        
    # Show the current board status
    def show(self):
        print('\n'+'\n'.join([' '.join([['.', 'O', 'X'][self.board[3*j + i]]
                for i in range(3)]) for j in range(3)]))
                 
    # Defining a scoring system
    def scoring(self):
        return -100 if self.loss_condition() else 0

if __name__ == "__main__":
    
    # Define the Negamax algorithm and designate depth level
    algorithm = Negamax(8)
    
    # Displaying the rules for our player
    checkers_info = open('checkers_info.txt')
    print(checkers_info.read())
    
    # Checking if our player is ready to start
    start_conditon = input("\nAre you ready to start the game? (y/n):").lower()
    
    if start_conditon == 'y':
        # Start the game
        GameController([Human_Player(), AI_Player(algorithm)]).play()
        
    else:
        print("\n\nOk, Goodbye!")