class Player:

    all = []

    def __init__(self, username):
        self.username = username
        
    def results(self):
        pass
    
    def games_played(self):
        pass
    
    def played_game(self, game):
        pass
    
    def num_times_played(self, game):
        pass
    
    @classmethod
    def highest_scored(cls, game):
        pass
        

from classes.result import Result