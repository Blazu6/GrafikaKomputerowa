import pygame
from pygame.locals import *  # Import stałych (m.in. do trybu okna)
from OpenGL.GL import *      # Główna biblioteka OpenGL

pygame.init()  # Inicjalizacja modułów Pygame

screen_width = 500
screen_height = 500
# Tworzymy okno o rozmiarze 500×500, z włączonym podwójnym buforowaniem
# (DOUBLEBUF) i wsparciem dla OpenGL (OPENGL)
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)

pygame.display.set_caption('OpenGL in Python')  # Ustawiamy tytuł okna
done = False
white = pygame.Color(255, 255, 255)  # Definicja koloru (białego) - może się przydać

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Wciśnięcie "X" zamyka program
            done = True

    # Czyścimy ekran (bufor koloru i bufor głębi)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Zamiana bufora tylnego z buforem przednim, aby wyświetlić zawartość okna
    pygame.display.flip()

pygame.quit()  # Po wyjściu z pętli kończymy działanie programu