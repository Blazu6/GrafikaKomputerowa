import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Porównanie linii: line vs aaline")

done = False
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
bg_color = pygame.Color(30, 30, 30)  # ciemne tło, by lepiej widać było linie

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg_color)

    # Zwykła linia (czerwona)
    pygame.draw.line(screen, red, (100, 100), (900, 700), 1)

    # Linia z antyaliasingiem (biała)
    pygame.draw.aaline(screen, white, (100, 200), (900, 800))

    pygame.display.update()

pygame.quit()
