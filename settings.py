class Settings: 
    '''a class to store all settings for Alien Invasion game'''
    def __init__(self):
        '''initalize the game's settings'''
        #screen settings 
        self.screen_width = 1200 #1200 pixels wide
        self.screen_height = 800 #800 pixels high 
        self.bg_color = (230, 230, 230) #equal red, blue, green 

        #ship settings
        self.ship_speed = 1.5 #speed that the ship can move

        #bullet settings
        self.bullet_speed = 1.0 #bullets will travel slower than the ship
        self.bullet_width = 3 #width of 3 pixels
        self.bullet_height = 15 #height of 15 pixels
        self.bullet_color = (60, 60, 60) #dark gray bullet