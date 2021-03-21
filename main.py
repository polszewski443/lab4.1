from random import *

# Zad. 1
# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
print('#############ZAD1#############')

plik = open("pythonlab4.txt", "w")
for i in range(50):
    i = randint(1, 100)
    if i % 4 == 0:
        plik.write(str(i) + " ")
plik.close()
# Zad. 2
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
print('#############ZAD2#############')

plik = open("pythonlab4.txt", "r")
odczyt = plik.readlines()
print(odczyt)
plik.close()

# Zad. 3
# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
print('#############ZAD3#############')
with open("pythonlab4.txt", "a") as plik:
    plik.writelines("AAAAAAAAAAAAAAAABBBBB\nBBBBBBBBBBBBBCCCCCCCCCCCCCCCC\nAAAAAAAAABBBBBBBBBBD\n")

with open("pythonlab4.txt", "r") as plik:
    tekst = plik.readlines()
    print(tekst)

# Zad.4
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty (...):
print('#############ZAD4#############')


class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        return self.nazwa_produktu

    def ile_produktu(self):
        return f'{self.ilosc} {self.jednostka_miary}'

    def ile_kosztuje(self):
        return self.cena_jed * self.ilosc


klasa = NaZakupy('cukier', 42, 'kg', 2.30)

print(klasa.wyswietl_produkt(), klasa.ile_produktu(), klasa.ile_kosztuje(), 'zl')

# Zad.5
# Utwórz klasę, która definiuje ciągi arytmetyczne.
# Wartości powinny być przechowywane jako atrybut.
# Klasa powinna mieć metody:
print('#############ZAD5#############')


class Carytmetyczne:
    ciag = []
    pierw = 0
    roz = 0
    ilosc = 0
    suma = 0
    liczbael = 0
    element = ' '

    def wyswietl_dane(self):
        return f'Elementy: {self.ciag}'

    def pobierz_elementy(self):
        self.suma = 0
        self.ciag.clear()
        self.ilosc = int(input('Podaj ilosc elementow ciagu, a nastepnie podaj te elementy: '))
        for i in range(self.ilosc):
            self.ciag.append(int(input(self.element)))

    def pobierz_parametry(self):
        self.suma = 0
        self.ciag.clear()
        self.pierw = int(input('Podaj pierwsza wartosc ciagu: '))
        self.roz = int(input('Podaj roznice ciagu: '))
        self.ilosc = int(input('Podaj ilosc elementow ciagu do wygenerowania: '))

    def policz_sume(self):
        for i in range(0, len(self.ciag)):
            self.suma = self.suma + self.ciag[i]
        return self.suma

    def policz_elementy(self):
        self.ciag.append(self.pierw)
        for i in range(1, self.ilosc):
            self.ciag.append((self.ciag[i - 1] + self.roz))


klasa = Carytmetyczne()

klasa.pobierz_parametry()
klasa.policz_elementy()
print('Dane', klasa.wyswietl_dane(), 'Suma to', klasa.policz_sume())
klasa.pobierz_elementy()
print('Dane', klasa.wyswietl_dane(), 'Suma to', klasa.policz_sume())

# Zad. 6
# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka.
# Klasa powinna przechowywać współrzędne x, y, krok
# (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
print('#############ZAD6#############')


class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        return f'({self.x}, {self.y})'


klasa = Robaczek(0, 0, 1)

klasa.idz_w_gore(23)
klasa.idz_w_prawo(12)
klasa.idz_w_lewo(17)
klasa.idz_w_dol(16)
print('Robak znajduje sie na koordynatach: ', klasa.pokaz_gdzie_jestes())
