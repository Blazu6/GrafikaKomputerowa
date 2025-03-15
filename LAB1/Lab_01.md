
---

# Grafika Komputerowa - Laboratorium 01

## Cel zajęć

- **Grafika 2D:** Poznasz mechanizm tworzenia okna graficznego, rysowania pojedynczych pikseli oraz przekształcania układu współrzędnych.
- **Rysowanie elementów:** Opanujesz rysowanie gradientów, linii (zarówno przy pomocy funkcji Pygame, jak i poprzez ręczną implementację) oraz wyświetlanie tekstu.
- **Algorytmy rysowania:** Zrozumiesz różnice między metodą naiwą rysowania linii a algorytmem Bresenhama, a także rozszerzysz umiejętności o rysowanie okręgów i zastosowanie antyaliasingu.

---

## Część 1: Hello Graphics Window

### Zadania i przykładowe kody

### 1. Konfiguracja środowiska
- **Instalacja:**  
  - Pobierz Python (np. z [python.org](https://www.python.org/)).
  - Zainstaluj Visual Studio Code
  - Z okna poleceń zainstaluj PyGame (pip install pygame) 

### 2. Tworzenie pierwszego okna graficznego

Utwórz plik o nazwie `HelloWindow.py` i wpisz poniższy kod:

```python
import pygame

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()
pygame.quit()
```

**Co osiągniesz?**  
- Inicjalizujesz bibliotekę Pygame.
- Utworzysz okno o rozmiarze 1000×800 pikseli.
- Zapewnisz, że okno pozostanie otwarte dzięki pętli głównej, aż użytkownik kliknie przycisk zamknięcia.

### 3. Rysowanie pojedynczych pikseli i prostokątów

Aby zapoznać się z układem współrzędnych, utwórz plik `PlotPixel.py` i dodaj kod, który rysuje piksel w wybranym punkcie:

```python
import pygame

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Rysowanie pojedynczego piksela w punkcie (100, 100)
    screen.set_at((100, 100), white)
    # Możesz również narysować dodatkowy piksel, np. w punkcie (200,200)
    screen.set_at((200, 200), white)
    pygame.display.update()
pygame.quit()
```

Dodatkowo, aby piksel był lepiej widoczny, możesz narysować mały prostokąt:

```python
import pygame

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    position = (100, 100)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    pygame.display.update()
pygame.quit()
```

**Twoje zadanie:** Zmodyfikuj kod, tak aby narysować Twoje inicjały za pomocą prostokątów, linii lub pikseli.

---

## Część 2: Więcej rysowania!

## Cel zajęć

- **Eksperymentujesz z kolorami:** Nauczysz się tworzyć gradienty, mieszając kanały kolorów.
- **Rysowanie elementów:** Opanujesz rysowanie linii (w tym interaktywne rysowanie z użyciem myszy), wyświetlanie tekstu oraz rysowanie wielokątów.
- **Praca z obrazami rastrowymi:** Dowiesz się, jak wczytać i wyświetlić obraz rastrowy w swojej aplikacji.

---

### 1. Rysowanie gradientu kolorów

Utwórz plik `RGBSpace.py` i wklej poniższy kod, który rysuje gradient mieszający kanały czerwony i zielony (niebieski na stałe ustawiony na 255):

```python
import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y in range(screen_height):
        for x in range(screen_width):
            color = pygame.Color(int(x / screen_width * 255),
                                 int(y / screen_height * 255), 255)
            screen.set_at((x, y), color)
    pygame.display.update()
pygame.quit()
```

**Twoje zadanie:** Zmodyfikuj kod, aby stworzyć gradient mieszający kanały zielony i niebieski (przy czym kanał czerwony powinien być ustawiony na 0).

---

### 2. Rysowanie linii z użyciem myszy

Utwórz plik `PygameLine.py` i wpisz poniższy kod. Dzięki niemu będziesz mógł narysować linię poprzez dwa kliknięcia myszy:

```python
import pygame
from pygame.locals import *

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)
times_clicked = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if times_clicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            times_clicked += 1
            if times_clicked > 1:
                pygame.draw.line(screen, white, point1, point2, 1)
                times_clicked = 0
    pygame.display.update()
pygame.quit()
```

---

### 3. Wyświetlanie tekstu

Utwórz plik `CustomText.py` i skorzystaj z poniższego przykładu:

```python
import pygame

pygame.init()
screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)
pygame.font.init()

# Użycie systemowej czcionki Comic Sans MS
font = pygame.font.SysFont('Comic Sans MS', 60, False, True)
text = font.render('graphic design is my passion', False, white)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(text, (10, 10))
    pygame.display.update()
pygame.quit()
```

**Twoje zadanie:** Znajdź inny plik czcionki TrueType (.ttf) (np. ze strony [dafont.com](https://www.dafont.com)), dodaj go do folderu „fonts” w swoim projekcie, a następnie zmodyfikuj kod, aby wyświetlić dodatkowy napis poniżej już istniejącego:

```python
# Przykład użycia niestandardowej czcionki:
font_custom = pygame.font.Font('fonts/NazwaTwojejCzcionki.ttf', 100)
custom_text = font_custom.render('Inny tekst', False, white)
# W pętli głównej:
screen.blit(custom_text, (10, 120))
```

---

### 4. Rysowanie wielokątów

W tej sekcji nauczysz się, jak rysować wypełnione i obrysowane wielokąty przy użyciu funkcji `pygame.draw.polygon()`. Wielokąty to kształty złożone z połączonych linii (krawędzi) i punktów (wierzchołków).

Utwórz plik `PolygonDrawing.py` i użyj poniższego kodu:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(pygame.Color(0, 0, 0))
    
    # Rysowanie wypełnionego trójkąta
    triangle_points = [(400, 100), (300, 300), (500, 300)]
    pygame.draw.polygon(screen, white, triangle_points, 0)
    
    # Rysowanie wypełnionego kwadratu
    square_points = [(150, 400), (150, 550), (300, 550), (300, 400)]
    pygame.draw.polygon(screen, blue, square_points, 0)
    
    pygame.display.update()
pygame.quit()
```

**Wyjaśnienie:**  
- Funkcja `pygame.draw.polygon()` przyjmuje jako argumenty: powierzchnię, kolor, listę wierzchołków, a ostatni parametr określa grubość obrysu (0 oznacza wypełnienie kształtu).

---

### 5. Praca z obrazami rastrowymi

W tej sekcji nauczysz się, jak wczytywać i wyświetlać obrazy rastrowe w Pygame. 
Utwórz plik `RasterImages.py` i wklej poniższy kod:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

# Załaduj obraz – upewnij się, że plik "obraz.png" znajduje się w katalogu projektu
image = pygame.image.load('obraz.png')

# Opcjonalnie: zmień rozmiar obrazu, jeśli jest za duży lub za mały
# image = pygame.transform.scale(image, (400, 300))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(pygame.Color(0, 0, 0))
    # Wyświetl obraz w pozycji (200, 150)
    screen.blit(image, (200, 150))
    pygame.display.update()
pygame.quit()
```

**Uwaga:**  
- Upewnij się, że plik obrazu (np. "obraz.png") znajduje się w katalogu projektu lub podaj pełną ścieżkę do pliku.
- Możesz eksperymentować ze skalowaniem obrazu, używając funkcji `pygame.transform.scale()`.

---


## Część 3: Rysowanie pixel po pixelu

### Zadania i przykładowe kody

W tej części skupimy się na rysowaniu linii na poziomie pojedynczych pikseli oraz na omówieniu dwóch podejść: metody naiwnej i algorytmu Bresenhama.

### 1. Metoda naiwna rysowania linii

**Cel:** Narysować linię, obliczając dla każdego x wartość y na podstawie równania liniowego (y = m*x + c).

Przykładowy kod (utwórz plik `NaiveLine.py`):

```python
import pygame
import math

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)

# Parametry linii
m = 0.5   # nachylenie
c = 100   # wyraz wolny

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Rysowanie linii metodą naiwną: dla każdego x oblicz y = m*x + c
    for x in range(screen_width):
        y = int(m * x + c)
        if 0 <= y < screen_height:
            screen.set_at((x, y), white)
    pygame.display.update()
pygame.quit()
```

**Test:**  
- Zmień wartości m i c, aby zobaczyć, jak zmienia się linia.
- Sprawdź, co dzieje się dla linii o większym nachyleniu (np. m = 2) lub przy ujemnym nachyleniu.

### 2. Algorytm Bresenhama do rysowania linii

**Cel:** Zaimplementować algorytm, który rysuje linię efektywniej (bez operacji zmiennoprzecinkowych) niż metoda naiwna.

Utwórz plik `BresenhamLine.py` i wpisz poniższy kod:

```python
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
```

**Co warto przetestować?**  
- Zmieniaj punkty początkowe i końcowe, aby zobaczyć, jak algorytm radzi sobie z liniami w różnych kierunkach.
- Porównaj wizualnie linię narysowaną metodą naiwną i algorytmem Bresenhama.

### 3. Rozszerzenie – Rysowanie okręgów i antyaliasing

**Cel:**  
- Zaimplementuj rysowanie okręgów metodą Bresenhama (lub zmodyfikowaną wersją) oraz wprowadź podstawy antyaliasingu dla wygładzenia krawędzi.

Przykładowy kod do rysowania okręgu (utwórz plik `BresenhamCircle.py`):

```python
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
```

**Antyaliasing:**  
Wprowadzenie antyaliasingu (wygładzania krawędzi) może być bardziej złożone. Jako zadanie dodatkowe spróbuj:
- Zastosować funkcję `pygame.draw.aaline()`, która rysuje linię z włączonym antyaliasingiem.
- Porównać efekt linii rysowanej funkcją `pygame.draw.line()` i `pygame.draw.aaline()`.

Na przykład:

```python
import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Rysowanie linii z antyaliasingiem
    pygame.draw.aaline(screen, white, (100, 100), (900, 700))
    pygame.display.update()
pygame.quit()
```

---