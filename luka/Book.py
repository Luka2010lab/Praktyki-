class Book:
    autor = ""
    tytul = ""
    ilosc_stron = ""

    def __init__(self, autor, tytul, ilosc_stron):
        self.autor = autor
        self.tytul = tytul
        self.ilosc_stron = ilosc_stron
    
    def wyswiel(self):
        print(self.autor)
        print(self.tytul)
        print(self.ilosc_stron)