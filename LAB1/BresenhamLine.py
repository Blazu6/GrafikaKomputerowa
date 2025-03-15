import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)

# Funkcja implementująca algorytm Bresenhama dla linii o nachyleniu m < 1
def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return points

# Przykładowe punkty końcowe linii
x0, y0 = 100, 150
x1, y1 = 800, 600

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for point in bresenham_line(x0, y0, x1, y1):
        screen.set_at(point, white)
    pygame.display.update()
pygame.quit()