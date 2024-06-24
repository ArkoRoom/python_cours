### exercice

# Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec : 
# - numéro de voie 
# - complément 
# - intitulé de voie 
# - commune 
# - code postal 
# - Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire. 
# - Le logiciel devra permettre l'ajout, l'édition, la suppression et la visualisation des données par l'utilisateur. 

set_nom_famille = set()

while True:
    print('''
          1. Ajouter un nom
          2. Afficher les noms
          3. Supprimer le nom
          4. Editer le nom
          0. Quitter''')
    choix_menu = input("Merci d'indiquer votre choix : ")
    match choix_menu:
        case "1":
            print("=== Ajout d'un nom de famille ===")
            nom_famille = input("Merci de saisir le nom de famille : ")
            set_nom_famille.add(nom_famille)
        case "2":
            print("=== Affichage des noms de famille ===")
            for nom in set_nom_famille:
                print(nom)
        case "3":
            print("=== Suppression d'un nom de famille ===")
            nom_famille = input("Merci de saisir le nom de famille : ")
            set_nom_famille.discard(nom_famille)
        case "4":
            print("=== Edition d'un nom de famille ===")
            nom_famille_a_modifier = input("Merci de saisir le nom de famille à modifier : ")
            nouvelle_valeur_nom_famille = input("Merci de saisir la nouvell valeur : ")
            set_nom_famille.remove(nom_famille_a_modifier)
            set_nom_famille.add(nouvelle_valeur_nom_famille)
        case "0":
            break