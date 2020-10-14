import pygame.font #renders text screen

class Button:
    '''a class to create a play button
    for the user to push to start the game'''
    def __init__(self, ai_game, msg): #msg contains the button's text
        '''initialize button attributes'''
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect()
        
        '''set the dimensions and properties of the button'''
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) #green button
        self.text_color = (255, 255, 255) #white text
        self.font = pygame.font.SysFont(None, 48) #default font, sixe 48

        '''build the game's rect object and center it'''
        self.rect = pygame.Rect(0, 0, self.width, self.height) #make the object (x,y,width,height)
        self.rect.center = self.screen_rect.center #the buttons center attribute should match the screen's 

        '''the button message needs to be prepped only once'''
        self._prep_msg(msg) #renders the text as an image

    def _prep_msg(self, msg): #needs a self and a msg paramater to be rendered as an image 
        '''turn msg into a rendered image and
        center the text on the button'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #returns text stored in msg into an image and assigns to self.msg_image
        self.msg_image_rect = self.msg_image.get_rect() #create a position from the image
        self.msg_image_rect.center = self.rect.center  #set the image of the text to be centered the same as the button

    def draw_button(self):
        '''draw blank button and then draw message'''
        self.screen.fill(self.button_color, self.rect) #draw the rectangular portion of the button
        self.screen.blit(self.msg_image, self.msg_image_rect) #blit() calls the the text image and the rect object associated with the text