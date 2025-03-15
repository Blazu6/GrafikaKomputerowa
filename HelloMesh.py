import pygame
from Mesh3D import *  # Importujemy naszą klasę Mesh3D z pliku Mesh3D.py
from pygame.locals import *
from OpenGL.GLU import *

pygame.init()  # Inicjujemy moduły Pygame

screen_width = 500
screen_height = 500
# Tworzymy okno 500×500 z trybem OpenGL i podwójnym buforowaniem
screen = pygame.display.set_mode((screen_width,
                                  screen_height),
                                  DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
# Ustawienie macierzy projekcji (perspektywa)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(60, screen_width / screen_height, 0.1, 100.0)  # Zmiana FOV na 60 stopni
glMatrixMode(GL_MODELVIEW)
glEnable(GL_DEPTH_TEST)  # Włączenie testu głębi (potrzebne do poprawnego rysowania 3D)
done = False
white = pygame.Color(255, 255, 255)

mesh = Cube()  # Tworzymy obiekt siatki (mesh)

# Pętla główna aplikacji
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Wyjście z pętli, gdy zamykamy okno

    # Czyścimy bufor koloru i bufor głębi
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -3.0)  # Odsunięcie obiektu od kamery (zamiast -3.0)
    glRotatef(pygame.time.get_ticks() * 0.05, 1, 1, 0)  # Animacja obrotu w czasie
    mesh.draw()  # Wywołujemy metodę rysującą model

    pygame.display.flip()  # Prezentujemy nowo narysowaną klatkę

pygame.quit()  # Sprzątanie i zakończenie programu