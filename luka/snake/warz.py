import pygame
from pygame.sprite import Sprite
from Dieuction import Dirction



class warz(Sprite):
    def __init__(self):
        self.orginalny_obraz = pygame.image.load('images/head.png')

        self.obraz = pygame.transform.rotate(self.orginalny_obraz, 0)

        self.pozycja = self.obraz.get_rect(center=(12*32 - 16, 9*32 - 16))

        self.kierunek = Dirction.Gora
        self.nowy_kierunek = Dirction.Gora
    def zmien_kierunek(self, kierunek):
        zmiana_morzliwa = True
        if kierunek == Dirction.Gora and self.kierunek == Dirction.Dol:
            zmiana_morzliwa = False
        if kierunek == Dirction.Dol and self.kierunek == Dirction.Gora:
            zmiana_morzliwa = False
        if kierunek == Dirction.Prawo and self.kierunek == Dirction.Lewo:
            zmiana_morzliwa = False
        if kierunek == Dirction.Lewo and self.kierunek == Dirction.Prawo:
            zmiana_morzliwa = False
        if zmiana_morzliwa:
            self.nowy_kierunek = kierunek

    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.orginalny_obraz, (self.kierunek.value*(-90)))
        if self.kierunek == Dirction.Gora:
            self.pozycja.move_ip(0, -32)
        if self.kierunek == Dirction.Prawo:
            self.pozycja.move_ip(32, 0)
        if self.kierunek == Dirction.Lewo:
            self.pozycja.move_ip(-32, 0)
        if self.kierunek == Dirction.Dol:
            self.pozycja.move_ip(0, 32)