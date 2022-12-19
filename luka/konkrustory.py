from samochud import samochod
from Book import Book
from zadanie.kolo import Circle

# auto = samochod()
# auto.kolor = "czerwony"
# auto.marka = "ferrari"
# auto.rejstracja = "CG 32713"
# auto.roztaw_osi = "1.32"
# auto.model = "z46"

# auto.wyswietl()

# nowe_ferrari = samochod("ferrari", "czerwone", "CG 32713", 1,32, "z46")
# nowe_ferrari.wyswietl()

ksiaszka = Book("Adam Mickiewicz", "szatan z 8 klasy", "2137 stron")
ksiaszka.wyswiel()

okrag = Circle(1)
print(okrag.area())
print(okrag.length())


