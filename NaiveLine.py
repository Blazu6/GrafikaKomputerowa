import pygame
import math

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)

# Parametry linii
m = 2   # nachylenie
c = 200   # wyraz wolny

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Rysowanie linii metodą naiwną: dla każdego x oblicz y = m*x + c
    for x in range(screen_width):
        y = int(m * x + c)
        if 0 <= y < screen_height:
            screen.set_at((x, y), white)
    pygame.display.update()
pygame.quit()