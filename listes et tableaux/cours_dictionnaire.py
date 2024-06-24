# Les dictionnaires

# Un exemple de dictionnaire
first_dico = {
    "nom": "Dupont",
    "prenom": "Pierre",
    "age": 42
}
print(first_dico["nom"])

# Ajout d'un element au dictionnaire
first_dico["ville"] = "Paris"

# Suppression d'un element d'un dictionnaire
del first_dico["age"]

# itération des cle
for cle in first_dico : 
    print(f"{cle} => {first_dico[cle]}")

# iterer juste les valeurs
for element in first_dico.values() : 
    print(element)

# iterer avec clé et valeur
for cle, element in first_dico.items() : 
    print(f"{cle} => {element}")