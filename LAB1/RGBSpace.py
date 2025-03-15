import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y in range(screen_height):
        for x in range(screen_width):
            color = pygame.Color(0, int(x / screen_width * 255),
                                 int(y / screen_height * 255))
            screen.set_at((x, y), color)
    pygame.display.update()
pygame.quit()