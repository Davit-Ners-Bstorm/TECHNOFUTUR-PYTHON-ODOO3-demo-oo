from models.Animal import Animal

class Elephant(Animal):
    def __init__(self, nom, appetit, satisfaction, soigneur, longueur_defense):
        super().__init__(nom, appetit, satisfaction, soigneur)
        self.longueur_defense = longueur_defense

    @property
    def longueur_defense(self):
        return self._longueur_defense

    @longueur_defense.setter
    def longueur_defense(self, nv_longueur_defense):
        if type(nv_longueur_defense) != int:
            raise TypeError("La longueur de la defense doit être un integer !")
        if nv_longueur_defense < 0:
            raise ValueError("La longueur de la defense ne peut pas être inferieur à 0")
        self._longueur_defense = nv_longueur_defense

    def bain_de_boue(self):
        self.satisfaction = 100
        print(f"{self.nom} prend un bain de boue")

    def aspirer_eau(self):
        print(f"{self.nom} aspire de l'eau")

    def observer_environement(self, how: str = 'intense'):
        print(f"L'elephant {self.nom} observe l'environnement de manière {how} !")

    def probabilite_deces(self):
        return 5
