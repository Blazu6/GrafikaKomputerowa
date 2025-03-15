import pygame

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    position = (100, 100)
    
    #O
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 100))
    pygame.draw.rect(screen, white, (position[0], position[1], 60, 10))
    pygame.draw.rect(screen, white, (160, 100, 10, 100))
    pygame.draw.rect(screen, white, (100, 200, 70, 10))

    #B
    pygame.draw.rect(screen, white, (200, 100, 10, 100)) 
    pygame.draw.rect(screen, white, (200, 100, 60, 10))  
    pygame.draw.rect(screen, white, (200, 150, 60, 10))  
    pygame.draw.rect(screen, white, (200, 200, 60, 10))
    pygame.draw.rect(screen, white, (260, 110, 10, 90)) 
    pygame.display.update()
pygame.quit()