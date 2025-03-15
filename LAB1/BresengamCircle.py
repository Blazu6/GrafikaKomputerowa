import pygame

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)

def bresenham_circle(cx, cy, r):
    points = []
    x = 0
    y = r
    d = 3 - 2 * r
    while y >= x:
        # Odbicie względem osi – osiem symetrycznych punktów
        points.extend([
            (cx + x, cy + y), (cx - x, cy + y),
            (cx + x, cy - y), (cx - x, cy - y),
            (cx + y, cy + x), (cx - y, cy + x),
            (cx + y, cy - x), (cx - y, cy - x)
        ])
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1
    return points

# Parametry okręgu: środek (300,300) i promień 200
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for point in bresenham_circle(300, 300, 200):
        screen.set_at(point, white)
    pygame.display.update()
pygame.quit()