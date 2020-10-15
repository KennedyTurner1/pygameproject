class Settings: 
    '''a class to store all settings for Alien Invasion game'''
    def __init__(self):
        '''initalize the game's static settings'''
        #screen settings 
        self.screen_width = 1200 #1200 pixels wide
        self.screen_height = 800 #800 pixels high 
        self.bg_color = (230, 230, 230) #equal red, blue, green 

        #ship settings
        self.ship_limit = 3 #number of ships allowed before you die

        #bullet settings
        self.bullet_width = 3 #width of 3 pixels
        self.bullet_height = 15 #height of 15 pixels
        self.bullet_color = (60, 60, 60) #dark gray bullet
        self.bullets_allowed = 3 #limit the number of bullets fired at one time

        #alien settings
        self.fleet_drop_speed = 10 #this is the speed the alien will drop when it hits the right edge of the screen

        #How quickly the game speeds up
        self.speed_up_scale = 1.1 #as a new fleet is created, the aliens speed up

        #How quickly the alien point values increase
        self.score_scale = 1.5 #as the speed increases, the point values increase

        self.initalize_dynamic_settings()
    
    def initalize_dynamic_settings(self):
        '''initialize the settings that change throughout the game'''
        self.ship_speed = 1.5 #speed that the ship can move
        self.bullet_speed = 3.0 #bullets will travel slower than the ship
        self.alien_speed = 1.0 #alien movement speed
        self.fleet_direction = 1 #default is right
                                 #fleet direction of 1 represents right, -1 represents left
        self.alien_points = 50 #each time an alien is hit, increase the points by 50

    def increase_speed(self):
        '''increase speed settings and alien point values'''
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale) #when we increase the speed, we increase the point value at each level up
