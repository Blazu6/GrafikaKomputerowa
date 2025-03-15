**Wprowadzenie do Grafiki Komputerowej z PyOpenGL**
---
### **1. Wprowadzenie teoretyczne**

#### **1.1 Pipeline graficzny OpenGL**
Graficzny potok przetwarzania (ang. pipeline) w OpenGL składa się z kilku etapów:
- **Transformacja modelu** – przekształcenie współrzędnych obiektu względem kamery.
- **Projekcja** – rzutowanie sceny na ekran (perspektywiczne lub ortogonalne).
- **Clipping** – usuwanie niewidocznych elementów.
- **Rasteryzacja** – konwersja współrzędnych świata na piksele.
- **Wyświetlanie** – rendering obrazu na ekranie.

Każdy z tych etapów jest niezbędny do prawidłowego renderowania obrazu. Transformacja modelu pozwala na określenie pozycji obiektu w przestrzeni 3D. Projekcja definiuje, jak obiekt zostanie odwzorowany na dwuwymiarowym ekranie. Clipping usuwa elementy, które nie powinny być widoczne, a rasteryzacja zamienia współrzędne geometryczne na odpowiednie piksele.

#### **1.2 Współrzędne 3D i kamery**
OpenGL stosuje system współrzędnych prawoskrętnych. Pozycjonowanie obiektów względem kamery odbywa się przez odpowiednie transformacje macierzowe (przesunięcia, rotacje, skalowania). Kamera w OpenGL jest wirtualnym punktem widzenia, który określa sposób postrzegania sceny. Możemy stosować dwa podstawowe rodzaje rzutowania:
- **Rzutowanie perspektywiczne** – odwzorowanie świata w sposób zbliżony do ludzkiego oka (obiekty dalsze wydają się mniejsze).
- **Rzutowanie ortogonalne** – brak perspektywy, wszystkie obiekty mają ten sam rozmiar niezależnie od odległości.

#### **1.3 Modele 3D i siatki (mesh)**
Obiekty 3D są reprezentowane jako zbiór wierzchołków połączonych w trójkąty. Struktura ta nazywana jest **siatką** (ang. mesh) i zawiera informację o:
- **wierzchołkach** – określających położenie punktów w przestrzeni,
- **indeksach trójkątów** – wskazujących, które wierzchołki tworzą powierzchnię.

Siatki trójkątów są powszechnie stosowane w grafice komputerowej, ponieważ trójkąty są najmniejszymi wielokątami, które zawsze leżą w jednej płaszczyźnie. Dzięki temu renderowanie trójkątów jest efektywne i pozwala na tworzenie skomplikowanych modeli.

---

### **2. Instalacja i konfiguracja środowiska**

1. **Utwórz nowy folder** np. Lab02a
2. **Zainstaluj biblioteki** PyOpenGL oraz Pygame:
   ```sh
   pip install PyOpenGL PyOpenGL_accelerate pygame
   ```
3. **Utwórz plik `OpenGLStarter.py`** i wykorzystaj poniższy kod:
   ```python
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
   ```
   - Ten skrypt tworzy okno wielkości 500×500, inicjalizuje Pygame i OpenGL oraz w pętli głównej czyści ekran i wyświetla efekt w oknie.
   - `pygame.display.flip()` dokonuje zamiany bufora tylnego z przednim, co aktualizuje zawartość okna.

4. **Uruchom skrypt** i sprawdź, czy wyświetla się puste okno.

---

### **3. Tworzenie i renderowanie modeli 3D**

