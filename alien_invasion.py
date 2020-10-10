import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion: 
    '''overall class to manage game assets and behavior. Empty window.'''
    def __init__(self): 
        '''initalizes the game and then creates settings'''
        pygame.init() #initalize background settings 
        self.settings = Settings() #create an instance of Settings and assign it to self.settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # screen is a surface
        pygame.display.set_caption("Alien Invasion") #set the caption

        self.ship = Ship(self) #makes an instance of Ship which requires one argument, self, to get the attributes of Alien Invasion

        self.bg_color = (self.settings.bg_color) 
                                                #set the background color from the instance of line 12 *********************************
    
    def run_game(self): 
        '''runs the game by starting the main loop'''
        while True: #watch for keyboard and mouse events
                    #an event is an action the user performs while playing the game
            self._check_events() 
            self.ship.update() #called the method update() in ship.py to update the position of the ship
            self._update_screen()

    def _check_events(self):
        '''respond to keypresses and mouse events'''
        for event in pygame.event.get(): #event loop, returns a list of events that have taken place since last called
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN: #if the key stroke is down 
                if event.key == pygame.K_RIGHT: #and it is to the right
                    self.ship.moving_right = True #the ship needs to be moved right by 1
                elif event.key == pygame.K_LEFT: 
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP: #if the keystroke is up
                if event.key == pygame.K_RIGHT: #and it is right
                    self.ship.moving_right = False #nothing is being pressed, don't do anything
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False #use elif instead of if because if the player presses two keys at once
                                                  #two separate events will be detected

            
    def _update_screen(self):
        '''update the images on the screen, flip to the newest screen'''
        self.screen.fill(self.settings.bg_color) #redraw the screen for each pass through the loop
                                                 #fill the screen with the background color
        self.ship.blitme() #draw the ship on the screen 

        pygame.display.flip()  #Make the most recently drawn/updated screen visible.
            
if __name__ == '__main__': 
    '''making an instance and running the game'''
    ai = AlienInvasion() #instance of the game
    ai.run_game() #run the game
