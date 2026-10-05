from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Elephant import Elephant

class Soigneur:
    def __init__(self, nom: str, date_de_naissance: str, experience: str, nb_animaux_responsable: int):
        self.nom = nom
        self.date_de_naissance = date_de_naissance
        self.experience = experience

        if nb_animaux_responsable < 0:
            print('Attention valeure negative')
            self.nb_animaux_responsable = 0
        else:
            self.nb_animaux_responsable = nb_animaux_responsable

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
