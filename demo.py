from datetime import date

class Voiture:
    nombre_de_roues = 4

    def __init__(self, marque, model, couleur, identifiant, date_de_fabrication):
        self.marque = marque
        self._identifiant = identifiant
        self.model = model
        self.couleur = couleur
        self.date_de_fabrication = date_de_fabrication
        self.vitesse_actuelle = 0

    @property
    def identifiant(self):
        return self._identifiant

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, nv_marque: str):
        if not nv_marque:
            raise ValueError("La marque ne peut pas être vide!")
        if type(nv_marque) != str:
            raise TypeError("La marque doit être un string!")
        if nv_marque.lower() == "peugeot":
            raise ValueError("on veut pas de ça!")
        self._marque = nv_marque

    @marque.deleter
    def marque(self):
        if self.marque == "BMW":
            print('Tu peux pas!')
        else:
            del self._marque

    def accelerer(self):
        self.vitesse_actuelle += 60
        print(f"VROUM VROUM {self.marque} + {self.vitesse_actuelle}KMH")

    @property
    def infos(self):
        return f"{self.marque} - {self.model} --- Roule à {self.vitesse_actuelle} km/h"

    @property
    def age_vehicule(self):
        today = date.today()
        return today.year - self.date_de_fabrication



voiture1 = Voiture("BMW", "M3", "Blanche", "1", 1980)
voiture2 = Voiture('Mercedes', "C63", "Noire", "2", 2011)
voiture3 = Voiture('Toyota', "Corolla", "Bleu", "3", 2025)

# voiture1.marque = "Peugeot"
# voiture1.marque = 'Peugeot'
# print(voiture1._marque)
# del voiture1.marque

# voiture1.identifiant = "2"
print(voiture1.identifiant)
print(voiture1.age_vehicule)

# print(voiture1.marque)
# print(voiture2.marque)
# print(voiture3.marque)

# print(voiture1.nombre_de_roues)
# print(voiture2.nombre_de_roues)
# print(voiture3.nombre_de_roues)

# print(Voiture.nombre_de_roues)
# print(Voiture.marque)

# print(voiture1.nombre_de_roues, voiture2.nombre_de_roues)

# voiture1.hello = 2




# class Chat:
#     nom = "Gerard"

# chat1 = Chat()
# chat2 = Chat()
# chat1.nom = "Kitty"
# chat1.race = "Siamois"

# print(chat1.race, chat2.nom, Chat.nom)
