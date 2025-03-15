# **Oświetlenie i Teksturowanie w PyOpenGL**
---
## **1. Wprowadzenie teoretyczne**

W grafice 3D, aby obiekt wyglądał realistycznie i trójwymiarowo, istotne są dwie rzeczy:
1. **Oświetlenie (Lighting)** – w OpenGL wyróżniamy trzy składowe światła:
   - **Ambient** – światło otoczenia, jednolite i bezkierunkowe, które oświetla scenę w minimalnym stopniu.
   - **Diffuse** – światło rozproszone, zależne od kąta padania; najlepiej widać je na ścianach zwróconych w stronę źródła.
   - **Specular** – światło odbite, tworzące na powierzchni połyski (refleksy).

   Dodatkowo można ustawić **pozycję** źródła światła (np. (x, y, z)) oraz wartości kolorów (RGB) każdej składowej. Obiekty w scenie reagują na światło poprzez tzw. **materiały**, które określają m.in. kolor diffuse obiektu, składową specular (dla połysku) itp.

2. **Teksturowanie** – nakładanie obrazu (np. pliku .png, .jpg, .tif) na siatkę 3D. Każdy wierzchołek modelu otrzymuje współrzędne (u, v) w zakresie [0..1], określające fragment tekstury przypisany do danej części modelu - **mapowanie UV**.

Realistyczna scena najczęściej wykorzystuje oba elementy: **światło** podkreśla kształt, a **tekstura** nadaje detale powierzchni.

---
## **2. Przygotowanie projektu**
1. **Nowy folder**: Utwórz folder np. `Lab02b` i **skopiuj** do niego pliki z poprzednich ćwiczeń (np. `HelloMesh.py`, `Mesh3D.py`, `Cube.py`).
2. **Instalacja bibliotek**: Upewnij się, że masz w środowisku Python:
   ```bash
   pip install PyOpenGL PyOpenGL_accelerate pygame
   ```
3. **Plik tekstury**: Jeżeli chcesz nakładać teksturę, przygotuj plik graficzny (np. `brick.png`, 512×512) i umieść go w folderze. Zapamiętaj ścieżkę, np. `images/brick.tif`.

---
## **3. Zmiana trybu rysowania na wypełnione ściany**

1. **Otwórz** plik `Mesh3D.py` i zlokalizuj miejsce, gdzie rysujesz trójkąty metodą `glBegin(...)`.
2. **Zamień** w nim `GL_LINE_LOOP` na:
   ```python
   glBegin(GL_POLYGON)
   ```
   To sprawi, że trójkąty będą wypełnione kolorem zamiast rysowanych samych krawędzi.
3. **Uruchom** (opcjonalnie) poprzedni skrypt `HelloMesh.py`, by sprawdzić, czy widać różnicę – sześcian powinien być wypełniony.

---
## **4. Tworzenie `HelloLights.py` i konfiguracja kamery**

1. **Utwórz** nowy plik `HelloLights.py` i **skopiuj** do niego kod z `HelloMesh.py` (zachowując logikę tworzenia okna, rotacji sześcianu, pętli głównej).
2. **Dodaj** zaraz po utworzeniu okna:
   ```python
   from OpenGL.GL import *
   from OpenGL.GLU import *
   ...
   done = False
   white = pygame.Color(255, 255, 255)

   glMatrixMode(GL_PROJECTION)
   gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

   glMatrixMode(GL_MODELVIEW)
   glTranslatef(0.0, 0.0, -3)

   glEnable(GL_DEPTH_TEST)  # bufor głębi – odrzucanie fragmentów zasłoniętych
   ```
   - `gluPerspective(60, ratio, 0.1, 100.0)` ustawia pole widzenia 60° i płaszczyzny near/far.
   - `glMatrixMode(GL_MODELVIEW)` oznacza, że kolejne operacje (np. `glTranslatef`) będą dotyczyć przesunięcia/obrotu sceny.
   - `glEnable(GL_DEPTH_TEST)` włącza mechanizm, dzięki któremu obiekty niewidoczne (za innymi) nie są nadpisywane.

---
## **5. Dodawanie oświetlenia**

### 5.1 Włączenie trybu oświetlenia
1. **Aktywuj** światło w OpenGL:
   ```python
   glEnable(GL_LIGHTING)  # włączenie obsługi oświetlenia
   ```
2. **Ustaw** pozycję światła (np. GL_LIGHT0) i je włącz:
   ```python
   glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
   glEnable(GL_LIGHT0)
   ```
   - `(5, 5, 5, 1)` oznacza, że światło jest w punkcie (5,5,5) w przestrzeni świata (1 to współczynnik pozycji).
3. **Uruchom** aplikację – sześcian może być jednak słabo widoczny (szary), bo nie ma jeszcze koloru światła.

### 5.2 Ustawienie kolorów (ambient, diffuse, specular)
1. Aby zdefiniować barwy światła:
   ```python
   glLightfv(GL_LIGHT0, GL_AMBIENT,  (1, 0, 1, 1))  # np. fioletowe ambient
   glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1, 1, 0, 1))  # np. żółte diffuse
   glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))  # np. zielone specular
   ```
   Każda składowa to (R, G, B, A) ∈ [0..1].
2. **Zapisz i uruchom** ponownie – zobaczysz różnokolorowe oświetlenie, lecz bryła może być dalej mało wyraźna.

### 5.3 Materiał obiektu
1. Aby bryła reagowała na światło, ustaw jej materiał, np.:
   ```python
   glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1))
   ```
   co oznacza, że obiekt ma zieloną składową diffuse. Przy białym świetle objawi się to kolorem zielonym.
