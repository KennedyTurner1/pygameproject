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
        self.ship_limit = 3 #number of ships allowed before you die

        #bullet settings
        self.bullet_speed = 1.5 #bullets will travel slower than the ship
        self.bullet_width = 3 #width of 3 pixels
        self.bullet_height = 15 #height of 15 pixels
        self.bullet_color = (60, 60, 60) #dark gray bullet
        self.bullets_allowed = 3 #limit the number of bullets fired at one time

        #alien settings
        self.alien_speed = 5.0 #alien movement speed
        self.fleet_drop_speed = 10 #this is the speed the alien will drop when it hits the right edge of the screen
        self.fleet_direction = 1 #default is right
                                 #fleet direction of 1 represents right, -1 represents left