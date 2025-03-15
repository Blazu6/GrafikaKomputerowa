from OpenGL.GL import *  # Import funkcji z OpenGL (m.in. do rysowania)
import pygame

class Mesh3D:
    def __init__(self):
        # Definiujemy listę wierzchołków (x, y, z)
        self.vertices = [(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5)]
        # Definiujemy indeksy określające, które wierzchołki tworzą trójkąty
        self.triangles = [0, 2, 3, 0, 3, 1]

        self.draw_type = GL_LINE_LOOP
        self.texture   = None
        self.texID     = 0

    def init_texture(self):
        self.texID = glGenTextures(1)

        textureData = pygame.image.tobytes(self.texture, 'RGB', 1)
        width  = self.texture.get_width()
        height = self.texture.get_height()

        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) #mipmapping
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0,
                    GL_RGB, GL_UNSIGNED_BYTE, textureData)

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texID)

        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)

            glTexCoord2fv(self.uvs[t])
            glVertex3fv(self.vertices[self.triangles[t]])

            glTexCoord2fv(self.uvs[t+1])
            glVertex3fv(self.vertices[self.triangles[t+1]])

            glTexCoord2fv(self.uvs[t+2])
            glVertex3fv(self.vertices[self.triangles[t+2]])

            glEnd()
            
class Cube(Mesh3D):
    def __init__(self, draw_type, filename):

        # Nadpisujemy wierzchołki, dodając pełny sześcian (8 punktów)
        self.vertices = [
            (0.5, -0.5, 0.5),   # 0
            (-0.5, -0.5, 0.5),  # 1
            (0.5, 0.5, 0.5),    # 2
            (-0.5, 0.5, 0.5),   # 3
            (0.5, -0.5, -0.5),  # 4
            (-0.5, -0.5, -0.5), # 5
            (0.5, 0.5, -0.5),   # 6
            (-0.5, 0.5, -0.5)   # 7
        ]

            # Front (indeksy: 0,2,3, 0,3,1)
        self.uvs = [(1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
            (1.0, 0.0), (0.0, 1.0), (0.0, 0.0),
            # Back (indeksy: 4,6,7, 4,7,5)
            (0.0, 0.0), (0.0, 1.0), (1.0, 1.0),
            (0.0, 0.0), (1.0, 1.0), (1.0, 0.0),
            # Left (indeksy: 1,5,3, 3,5,7)
            (0.0, 0.0), (1.0, 0.0), (0.0, 1.0),
            (0.0, 1.0), (1.0, 0.0), (1.0, 1.0),
            # Right (indeksy: 0,2,4, 2,4,6)
            (1.0, 0.0), (1.0, 1.0), (0.0, 0.0),
            (1.0, 1.0), (0.0, 0.0), (0.0, 1.0),
            # Up (indeksy: 2,3,7, 2,6,7)
            (1.0, 0.0), (0.0, 0.0), (0.0, 1.0),
            (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
            # Down (indeksy: 0,1,5, 0,4,5)
            (1.0, 1.0), (0.0, 1.0), (0.0, 0.0),
            (1.0, 1.0), (1.0, 0.0), (0.0, 0.0) ]

        # Definiujemy 12 trójkątów (2 na każdą ścianę)
        self.triangles = [
            0, 2, 3,  0, 3, 1,  # Przednia ściana
            4, 6, 7,  4, 7, 5,  # Tylna ściana
            1, 5, 3,  3, 5, 7,  # Lewa ściana
            0, 2, 4,  2, 4, 6,  # Prawa ściana
            2, 3, 7,  2, 6, 7,  # Górna ściana
            0, 1, 5,  0, 4, 5   # Dolna ściana
        ]

        Mesh3D.texture = pygame.image.load(filename)
        Mesh3D.draw_type = draw_type
        Mesh3D.init_texture(self)
