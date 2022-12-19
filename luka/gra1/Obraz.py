import pygame

class Obraz(pygame.sprite.Sprite):
    def __init__(self, scieszka):
        super(Obraz, self).__init__()
        self.obraz = pygame.image.load(scieszka)




        