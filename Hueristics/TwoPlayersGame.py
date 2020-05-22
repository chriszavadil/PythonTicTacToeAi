# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:04:16 2020
This was a project I worked on during the Python A-Z AI Bootcamp using Negamax
@author: Chris Zavadil
"""


from copy import deepcopy


class TwoPlayersGame:
    
    
    def play(self, nmoves=1000, verbose=True):
        
        history = []
        
        if verbose:
            self.show()
        
        for self.nmove in range(1, nmoves+1):
            
            if self.is_over():
                break
            
            move = self.player.ask_move(self)
            history.append((deepcopy(self), move))
            self.make_move(move)
            
            if verbose:
                print( "\nMove #%d: player %d plays %s :"%(
                             self.nmove, self.nplayer, str(move)) )
                self.show()
                
            self.switch_player()
        
        history.append(deepcopy(self))
        
        return history
    
    @property
    def nopponent(self):
        return 2 if (self.nplayer == 1) else 1
    
    @property
    def player(self):
        return self.players[self.nplayer- 1]
    
    @property
    def opponent(self):
        return self.players[self.nopponent - 1]
    
    def switch_player(self):
        self.nplayer = self.nopponent

    def copy(self):
        return deepcopy(self)