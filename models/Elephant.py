from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Soigneur import Soigneur

class Elephant:
    def __init__(self, nom: str, appetit: int, satisfaction: int, soigneur: "Soigneur"):
        self.nom = nom

        # Appetit
        if appetit < 0:
            print("Valeur negative, l'estomac explose!!!L'appetit est automatiquement ramené à 0")
            self.appetit = 0
        elif appetit > 100:
            print("Attention il va mourrir de faim, incorrecte, l'appetit est automatiquement ramené à 100")
            self.appetit = 100
        else:
            self.appetit = appetit

        # Satisfaction
        if satisfaction < 0:
            print("Valeur negative, il va mourrir de tristesse!!!La satisfaction est automatiquement ramené à 0")
            self.satisfaction = 0
        elif satisfaction > 100:
            print("Attention il v aexploser de joie, la satisfaction est automatiquement ramené à 100")
            self.satisfaction = 100
        else:
            self.satisfaction = satisfaction

        self.soigneur = soigneur

        self.en_vie = True

    def manger(self):
        if not self.en_vie:
            print(f"{self.nom} est mort, il ne peut donc pas manger :(")
            return
        if self.appetit <= 0:
            print(f"{self.nom} n'a pas faim")
            return
        self.appetit = 0
        self.satisfaction = self.satisfaction + 10 if self.satisfaction < 91 else 100
        # self.satisfaction = min(self.satisfaction + 10, 100)
        print(f"{self.nom} a bien mangé, et il est satisfait!")

