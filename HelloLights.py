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
done = False
white = pygame.Color(255, 255, 255)

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

glMatrixMode(GL_MODELVIEW)

glEnable(GL_DEPTH_TEST)  # bufor głębi – odrzucanie fragmentów zasłoniętych
glEnable(GL_LIGHTING)  # włączenie obsługi oświetlenia

glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT,  (0, 1, 0, 1))  # np. fioletowe ambient
glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1, 1, 0, 1))  # np. żółte diffuse
glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))  # np. zielone specular

glLightfv(GL_LIGHT1, GL_POSITION, (-5, -5, 0))  # Przeciwny róg sceny
glLightfv(GL_LIGHT1, GL_AMBIENT,  (0, 0, 1, 1))  # Niebieskie ambient
glLightfv(GL_LIGHT1, GL_DIFFUSE,  (1, 0, 0, 1))  # Czerwone diffuse
glLightfv(GL_LIGHT1, GL_SPECULAR, (1, 1, 1, 1))  # Białe specular
glEnable(GL_LIGHT1)  # Włącz drugie światło

glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 0, 0, 1))

mesh = Cube(GL_POLYGON, "brick")

# Pętla główna aplikacji
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Wyjście z pętli, gdy zamykamy okno

    # Czyścimy bufor koloru i bufor głębi
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -3.0)  # Odsunięcie obiektu od kamery
    glRotatef(pygame.time.get_ticks() * 0.05, 1, 1, 0)  # Animacja obrotu w czasie
    mesh.draw()  # Wywołujemy metodę rysującą model

    pygame.display.flip()  # Prezentujemy nowo narysowaną klatkę

pygame.quit()  # Sprzątanie i zakończenie programu