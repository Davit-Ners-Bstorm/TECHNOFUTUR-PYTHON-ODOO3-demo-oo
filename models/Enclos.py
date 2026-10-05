from models.Elephant import Elephant

class Enclos:
    def __init__(self, nom: str, capacite_max: int, taille: int, liste_animaux: list["Elephant"] = []):
        self.nom = nom
        self.capacite_max = capacite_max
        self.taille = taille
        self.liste_animaux = liste_animaux

    def ajouter_animal(self, animal: "Elephant"):
        if len(self.liste_animaux) >= self.capacite_max:
            print(f"On ne peut pas rajotuer {animal.nom} à notre enclos {self.nom}, SORRY!")
        elif animal in self.liste_animaux:
            print(f"L'animal est deja dans l'enclos!")
        else:
            self.liste_animaux.append(animal)
            print("L'animal a bien été rajouté!")

    def enlever_animal(self, animal: "Elephant"):
        if animal not in self.liste_animaux:
            print('On peut pas le retirer, il est meme pas chez nous!')
        else:
            self.liste_animaux.remove(animal)
            print(f"{animal.nom} est bien retiré de l'enlos!")

    def afficher_animaux(self):
        if not self.liste_animaux:
            print("L'enclos est vide, que passa ?!")
        else:
            print(", ".join(pet.nom if pet.en_vie else f"{pet.nom} (RIP)" for pet in self.liste_animaux))
