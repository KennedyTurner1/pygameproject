import pygame.font #renders text screen
from pygame.sprite import Group #we are making a group of ships
from ship import Ship

class Scoreboard:
    '''a class to report scoring information'''
    def __init__(self, ai_game): 
        '''initialize scorekeeping attributes'''
        self.ai_game = ai_game #assign the game instance to an attribute 
        self.screen = ai_game.screen #put our element on the game screen 
        self.screen_rect = self.screen.get_rect() #get the position of our element
        self.settings = ai_game.settings #scoreboard settings are the game settings 
        self.stats = ai_game.stats #scoreboard stats are the game stats
        
        '''font settings for scoring information'''
        self.text_color = (30, 30, 30) #black text
        self.font = pygame.font.SysFont(None, 48) #default font, size 48, instantiate a font object

        '''prepare the score images'''
        self.prep_score() #display the starting score 
        self.prep_high_score() #display the high score 
        self.prep_level() #display the level
        self.prep_ships() #display the number of ships 

    def prep_score(self):
        '''Turn the score into a rendered image'''
        rounded_score = round(self.stats.score, -1) #pass a negative number and it will round to be nearest 10
        score_str = "{:,}".format(rounded_score) #this tells python to insert commas into the rounded score
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color) #take the string and pass it as an image obj

        '''display the score at the top right of the screen'''
        self.score_rect = self.score_image.get_rect() #get the current position of the image and set it as the score-rect position
        self.score_rect.right = self.screen_rect.right - 20 #put the image in the right corner minus 20 pixels
        self.score_rect.top = 20 #put the image from the top of the screen by 20 pixels

    def prep_high_score(self):
        '''turn the high score into a rendered image'''
        high_score = round(self.stats.high_score, -1) #round the highest score to the closest 10
        high_score_str = "{:,}".format(high_score) #add commas
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color) #make an image object for high score

        '''center the high score at the top of the screen'''
        self.high_score_rect = self.high_score_image.get_rect() #get the position of the image
        self.high_score_rect.centerx = self.screen_rect.centerx #center it at the x axis
        self.high_score_rect.top = self.score_rect.top #put it at the top 
    
    def prep_level(self):
        '''turn the level into a rendered image'''
        level_str = str(self.stats.level) #take the level as an int and turn it into a string 
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color) #take the string and pass it as an image obj

        '''display the score at the top right of the screen'''
        self.level_rect = self.level_image.get_rect() #get the current position of the image and set it as the level position
        self.level_rect.right = self.screen_rect.right - 20 #put the image in the right corner of the screen minus 20 pixels
        self.level_rect.top = self.score_rect.bottom + 10 #put the position of the level 10 pixels from the bottom of the score object
    
    def prep_ships(self):
        '''show how many ships are left'''
        self.ships = Group()         #creates an empty group to hold ship instances
        for ship_number in range(self.stats.ships_left): #this loop runs for every ship the player has left
            ship = Ship(self.ai_game) #create a new ship (instance)
            ship.rect.x = 10 + ship_number * ship.rect.width #place every ship a little bit away from each other (by a width)
            ship.rect.y = 10 #appear in the upper left corner
            self.ships.add(ship) #add the ship to the group

    def check_high_score(self):
        '''check to see if there is a new high score'''
        if self.stats.score > self.stats.high_score: #if the score is greater than the high score 
            self.stats.high_score = self.stats.score #the score becomes the high score
            self.prep_high_score() #prep the high score to be passed as the new image
    
    def show_score(self):
        '''draw score to the screen'''
        self.screen.blit(self.score_image, self.score_rect) #draw the image on the screen at the defined position score_rect
        self.screen.blit(self.high_score_image, self.high_score_rect) #draw the high score image on the screen at the set location
        self.screen.blit(self.level_image, self.level_rect) #draw the level
        self.ships.draw(self.screen) #we call draw on a group rather than one value (like score)


    