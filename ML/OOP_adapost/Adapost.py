from TooManyAnimalsException import TooManyAnimalsException
from Pisica import Pisica
from Catel import Catel

class Adapost:

    def __init__(self):
        self.lista_animale = []

    def adauga_animal(self, a):
        if len(self.lista_animale) == 30:
            raise TooManyAnimalsException()
        self.lista_animale.append(a)
        print('Am adaugat un animal in adapost! ')

    def adoptie_animal(self, id_animal):
        for animal in self.lista_animale:
            if animal.id == id_animal:
                print('Am adoptat un animal')
                self.lista_animale.remove(animal)
                break

    def afisare_animale(self):
        for animal in self.lista_animale:
            print(str(animal.id) + ' ' + animal.rasa + ' ' + str(animal.varsta))


    def afisare_specifica(self, tip):
        if tip == 'pisica':
            for animal in self.lista_animale:
                if isinstance(animal, Pisica):
                    print(animal.id, animal.rasa, animal.varsta, animal.vaccinat, animal.sterilizat)
        elif tip == 'catel':
            for animal in self.lista_animale:
                if isinstance(animal, Catel):
                    print(animal.id, animal.rasa, animal.varsta, animal.vaccinat)



