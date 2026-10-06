from models.Soigneur import Soigneur
from models.Elephant import Elephant
from models.Enclos import Enclos
from models.Animal import Animal
from models.Girafe import Girafe


soigneur1 = Soigneur("Jordan", "01/01/1994", "+15 ans trop fort", 5)
soigneur2 = Soigneur("Raphaël", "01/01/1994", "+15 ans trop fort", 5)
elephant1 = Elephant("el", 50, 50, soigneur1, 24)
elephant2 = Elephant("el2", 50, 50, soigneur1, 24)
elephant3 = Elephant("el3", 50, 50, soigneur2, 24)

print('infos elephant', f"satisfaction = {elephant1.satisfaction}", f"appetit = {elephant1.appetit}")

soigneur1.nourrir(elephant1)
soigneur1.entretenir(elephant1)

print('infos elephant', f"satisfaction = {elephant1.satisfaction}", f"appetit = {elephant1.appetit}")
# soigneur2.nourrir(elephant1)

enclos1 = Enclos("ODOO", 2, 42)

print('****************************')

enclos1.afficher_animaux()

print('****************************')
print('****************************')
print('****************************')

enclos1.ajouter_animal(elephant1)
print('****************************')

enclos1.afficher_animaux()

enclos1.ajouter_animal(elephant3)

enclos1.afficher_animaux()

# enclos1.ajouter_animal(elephant2)

# elephant1.en_vie = False

enclos1.afficher_animaux()

enclos1.enlever_animal(elephant1)

enclos1.afficher_animaux()

enclos1.enlever_animal(elephant1)




# def sayHello(nom, bonjour):
#     return f"{nom} dit {bonjour}"

# print(sayHello("Raphaël", 'Bonjour'))
# print(sayHello(bonjour='Bonjour', nom='Raphaël'))

girafe = Girafe("girafe", 25, 25, soigneur2, 23)

print(isinstance(elephant1, Elephant))
print(isinstance(elephant1, Animal))

elephant1.manger()
girafe.manger()


elephant1.observer_environement()
girafe.observer_environement("bizzare")
