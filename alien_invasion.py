import sys

import pygame

class AlienInvasion: #overall class to manage game assets and behavior. Empty window. 
    def __init__(self): #initialize game and create resources 
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self): #start the main loop for the game
        while True: #watch for keyboard and mouse events
            for event in pygame.event.get():
                