import pygame



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
    h = pygame.image.load("monster_game_tools/images/hero.png")
    m = pygame.image.load("monster_game_tools/images/monster.png")
    g = pygame.image.load("monster_game_tools/images/goblin.png")
    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        
        # Draw background
        screen.fill(white_color)
        screen.blit(bg, (0, 0))
        screen.blit(h, (240, 190))
        screen.blit(m, (100, 100))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()