#### **3.1 Definiowanie modelu 3D**
Kolejnym krokiem jest utworzenie modelu 3D w postaci siatki (mesh) W tym celu stwórz nowy plik o nazwie `Mesh3D.py` i wykorzystaj poniższy kod:
   ```python
   from OpenGL.GL import *  # Import funkcji z OpenGL (m.in. do rysowania)

   class Mesh3D:
      def __init__(self):
          # Definiujemy listę wierzchołków (x, y, z)
          self.vertices = [(0.5, -0.5, 0.5),
                          (-0.5, -0.5, 0.5),
                          (0.5, 0.5, 0.5),
                          (-0.5, 0.5, 0.5)]
          # Definiujemy indeksy określające, które wierzchołki tworzą trójkąty
          self.triangles = [0, 2, 3, 0, 3, 1]

      def draw(self):
          # Rysujemy trójkąty w pętli, po 3 indeksy na każdy trójkąt
          for t in range(0, len(self.triangles), 3):
              glBegin(GL_LINE_LOOP)  # Rozpoczynamy rysowanie obwiedni trójkąta

              # Przekazujemy do OpenGL współrzędne każdego z wierzchołków
              glVertex3fv(self.vertices[self.triangles[t]])
              glVertex3fv(self.vertices[self.triangles[t + 1]])
              glVertex3fv(self.vertices[self.triangles[t + 2]])

              glEnd()  # Kończymy rysowanie aktualnego trójkąta
   ```
   **Omówienie kodu:**
   - `self.vertices` – zawiera współrzędne 6 wierzchołków.
   - `self.triangles` – opisuje dwa trójkąty (w sumie 6 indeksów), łączące wybrane wierzchołki.
   - `glBegin(GL_LINE_LOOP)` – rysuje trójkąt jako obwiednię linii (siatkę).
   - `glVertex3fv(...)` – przekazuje kolejne wierzchołki danego trójkąta do OpenGL.
   - `glEnd()` – kończy rysowanie aktualnego prymitywu.

        **Zastanów się, względem jakiego punktu są definiowane współrzędne wierzchołków?**

#### **3.2 Łączenie wszystkiego w pliku `HelloMesh.py`**
Aby wyświetlić nasz model 3D w nowo utworzonym oknie, tworzymy plik `HelloMesh.py` z kodem:
   ```python
   import pygame
   from Mesh3D import *  # Importujemy naszą klasę Mesh3D z pliku Mesh3D.py
   from pygame.locals import *

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

   mesh = Mesh3D()  # Tworzymy obiekt siatki (mesh)

   # Pętla główna aplikacji
   while not done:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               done = True  # Wyjście z pętli, gdy zamykamy okno

       # Czyścimy bufor koloru i bufor głębi
       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

       mesh.draw()  # Wywołujemy metodę rysującą model

       pygame.display.flip()  # Prezentujemy nowo narysowaną klatkę

   pygame.quit()  # Sprzątanie i zakończenie programu
   ```
   **Omówienie kodu:**
   - Jest to praktycznie ten samo kod jak w `OpenGLStarter.py`, tworzymy okno i inicjalizujemy Pygame. W kolejnych ćwiczeniach będziemy na nim bazować.
   - `mesh = Mesh3D()` – tworzymy obiekt siatki zdefiniowanej w pliku `Mesh3D.py`.
   - `mesh.draw()` – wywołuje rysowanie obiektu w pętli głównej.

Po uruchomieniu `HelloMesh.py` powinniśmy zobaczyć zarys (siatkę) kwadratu (złożonego z dwóch trójkątów), narysowanego na ekranie.

---

### **4. Konfiguracja kamery i transformacji**

Poniżej przedstawiono szczegółowe instrukcje dotyczące użycia funkcji odpowiedzialnych za konfigurację widoku (kamery) i transformacje sceny 3D. Wszystkie kroki wykonaj w pliku `HelloMesh.py`:

1. **Import funkcji z biblioteki GLU** (jeśli jeszcze nie ma):
   ```python
   from OpenGL.GLU import *
   ```
   Biblioteka GLU (OpenGL Utility Library) udostępnia m.in. funkcje `gluPerspective` i inne narzędzia upraszczające ustawienia kamery.

