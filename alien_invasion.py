import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

class AlienInvasion: 
    '''overall class to manage game assets and behavior. Empty window.'''
    def __init__(self): 
        '''initalizes the game and then creates settings'''
        pygame.init() #initalize background settings 
        self.settings = Settings() #create an instance of Settings and assign it to self.settings

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # the main surface is assigned to a screen, make the game fullscreen
        self.settings.screen_width = self.screen.get_rect().width #************************************************************
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion") #set the caption

        self.ship = Ship(self) #makes an instance of Ship which requires one argument, self, to get the attributes of Alien Invasion
        self.bullets = pygame.sprite.Group() #create an instance of bullets in a group that have already been fired 
    
    def run_game(self): 
        '''runs the game by starting the main loop'''
        while True: #watch for keyboard and mouse events
                    #an event is an action the user performs while playing the game
            self._check_events() 
            self.ship.update() #called the method update() in ship.py to update the position of the ship
            self._update_bullets() #calls the update bullets method to update all the bullets
            self._update_screen() #calls the update screen method to show the newest screen 

    def _check_events(self):
        '''respond to keypresses and releases'''
        for event in pygame.event.get(): #event loop, returns a list of events that have taken place since last called
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN: #if the key stroke is down
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: #if the keystroke is up
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''respond to keypresses and releases'''
        if event.key == pygame.K_RIGHT: #and it is to the right
            self.ship.moving_right = True #the ship needs to be moved right by the speed
        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #efficient way to quit the game, press the Q button 
            sys.exit()
        elif event.key == pygame.K_SPACE: #if the spacebar is pressed
            self._fire_bullet() #fire a bullet

    def _check_keyup_events(self, event):
        '''respond to keypresses'''
        if event.key == pygame.K_RIGHT: #and it is right
            self.ship.moving_right = False #nothing is being pressed, don't do anything
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False #use elif instead of if because if the player presses two keys at once
                                          #two separate events will be detected
    
    def _fire_bullet(self):
        '''create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed: #if the amount of bullets in the group is less than 3:
            new_bullet = Bullet(self) #create an instance of a bullet
            self.bullets.add(new_bullet) #add the bullet to the group of bullets

    def _update_bullets(self):
        '''update the position of bullets and get rid of old bullets'''
        self.bullets.update() #calls the update() method in bullet.py

        '''let's get rid of the bullets that have disappeared off the screen'''
        for bullet in self.bullets.copy():  #pygames doesn't allow you to adjust the length of a for loop while it is running
                                            #we use a copy of the bullets to modify the bullets inside the loop
            if bullet.rect.bottom <= 0: #if the bottom of the bullet's y coordinate is negative
                self.bullets.remove(bullet) #remove is from the group

       
    def _update_screen(self):
        '''update the images on the screen, flip to the newest screen'''
        self.screen.fill(self.settings.bg_color) #redraw the screen for each pass through the loop
                                                 #fill the screen with the background color
        self.ship.blitme() #draw the ship on the screen 
        for bullet in self.bullets.sprites(): #for every bullet in the group 
            bullet.draw_bullet() #make sure the bullet is drawn

        pygame.display.flip()  #Make the most recently drawn/updated screen visible.
            
if __name__ == '__main__': 
    '''making an instance and running the game'''
    ai = AlienInvasion() #instance of the game
    ai.run_game() #run the game
