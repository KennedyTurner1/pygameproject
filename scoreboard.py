import pygame.font #renders text screen

class Scoreboard:
    '''a class to report scoring information'''
    def __init__(self, ai_game): 
        '''initialize scorekeeping attributes'''
        self.screen = ai_game.screen #put our element on the game screen 
        self.screen_rect = self.screen.get_rect() #get the position of our element
        self.settings = ai_game.settings #scoreboard settings are the game settings 
        self.stats = ai_game.stats #scoreboard stats are the game stats
        
        '''font settings for scoring information'''
        self.text_color = (30, 30, 30) #black text
        self.font = pygame.font.SysFont(None, 48) #default font, size 48, instantiate a font object

        '''prepare the initial score image'''
        self.prep_score() 
    
    def prep_score(self):
        '''Turn the score into a rendered image'''
        score_str = str(self.stats.score) #take the score as an int and turn it into a string 
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color) #take the string and pass it as an image obj

        '''display the score at the top right of the screen'''
        self.score_rect = self.score_image.get_rect() #get the current position of the image and set it as the score-rect position
        self.score_rect.right = self.screen_rect.right - 20 #put the image in the right corner minus 20 pixels
        self.score_rect.top = 20 #put the image from the top of the screen by 20 pixels
    
    def show_score(self):
        '''draw score to the screen'''
        self.screen.blit(self.score_image, self.score_rect) #draw the image on the screen at the defined position score_rect
    