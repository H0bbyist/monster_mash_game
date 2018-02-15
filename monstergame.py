import pygame
import random


class Monster:
  def __init__(self):
    self.x = 100
    self.y = 100
    self.counter = 0
    self.xdirection = 1
    self.ydirection = 1
    self.image = pygame.image.load("monster_game_tools/images/monster.png")

class Hero:
  def __init__(self):
    self.x = 240
    self.y = 190
    self.counter = 0
    self.direction = 0
    self.image = pygame.image.load("monster_game_tools/images/hero.png")

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
    blue_color = (97, 159, 182)
    
  

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    bg = pygame.image.load("monster_game_tools/images/background.png")
    
    # Game initialization

    m.counter = 0

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        m.counter += 1
        if m.counter > 60:
          m.xdirection = random.randint(1, 3)
          m.ydirection = random.randint(1, 3)
          m.counter = 0
        
        if m.xdirection == 1:
          m.x += 5
        elif m.xdirection == 2:
          m.x -= 5
        else:
          m.x += 0
        if m.ydirection == 1:
          m.y += 5
        elif m.ydirection == 2:
          m.y -= 5
        else:
          m.y += 0
      
          

        if m.x > 512:
          m.x = 0
        if m.x < 0:
          m.x = 512
        if m.y > 480:
          m.y = 0
        if m.y < 0:
          m.y = 480
        

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








