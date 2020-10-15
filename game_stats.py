class GameStats: 
    '''track statistics for alien invasion'''
    def __init__(self, ai_game):
        '''initialize statistics'''
        self.settings = ai_game.settings #the game's settings are our settings
        self.reset_stats() #reset the stats each time a player runs a new game

        '''start AlienInvasion game in an inactive state'''
        self.game_active = False #start the game inactive so a player can press a play button to change the flag state

    def reset_stats(self):
        '''initialize statistics that can change during the game'''
        self.ships_left = self.settings.ship_limit #the number of ships left is defined in the settings, set it back to 3
        self.score = 0  #reset the score each time a new game starts, not just one time (not in __init__)