import sys
import pygame


pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))

while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()