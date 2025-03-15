import pygame

pygame.init()
screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)
pygame.font.init()

# Użycie systemowej czcionki Comic Sans MS
font_path = "fonts/Czcionka.otf"
font = pygame.font.SysFont('Comic Sans MS', 60, False, True)
text = font.render('graphic design is my passion', False, white)
font_path = "fonts/Czcionka.otf"
myFont = pygame.font.Font(font_path, 60)
myText = myFont.render('in Paris', False, white)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(text, (10, 10))
    screen.blit(myText, (10, 120))
    pygame.display.update()
pygame.quit()