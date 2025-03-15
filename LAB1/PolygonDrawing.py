import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(pygame.Color(0, 0, 0))
    
    # Rysowanie wypełnionego trójkąta
    triangle_points = [(400, 100), (300, 300), (500, 300)]
    pygame.draw.polygon(screen, white, triangle_points, 0)
    
    # Rysowanie wypełnionego kwadratu
    square_points = [(150, 400), (150, 550), (300, 550), (300, 400)]
    pygame.draw.polygon(screen, blue, square_points, 0)
    
    pygame.display.update()
pygame.quit()