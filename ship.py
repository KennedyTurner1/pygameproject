import pygame

class Ship:
    'a class to manage the ship'

    def __init__(self, ai_game): #self reference and the instance of the alien invasion game reference
                                #gives Ship access to all things defined in Alien Invasion
        'initialize the ship and set its starting position'
        self.screen = ai_game.screen #assign screen to an attribute of Ship 
        self.settings = ai_game.settings #assign settings as an attribute of Ship  
        self.screen_rect = ai_game.screen.get_rect() #all elements are treated as rectangles... ship and screen are treated as rects
                                                    #getting the location of the ship on the screen *******************************

        self.image = pygame.image.load('images/ship.bmp') #loads the image
        self.rect = self.image.get_rect() #give the location of our ship 

        self.rect.midbottom = self.screen_rect.midbottom #centered horizontally and aligned with bottom of the screen 

        self.x = float(self.rect.x) #store a decimal value for the ship's horizontal position

        self.moving_right = False #movement flag, ship is motionless at False
        self.moving_left = False #initializes this attribute as motionless
    
    def update(self): #update the ship's position based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right: #if this is true and the ships position is less than the screen bounds
            self.x += self.settings.ship_speed #move the ship to the right by the current speed
        if self.moving_left and self.rect.left > 0: #flag is True and the position of the x coordinate of the ship isn't greater than 0 
                                                    #the top left corner of the screen is (0,0)
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x #update the ships position from self.x to self.rect.x because that controls the position of the ship

    def blitme(self): #puts the ship to the screen at the location specified by self.rect
        'draw the ship at its current location'
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''center the ship on the screen'''
        self.rect.midbottom = self.screen_rect.midbottom #make the screen's midbottom the smae position as our ship
        self.x = float(self.rect.x) #update the position of our x position