2. **Zmień** np. diffuse światła na (1,0,0,1) (czerwone) i sprawdź, jak odbija się ono od zielonej powierzchni – może stać się ciemna.
3. **Eksperymentuj** z różnymi wartościami ambient/diffuse światła i kolorem materiału obiektu.

### 5.4 Test aplikacji
- **Uruchom** `HelloLights.py` ponownie.
- **Obserwuj** efekty przy rotacji obiektu (np. jeśli w pętli głównej masz `glRotatef(5, 1, 0, 1)`).
- Możesz dodać drugie źródło światła (GL_LIGHT1) i ustawić mu inny kolor.

---
## **6. Dodawanie tekstury**

### 6.1 Przygotowanie pliku
1. Umieść obraz (np. `brick.tif`) w folderze i zapamiętaj ścieżkę, np. `"images/brick.tif"`. Dowolny obraz tekstury znajdź w sieci.
### 6.2 Modyfikacja `Mesh3D`
1. **Dodaj** pola:
   ```python
   self.triangles = [0,2,3,0,3,1]
   self.draw_type = GL_LINE_LOOP
   self.texture   = None
   self.texID     = 0
   ```
2. **Stwórz** metodę `init_texture`:
   ```python
    def init_texture(self):
        self.texID = glGenTextures(1)

        textureData = pygame.image.tobytes(self.texture, 'RGB', 1)
        width  = self.texture.get_width()
        height = self.texture.get_height()

        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) #mipmapping
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, textureData)
   ```
   - `glGenTextures(1)` – tworzy 1 identyfikator tekstury.
   - `pygame.image.tobytes(...)` konwertuje obraz do danych bajtowych.
   - `glTexImage2D` – przesyła dane do OpenGL, tworząc teksturę 2D.

### 6.3 Ustawianie tekstury w `Cube`
1. Jeśli masz klasę `Cube(Mesh3D)`, w konstruktorze dodaj:
   ```python
    def __init__(self, draw_type, filename):
        ...
        Mesh3D.texture = pygame.image.load(filename)
        Mesh3D.draw_type = draw_type
        Mesh3D.init_texture(self)
   ```
2. Upewnij się, że sześcian ma zdefiniowane `self.vertices` (8 wierzchołków) i `self.triangles` (12 trójkątów na 6 ścian).

### 6.4 Definiowanie współrzędnych UV
1. Poniżej wierzchołków (`self.vertices`) stwórz `self.uvs`. Każdy wierzchołek dostaje (u,v) ∈ [0..1]:
    ```python
    ...
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
    ...
    ```
2. W metodzie `draw` (w `Mesh3D`) przed każdym `glVertex3fv(...)` wywołaj `glTexCoord2fv(...)`:
   ```python
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
   ```
    1. `glEnable(GL_TEXTURE_2D)` – włącza dwuwymiarowe teksturowanie w OpenGL. Od tej chwili kolejne rysowane prymitywy mogą mieć przypisaną teksturę.
    2. `glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)` – ustawia sposób łączenia koloru tekstury z kolorem fragmentu; `GL_DECAL` oznacza, że piksele z tekstury zastępują oryginalny kolor.
    3. `glBindTexture(GL_TEXTURE_2D, self.texID)` – wiąże (aktywuje) teksturę utworzoną i zainicjowaną wcześniej w `init_texture`. Od teraz rysowanie będzie korzystać z tej tekstury.
    4. **Pętla**: `for t in range(0, len(self.triangles), 3):` – przechodzi przez listę trójkątów w paczkach po 3 indeksy.
    - `glBegin(self.draw_type)` – rozpoczyna rysowanie prymitywu (np. `GL_POLYGON`, co w praktyce będzie służyć do rysowania trójkątów wypełnionych).
    - `glTexCoord2fv(self.uvs[t])` – ustawia współrzędne tekstury (u,v) dla danego wierzchołka.
    - `glVertex3fv(self.vertices[self.triangles[t]])` – rysuje wierzchołek w przestrzeni 3D.
    - To samo powtarza się dla drugiego i trzeciego wierzchołka danego trójkąta (`t+1`, `t+2`).
    5. `glEnd()` – kończy definiowanie prymitywu.

    Dzięki takiemu powiązaniu współrzędnych UV i wierzchołków 3D OpenGL wie, który fragment tekstury powinien zostać nałożony na każdą z ścian obiektu.


### 6.5 Użycie w `HelloLights.py`
Zamiast:
```python
mesh = Cube()
```
użyj:
```python
mesh = Cube(GL_POLYGON, "images/brick.tif")
```
Następnie uruchom – powinieneś zobaczyć na ścianach sześcianu załadowany obrazek.

---
## **7. Zadania do wykonania**
1. Ustaw ambient światła `(GL_LIGHT0)` na zielony `(0,1,0,1)` i sprawdź rezultat.
2. Dodaj kolejne światło `GL_LIGHT1` w położeniu `(-5,5,0)` z niebieskim diffuse.
3. Zmień materiał obiektu (np. `glMaterialfv(GL_FRONT, GL_DIFFUSE, (1,0,0,1))`) i obserwuj, jak barwa światła oddziałuje na powierzchnię.
4. Dopasuj `self.uvs` tak, aby każda ściana sześcianu prezentowała inny fragment tekstury. Wykorzystaj cubemapę.

---

W dalszych krokach możesz:
- Dodawać kolejne światła (GL_LIGHT1, GL_LIGHT2...),
- Modyfikować parametry materiału (np. specular, shininess) i kolory światła,
- Eksperymentować z różnymi plikami tekstur i rozmieszczeniem UV.

