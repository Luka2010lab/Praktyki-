from Obraz import Obraz

class Element():
    def __init__(self, typ):
        self.wybrany = 0
        self.lista_obrazow = []

        for i in range(1,4):
            scieszka = f'images/{typ}{i}.png'
            wczytany_obraz = Obraz(scieszka)
            self.lista_obrazow.append(wczytany_obraz)

    def WybierzNastempny(self):
        self.Wybrany += 1
        if self.wybrany > 2:
            self.Wybrany = 0
    def WybranyObraz(self):
        return self.lista_obrazow[self.wybrany].obraz