2. **Ustawienie rzutowania** – do wyboru są dwa główne style:
   - **Rzutowanie perspektywiczne** (`gluPerspective`):
     ```python
     gluPerspective(45, screen_width / screen_height, 0.1, 100.0)
     ```
     **Parametry:**
     - `45` – kąt widzenia (FOV) w stopniach. Im wyższy kąt, tym większe „rozszerzenie” perspektywy.
     - `screen_width / screen_height` – współczynnik proporcji, dostosowany do wymiarów okna.
     - `0.1` – minimalna odległość rysowania (near plane), obiekty bliższe niż 0.1 nie będą renderowane.
     - `100.0` – maksymalna odległość rysowania (far plane), obiekty dalsze niż 100.0 nie będą renderowane.
     
     Dzięki perspektywie obiekty bardziej oddalone wydają się mniejsze – tak jak w rzeczywistości.

   - **Rzutowanie ortogonalne** (`glOrtho`):
     ```python
     glOrtho(-1, 1, 1, -1, 0.1, 50.0)
     ```
     **Parametry:**
     - `-1` i `1` – lewa oraz prawa krawędź frustum (obszaru widzenia),
     - `1` i `-1` – górna i dolna krawędź (uwaga, kolejność zależy od układu współrzędnych),
     - `0.1` – minimalna odległość rysowania (near plane),
     - `50.0` – maksymalna odległość rysowania (far plane).
     
     W tym trybie obiekty nie zmniejszają się wraz z oddalaniem, co przydaje się w rysunku technicznym lub interfejsach 2D.

3. **Przesunięcie obiektu (sceny) w osi Z**:
   ```python
   glTranslatef(0.0, 0.0, -3)
   ```
   - `glTranslatef(x, y, z)` – przesuwa rysowany układ współrzędnych o wektor (x, y, z).
   - Tu: `z = -3` oznacza odsunięcie obiektu w głąb ekranu tak, aby stał się widoczny.

4. **Rotacja obiektu** (opcjonalnie):
   ```python
   glRotatef(1, 1, 0, 1)
   ```
   - `glRotatef(angle, x, y, z)` – obraca obiekt o wartość `angle` (w stopniach) wokół wektora (x, y, z).

    **Zastanów się, w którym miejscu kodu umieścisz wywołania przedstawionych funkcji. Wykorzystaj funkcję `pygame.time.wait(100)` aby spowolnić obrót obiektu. Kwestie odmierzania czasu poruszymy w przyszłości.**

5. **Uruchom skrypt** i obserwuj zmiany:
   - Modyfikuj parametry `gluPerspective` lub `glOrtho` (np. zmień FOV z 45 na 60),
   - Eksperymentuj z wartościami w `glTranslatef` (np. z=-5 zamiast -3), sprawdź inne wartości przesunięcia dla x i y,
   - Dodaj lub usuń `glRotatef`, by sprawdzić, jak wygląda statyczny oraz animowany obiekt.


### **5. Zadanie do samodzielnej realizacji**

Zdefiniuj pełny sześcian. Potrzebne będzie zdefiniowanie 8 wierzchołków (po jednym w każdym rogu sześcianu) oraz zorganizowanie ich w postaci 12 trójkątów (po 2 na każdą ze ścian). Aby wyświetlić sześcian zamień `mesh = Mesh3D()` na `mesh = Cube()`.

   **Wskazówka:**
   - Najlepiej utwórz nową klasę dziedzicząc po klasie Mesh3D, np. `class Cube(Mesh3D):`, i w jej konstruktorze (`__init__`) ustaw `self.vertices` i `self.triangles` odpowiednio dla sześcianu. Metoda `draw()` pozostaje bez zmian. Klasę możesz utworzyć w nowym pliku o nazwie `Cube.py`(pamiętaj o imporcie) lub poniżej definicji klasy `Mesh3D`.
   - Spróbuj zdefiniować sześcian rozciągający się od punktu `(-0.5, -0.5, -0.5)` do `(0.5, 0.5, 0.5)`. Otrzymasz w ten sposób 8 wierzchołków (każdy narożnik sześcianu).
   - Następnie podziel jego ściany na pary trójkątów (każda ściana to 4 wierzchołki, co daje 2 trójkąty na ścianę, a w sumie 6 ścian).

