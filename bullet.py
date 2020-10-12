import pygame

from pygame.sprite import Sprite #sprite helps to group related objects in our game

class Bullet(Sprite):
    '''A class to manage bullets fired from the ship'''

    def __init__(self, ai_game): #ai_game is an attribute of the whole game
        '''create a bullet object at the ship's current position'''
        super().__init__() 
        self.screen = ai_game.screen #put the screen of the bullet on the ai game screen 
        self.settings = ai_game.settings #put the settings of the bullet on the ai game screen 
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height) #create a bullet position from imported Rec() class.
                                                                                              #the rect() position from the ship is bc it was an image
        self.rect.midtop = ai_game.ship.rect.midtop #this puts the bullet on top of the ship 

        self.y = float(self.rect.y) #store the bullet's position as a decimal value

    def update(self):
        '''Move the bullet up the screen'''
        self.y -= self.settings.bullet_speed #update the decimal position of the bullet
                                             #a fired bullet decreases the y coordinate as it moves up the screen
        self.rect.y = self.y #update the position of the bullet with the speed 
    
    def draw_bullet(self):
        '''draw the game bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect) #draw.rect fills the part of the screen defined by the bullet's position
                                                             #with the color of the bullet 

    



