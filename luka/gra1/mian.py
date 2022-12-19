import pygame
from NakrycieGlowy import Nakrycieglowy
from Element import Element 
from Weapon import Weapon


szerokosc_ekranu =  800
wysokosc_ekranu = 600

obraz_tla = pygame.image.load('images/background.png')
postac1 = pygame.image.load('images/base.png')
pygame.init()
ekran = pygame.display.set_mode([szerokosc_ekranu, wysokosc_ekranu])
zegar = pygame.time.Clock()

gra_dziala = True

while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.type == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
    
    ekran.blit(obraz_tla, (0,0))
    ekran.blit(postac1,(270, 130))
    ekran.blit(Nakrycieglowy().WybranyObraz(),(270,165))
    ekran.blit(Weapon().WybranyObraz(),(200,75))
    pygame.display.flip()

    zegar.tick(40)

pygame.quit()