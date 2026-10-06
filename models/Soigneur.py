from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Elephant import Elephant

class Soigneur:
    def __init__(self, nom: str, date_de_naissance: str, experience: str, nb_animaux_responsable: int):
        self.nom = nom
        self._date_de_naissance = date_de_naissance
        self._experience = experience

        if nb_animaux_responsable < 0:
            print('Attention valeure negative')
            self._nb_animaux_responsable = 0
        else:
            self._nb_animaux_responsable = nb_animaux_responsable

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nv_nom: str):
        if not nv_nom:
            raise ValueError("Le nom ne peut pas être vide!")
        if type(nv_nom) != str:
            raise TypeError("Le nom doit être un string!")
        self._nom = nv_nom

    @property
    def date_de_naissance(self):
        return self._date_de_naissance

    @property
    def experience(self):
        return self._experience

    @property
    def nb_animaux_responsable(self):
        return self._nb_animaux_responsable

    @property
    def age(self):
        day, month, year = [int(i) for i in self.date_de_naissance.split('/')]
        today = date.today()

        soigneur_age = today.year - year

        if (today.month, today.day) < (month, day):
            soigneur_age -= 1

        return soigneur_age

    def nourrir(self, elephant: "Elephant"):
        if elephant.soigneur == self:
            print(f"{self.nom} va essayer de nourrir {elephant.nom}!")
            elephant.manger()
        else:
            print(f"{elephant.nom} n'est pas à la charge de {self.nom}, il ne peut donc pas le nourrir!")

    def entretenir(self, elephant: "Elephant"):
        if elephant.soigneur == self:
            print(f"{self.nom} va brosser {elephant.nom}!")
            elephant.satisfaction = min(elephant.satisfaction + 25, 100)
        else:
            print(f"{elephant.nom} n'est pas à la charge de {self.nom}, il ne peut donc pas le brosser!")
