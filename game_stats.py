class GameStats: 
    '''track statistics for alien invasion'''
    def __init__(self, ai_game):
        '''initialize statistics'''
        self.settings = ai_game.settings #the game's settings are our settings
        self.reset_stats() #reset the stats each time a player runs a new game

    def reset_stats(self):
        '''initialize statistics that can change during the game'''
        self.ships_left = self.settings.ship_limit #the number of ships left is defined in the settings 