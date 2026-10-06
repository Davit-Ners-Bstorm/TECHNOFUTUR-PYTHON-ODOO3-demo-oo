from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Soigneur import Soigneur

class Elephant:
    def __init__(self, nom: str, appetit: int, satisfaction: int, soigneur: "Soigneur"):
        self.nom = nom

        # Appetit
        if appetit < 0:
            print("Valeur negative, l'estomac explose!!!L'appetit est automatiquement ramené à 0")
            self._appetit = 0
        elif appetit > 100:
            print("Attention il va mourrir de faim, incorrecte, l'appetit est automatiquement ramené à 100")
            self._appetit = 100
        else:
            self._appetit = appetit

        # Satisfaction
        self.satisfaction = satisfaction
        
        self.soigneur = soigneur

        self._en_vie = True

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
    def appetit(self):
        return self._appetit

    @property
    def satisfaction(self):
        return self._satisfaction

    @satisfaction.setter
    def satisfaction(self, nv_satisfaction: int):
        if nv_satisfaction < 0:
            print("Valeur negative, il va mourrir de tristesse!!!La satisfaction est automatiquement ramené à 0")
            self._satisfaction = 0
        elif nv_satisfaction > 100:
            print("Attention il v aexploser de joie, la satisfaction est automatiquement ramené à 100")
            self._satisfaction = 100
        else:
            self._satisfaction = nv_satisfaction
        

    @property
    def en_vie(self):
        return self._en_vie

    @property
    def soigneur(self):
        return self._soigneur

    @soigneur.setter
    def soigneur(self, nv_soigneur: "Soigneur"):
        from models.Soigneur import Soigneur
        if not isinstance(nv_soigneur, Soigneur):
            raise TypeError("Le soigneur doit être de type soigneur!")
        self._soigneur = nv_soigneur
        

    def manger(self):
        if not self.en_vie:
            print(f"{self.nom} est mort, il ne peut donc pas manger :(")
            return
        if self.appetit <= 0:
            print(f"{self.nom} n'a pas faim")
            return
        self._appetit = 0
        self._satisfaction = self.satisfaction + 10 if self.satisfaction < 91 else 100
        # self.satisfaction = min(self.satisfaction + 10, 100)
        print(f"{self.nom} a bien mangé, et il est satisfait!")
