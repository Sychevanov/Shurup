import pygame

pygame.init()
display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('name_game')

#icon = pygame.image.load('icon.png')

usr_width = 60
usr_height = 160
usr_x = 400
usr_y = 300

fps = pygame.time.Clock()

def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((255,255,255))
        pygame.draw.rect(display,(145,45,78),(usr_x,usr_y,usr_width,usr_height))
        pygame.display.update()
        fps.tick(60)

run_game()