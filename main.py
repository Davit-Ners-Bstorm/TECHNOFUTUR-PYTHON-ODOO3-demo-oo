from models.Soigneur import Soigneur
from models.Elephant import Elephant

class Voiture:
    nombre_de_roues = 4
    __slots__ = ('marque', 'model', 'couleur', 'vitesse_actuelle')

    def __init__(self, marque, model, couleur):
        self.marque = marque
        self.model = model
        self.couleur = couleur
        self.vitesse_actuelle = 0

    def accelerer(self):
        self.vitesse_actuelle += 60
        print(f"VROUM VROUM {self.marque} + {self.vitesse_actuelle}KMH")



# voiture1 = Voiture('BMW', "M3", "Blanche")
# voiture2 = Voiture('Mercedes', "C63", "Noire")
# voiture3 = Voiture('Toyota', "Corolla", "Bleu")

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


soigneur1 = Soigneur("Jordan", "01/01/1994", "+15 ans trop fort", 5)
soigneur2 = Soigneur("Raphaël", "01/01/1994", "+15 ans trop fort", 5)
elephant1 = Elephant("el", 50, 50, soigneur1)

print('infos elephant', f"satisfaction = {elephant1.satisfaction}", f"appetit = {elephant1.appetit}")

soigneur1.nourrir(elephant1)
soigneur1.entretenir(elephant1)

print('infos elephant', f"satisfaction = {elephant1.satisfaction}", f"appetit = {elephant1.appetit}")
# soigneur2.nourrir(elephant1)
