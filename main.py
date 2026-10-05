class Voiture:
    nombre_de_roues = 4

    def __init__(self, marque, model, couleur):
        self.marque = marque
        self.model = model
        self.couleur = couleur
        self.vitesse_actuelle = 0

    def accelerer(self):
        self.vitesse_actuelle += 60
        print(f"VROUM VROUM {self.marque} + {self.vitesse_actuelle}KMH")



voiture1 = Voiture('BMW', "M3", "Blanche")
voiture2 = Voiture('Mercedes', "C63", "Noire")
voiture3 = Voiture('Toyota', "Corolla", "Bleu")

# print(voiture1.marque)
# print(voiture2.marque)
# print(voiture3.marque)

# print(voiture1.nombre_de_roues)
# print(voiture2.nombre_de_roues)
# print(voiture3.nombre_de_roues)

print(Voiture.nombre_de_roues)
print(Voiture.marque)

