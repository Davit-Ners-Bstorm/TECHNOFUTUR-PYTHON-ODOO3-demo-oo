from models.Animal import Animal

class Girafe(Animal):
    def __init__(self, nom, appetit, satisfaction, soigneur, longueur_cou: int):
        super().__init__(nom, appetit, satisfaction, soigneur)
        self.longueur_cou = longueur_cou

    @property
    def longueur_cou(self):
        return self._longueur_cou

    @longueur_cou.setter
    def longueur_cou(self, nv_longueur_cou):
        if type(nv_longueur_cou) != int:
            raise TypeError("La longueur du cou doit être un integer !")
        if nv_longueur_cou < 0:
            raise ValueError("La longueur du cou ne peut pas être inferieur à 0")
        self._longueur_cou = nv_longueur_cou

    def manger(self):
        super().manger()
        print("C'etait bien des feuilles hein!")

    def boire_eau(self):
        print(f"{self.nom} a bien bu de l'eau!")

    def observer_environement(self, how: str = 'intense'):
        print(f"La girafe {self.nom} observe l'environnement de manière {how} , du haut de son cou de {self.longueur_cou} cm!")
