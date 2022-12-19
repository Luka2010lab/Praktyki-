class samochod:
    marka = ""
    model = ""
    rejstracja = ""
    kolor = ""
    roztaw_osi = ""

    def wyswietl(self):
        print(self.marka)
        print(self.model)
        print(self.rejstracja)
        print(self.kolor)
        print(self.roztaw_osi)

    def __init__(self, marka, kolor, model, roztaw_osi, rejstracjca):
        self.marka =  marka
        self.kolor = kolor
        self.model = model
        self.rejstracja = rejstracjca
        self.roztaw_osi = roztaw_osi
