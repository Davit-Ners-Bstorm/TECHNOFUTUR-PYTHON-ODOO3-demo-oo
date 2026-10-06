from abc import ABC, abstractmethod

class Vehicule(ABC):

    @property
    @abstractmethod
    def vitesse_max(self):
        pass

    @property
    def hey(self):
        return 'Hey'

    @abstractmethod
    def accelerer(self):
        pass

class Voiture(Vehicule):
    def __init__(self, marque, vitesse_max):
        self.marque = marque
        self._vitesse_max = vitesse_max

    @property
    def vitesse_max(self):
        return self._vitesse_max

    def accelerer(self):
        print('Vroum Vroum')

    @property
    @abstractmethod
    def voiture_function(self):
        pass

class VoitureSport(Voiture):
    def voiture_function(self):
        print('test funciotn')

voiture1 = VoitureSport("citroen", 175)

class Moto(Vehicule):
    def __init__(self, marque, vitesse_max):
        self.marque = marque
        self._vitesse_max = vitesse_max

    @property
    def vitesse_max(self):
        return self._vitesse_max

    def accelerer(self):
        print('Vroum Vroum')

moto1 = Moto('Yamasaki', 300)
moto1.accelerer()
print(moto1.hey)
