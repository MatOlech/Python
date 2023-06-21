import pygame
import random

# Inicjalizacja gry
pygame.init()

# Ustawienia ekranu
szerokosc = 800
wysokosc = 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Snake")

# Kolory
czarny = (0, 0, 0)
bialy = (255, 255, 255)
czerwony = (255, 0, 0)

# Rozmiar bloku
rozmiar_bloku = 20

# Inicjalizacja zegara
zegar = pygame.time.Clock()

# Funkcja rysująca węża na ekranie
def rysuj_weza(ekran, waz, rozmiar_bloku):
    for segment in waz:
        pygame.draw.rect(ekran, czarny, [segment[0], segment[1], rozmiar_bloku, rozmiar_bloku])

# Główna pętla gry
def gra():
    koniec_gry = False
    koniec_programu = False

    # Początkowe położenie węża
    x = szerokosc / 2
    y = wysokosc / 2

    # Początkowa prędkość węża
    predkosc_x = 0
    predkosc_y = 0

    # Inicjalizacja węża
    waz = []
    dlugosc_węża = 1

    # Inicjalizacja położenia jedzenia
    jedzenie_x = round(random.randrange(0, szerokosc - rozmiar_bloku) / rozmiar_bloku) * rozmiar_bloku
    jedzenie_y = round(random.randrange(0, wysokosc - rozmiar_bloku) / rozmiar_bloku) * rozmiar_bloku

    while not koniec_programu:
        while koniec_gry == True:
            ekran.fill(bialy)
            font = pygame.font.Font(None, 50)
            tekst = font.render("Koniec gry! Naciśnij Q - wyjście lub C - nowa gra", True, czerwony)
            ekran.blit(tekst, (szerokosc / 2 - tekst.get_width() / 2, wysokosc / 2 - tekst.get_height() / 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    koniec_programu = True
                    koniec_gry = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        koniec_programu = True
                        koniec_gry = False
                    if event.key == pygame.K_c:
                        gra()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                koniec_programu = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    predkosc_x = -rozmiar_bloku
                    predkosc_y = 0
                elif event.key == pygame.K_RIGHT:
                    predkosc_x = rozmiar_bloku
                    predkosc_y = 0
                elif event.key == pygame.K_UP:
                    predkosc_y = -rozmiar_bloku
                    predkosc_x = 0
                elif event.key == pygame.K_DOWN:
                    predkosc_y = rozmiar_bloku
                    predkosc_x = 0

        if x >= szerokosc or x < 0 or y >= wysokosc or y < 0:
            koniec_gry = True

        x += predkosc_x
        y += predkosc_y
        ekran.fill(bialy)
        pygame.draw.rect(ekran, czerwony, [jedzenie_x, jedzenie_y, rozmiar_bloku, rozmiar_bloku])
        waz_glowa = []
        waz_glowa.append(x)
        waz_glowa.append(y)
        waz.append(waz_glowa)
        if len(waz) > dlugosc_węża:
            del waz[0]

        for segment in waz[:-1]:
            if segment == waz_glowa:
                koniec_gry = True

        rysuj_weza(ekran, waz, rozmiar_bloku)
        pygame.display.update()

        if x == jedzenie_x and y == jedzenie_y:
            jedzenie_x = round(random.randrange(0, szerokosc - rozmiar_bloku) / rozmiar_bloku) * rozmiar_bloku
            jedzenie_y = round(random.randrange(0, wysokosc - rozmiar_bloku) / rozmiar_bloku) * rozmiar_bloku
            dlugosc_węża += 1

        zegar.tick(15)

    pygame.quit()

# Uruchomienie gry
gra()
