import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

# Załaduj obraz – upewnij się, że plik "obraz.png" znajduje się w katalogu projektu
image = pygame.image.load('obraz.png')

# Opcjonalnie: zmień rozmiar obrazu, jeśli jest za duży lub za mały
image = pygame.transform.scale(image, (400, 300))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(pygame.Color(0, 0, 0))
    # Wyświetl obraz w pozycji (200, 150)
    screen.blit(image, (200, 150))
    pygame.display.update()
pygame.quit()