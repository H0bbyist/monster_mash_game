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
      self.x += 4
    elif self.xdirection == 2:
      self.x -= 4
    else:
      self.x += 0
    if self.ydirection == 1:
      self.y += 4
    elif self.ydirection == 2:
      self.y -= 4
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

  def alive(self):
    if h.x + 32 < m.x:
      return True
    if m.x + 32 < h.x:
      return True
    if h.y + 32 < m.y:
      return True
    if m.y + 32 < h.y:
      return True
    else:
      return False
  
    
class Hero:
  def __init__(self,x, y):
    self.x = 240
    self.y = 190
    self.xdir = x
    self.ydir = y
    self.image = pygame.image.load("monster_game_tools/images/hero.png")

  def move(self):
    self.x += self.xdir
    self.y += self.ydir
    if self.x > 455:
      self.x = 455
    elif self.x < 25:
      self.x = 25
    if self.y > 415:
      self.y = 415
    elif self.y < 10:
      self.y = 10
  
  def alive(self):
      if g1.x + 32 < h.x:
        return True
      elif h.x + 32 < g1.x:
        return True
      elif g1.y + 32 < h.y:
        return True
      elif h.y + 32 < g1.y:
        return True
      else:
        return False

         
class Goblin:
  def __init__(self):
    self.x = random.randint(1, 500)
    self.y = random.randint(1, 500)
    self.counter = 0
    self.xdirection = 2
    self.ydirection = 1
    self.image = pygame.image.load("monster_game_tools/images/goblin.png")

  def move(self):
    self.counter += 1
    if self.counter > 180:
      self.xdirection = random.randint(1, 3)
      self.ydirection = random.randint(1, 3)
      self.counter = 0
    
    if self.xdirection == 1:
      self.x += 2
    elif self.xdirection == 2:
      self.x -= 2
    else:
      self.x += 0
    if self.ydirection == 1:
      self.y += 2
    elif self.ydirection == 2:
      self.y -= 2
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


class Win:
  def sequence(self):
    pygame.mixer.music.load("monster_game_tools/sounds/win.wav")
    pygame.mixer.music.play(0)
  
    
class Lose:
  def sequence(self):
    pygame.mixer.music.load("monster_game_tools/sounds/lose.wav")
    pygame.mixer.music.play(0)
    


def main():
    width = 512                     #image size 512 X 480px
    height = 480
    white_color = (255, 255, 255)
    
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Monster Mash!')
    clock = pygame.time.Clock()
    bg = pygame.image.load("monster_game_tools/images/background.png")

    herdead = False
    monsdead = False
    myfont = pygame.font.SysFont("", 50)
    winstatement = myfont.render('You Killed the Monster!', False, (0, 0, 0))
    losestatement = myfont.render("The Goblin Killed You!", False, (0, 0, 0))
    playagain = myfont.render("Play Again? Press Enter", False, (0, 0, 0))
    pygame.mixer.music.load("monster_game_tools/sounds/music.wav")
    pygame.mixer.music.play(-1)
    
    
    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == KEY_UP:
                  h.xdir = 0
                  h.ydir = -3
              elif event.key == KEY_DOWN:
                  h.xdir = 0
                  h.ydir = 3
              elif event.key == KEY_LEFT:
                  h.xdir = -3
                  h.ydir = 0
              elif event.key == KEY_RIGHT:
                  h.xdir = 3
                  h.ydir = 0


            if not m.alive():
              w.sequence()
              monsdead = True

            if not h.alive():
              l.sequence()
              herdead = True
            
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RETURN:
                monsdead = False
                herdead = False
                pygame.mixer.music.load("monster_game_tools/sounds/music.wav")
                pygame.mixer.music.play(-1)

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        m.move()
        h.move()
        g1.move()
        

        # Draw background
        
        screen.blit(bg, (0, 0))
        
        screen.blit(g1.image, (g1.x, g1.y))
        screen.blit(g1.image, (g1.x, g1.y))
        
        
        if herdead == False:
          screen.blit(h.image, (h.x, h.y))
        else:
          screen.blit(losestatement, (50,200))
          screen.blit(playagain, (50,230))
        if monsdead == False:
          screen.blit(m.image, (m.x, m.y))
        else:
          screen.blit(winstatement, (50,200))
          screen.blit(playagain, (50, 230))
        
       
        

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    h = Hero(0,0)
    m = Monster()
    g1 = Goblin()
    
    w = Win()
    l = Lose()
    main()








