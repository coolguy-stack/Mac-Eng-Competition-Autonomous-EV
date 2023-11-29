import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Communication')

font_1 = pygame.font.SysFont(None, 40)
font_2 = pygame.font.SysFont(None, 50)

home = True
show_message = False
show_confirmation = False
show_custom_message = False
username = "User Name" #change to your name
receiving = True #change to receive a call
contact_name = "Caller's Name" #change to caller's name

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

accept_logo = pygame.image.load('accept.jpg').convert_alpha()
decline_logo = pygame.image.load('decline.jpg').convert_alpha()
message_logo = pygame.image.load('message.png').convert_alpha()
rectangle = pygame.image.load('rectangle1.png').convert_alpha()

accept_button = Button(150, 300, accept_logo, 1)
message_button = Button(350, 300, message_logo, 1.1)
decline_button = Button(550, 300, decline_logo, 1)
suggestion_button = Button(100, 140, rectangle, 1)
custom_button = Button(170, 260, rectangle, 0.75)

def draw_text(text, font, color, x, y):
  img = font.render(text, True, color)
  screen.blit(img, (x, y))

def receive_call(contact_name):
  text_1 = font_1.render("Incoming call from:", True, (0,0,0))
  text_rect = text_1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
  screen.blit(text_1, text_rect)

  text_2 = font_2.render(contact_name, True, (0,0,0))
  text_rect = text_2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
  screen.blit(text_2, text_rect)

  accept_button.draw()
  decline_button.draw()
  message_button.draw()

def home_screen(username):
  text_3 = font_2.render("Hello, " + username, True, (0,0,0))
  text_rect = text_3.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
  screen.blit(text_3, text_rect)

def message(contact_name):
  text_4 = font_1.render("Send a message to " + contact_name + ":", True, (0,0,0))
  text_rect = text_4.get_rect(center=(SCREEN_WIDTH/2, 100))
  screen.blit(text_4, text_rect)

  text_5 = font_1.render("Sorry, I am driving. Can I call you later?", True, (0,0,0))
  text_rect = text_5.get_rect(center=(SCREEN_WIDTH/2, 200))
  screen.blit(text_5, text_rect)

  text_6 = font_1.render("Send a custom message", True, (0,0,0))
  text_rect = text_6.get_rect(center=(SCREEN_WIDTH/2, 300))
  screen.blit(text_6, text_rect)

  suggestion_button.draw()
  custom_button.draw()

running = True
while running:
  screen.fill((255,255,255))

  if home:
    home_screen(username)

  if receiving:
    home = False
    receive_call(contact_name)

  if show_message:
    message(contact_name)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()

      if accept_button.rect.collidepoint(pos) and receiving:
        print("accept")

      if decline_button.rect.collidepoint(pos) and receiving:
        receiving = False
        home = True

      if message_button.rect.collidepoint(pos) and receiving:
        receiving = False
        show_message = True

  pygame.display.update()

pygame.quit()