import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Monster:
  def __init__(self):
    self.x = 100
    self.y = 100
    self.counter = 0
    self.xdirection = 2
    self.ydirection = 1
    self.image = pygame.image.load("monster_game_tools/images/monster.png")

  def move(self):
    self.counter += 1
    if self.counter > 60:
      self.xdirection = random.randint(1, 3)
      self.ydirection = random.randint(1, 3)
      self.counter = 0
    
    if self.xdirection == 1:
      self.x += 5
    elif self.xdirection == 2:
      self.x -= 5
    else:
      self.x += 0
    if self.ydirection == 1:
      self.y += 5
    elif self.ydirection == 2:
      self.y -= 5
    else:
      self.y += 0
    if self.x > 512:
      self.x = 0
    if self.x < 0:
      self.x = 512
    if self.y > 480:
      self.y = 0
    if self.y < 0:
      self.y = 480
    

class Hero:
  def __init__(self):
    self.x = 240
    self.y = 190
    self.counter = 0
    self.image = pygame.image.load("monster_game_tools/images/hero.png")

  def move(self):
    self.x += x
    self.y += y
      
     
class Goblin:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.counter = 0
    self.direction = 0
    self.image = pygame.image.load("monster_game_tools/images/goblin.png")


def main():
    width = 512                     #image size 512 X 480px
    height = 480
    white_color = (255, 255, 255)
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Monster Mash!')
    clock = pygame.time.Clock()
    bg = pygame.image.load("monster_game_tools/images/background.png")
  
    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == KEY_UP:
                  
              elif event.key == KEY_DOWN:
                  
              elif event.key == KEY_LEFT:
                  
              elif event.key == KEY_RIGHT:
                  




            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        m.move()
        h.move()
      

        # Draw background
        screen.fill(white_color)
        screen.blit(bg, (0, 0))
        screen.blit(h.image, (h.x, h.y))
        screen.blit(m.image, (m.x, m.y))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    h = Hero()
    m = Monster()
    g = Goblin()
    main()








