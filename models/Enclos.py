from models.Elephant import Elephant

class Enclos:
    def __init__(self, nom: str, capacite_max: int, taille: int, liste_animaux: list["Elephant"] = []):
        self.nom = nom
        self.capacite_max = capacite_max
        self._taille = taille
        self._liste_animaux = liste_animaux

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
    def capacite_max(self):
        return self._capacite_max

    @capacite_max.setter
    def capacite_max(self, nv_capacite_max: int):
        if type(nv_capacite_max) != int:
            raise TypeError("La capacité max doit être un integer!")
        if nv_capacite_max < 0:
            raise ValueError("La capacité max ne peut pas être negative!")
        self._capacite_max = nv_capacite_max

    @property
    def taille(self):
        return self._taille

    @property
    def liste_animaux(self):
        return self._liste_animaux
        

    def ajouter_animal(self, animal: "Elephant"):
        if len(self.liste_animaux) >= self.capacite_max:
            print(f"On ne peut pas rajotuer {animal.nom} à notre enclos {self.nom}, SORRY!")
        elif animal in self.liste_animaux:
            print(f"L'animal est deja dans l'enclos!")
        else:
            self._liste_animaux.append(animal)
            print("L'animal a bien été rajouté!")

    def enlever_animal(self, animal: "Elephant"):
        if animal not in self.liste_animaux:
            print('On peut pas le retirer, il est meme pas chez nous!')
        else:
            self._liste_animaux.remove(animal)
            print(f"{animal.nom} est bien retiré de l'enlos!")

    def afficher_animaux(self):
        if not self.liste_animaux:
            print("L'enclos est vide, que passa ?!")
        else:
            print(", ".join(pet.nom if pet.en_vie else f"{pet.nom} (RIP)" for pet in self.liste_animaux))
