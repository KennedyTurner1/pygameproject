import pygame

class Ship:
    'a class to manage the ship'

    def __init__(self, ai_game): #self reference and the instance of the alien invasion game reference
                                #gives Ship access to all things defined in Alien Invasion
        'initialize the ship and set its starting position'
        self.screen = ai_game.screen #we assign screen to an attribute of Ship 
        self.screen_rect = ai_game.screen.get_rect() #all elements are treated as rectangles... ship and screen are treated as rects
                                                    #getting the location of the ship on the screen *******************************

        self.image = pygame.image.load('images/ship.bmp') #loads the image
        self.rect = self.image.get_rect() #give the location of our ship *****************************************

        self.rect.midbottom = self.screen_rect.midbottom #centered horizontally and aligned with bottom of the screen 

        self.moving_right = False #movement flag, ship is motionless at False
        self.moving_left = False #initializes this attribute as motionless
    
    def update(self): #update the ship's position based on the movement flag
        if self.moving_right: #if the flag is True
            self.rect.x += 1 #move the ship to the right by 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self): #puts the ship to the screen at the location specified by self.rect
        'draw the ship at its current location'
        self.screen.blit(self.image, self.rect)