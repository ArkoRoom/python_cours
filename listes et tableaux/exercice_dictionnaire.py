### exercice

# Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec : 
# - numéro de voie 
# - complément 
# - intitulé de voie 
# - commune 
# - code postal 
# - Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire. 
# - Le logiciel devra permettre l'ajout, l'édition, la suppression et la visualisation des données par l'utilisateur. 

choix_menu = None
edit_adresse = None
dico_adresse = {}
dico_adresses = []

while True:
    print('''
          1 - Ajouter une adresse
          2 - Modifier une adresse
          3 - Supprimer une adresse
          4 - Consulter la liste des adresses
          0 - Quitter
    ''')
    choix_menu = input("Merci d'indiquer votre choix : ")
    match choix_menu:
        case "1":
            print("***** Ajout d'une adresse *****")
            add_street_number = int(input("Numéro de voie : "))
            add_street_complement = input("Complement d'adresse : ")
            add_street_name = input("Nom de voie : ")
            add_town = input("Ville : ")
            add_postcode = int(input("Code Postal : "))
            dico_adresse["numéro"] = add_street_number
            dico_adresse["complément"] = add_street_complement
            dico_adresse["nom de voie"] = add_street_name
            dico_adresse["ville"] = add_town
            dico_adresse["code postal"] = add_postcode
            dico_adresses.append(dico_adresse)
            print(dico_adresses)
        case "2":
            # edit_adresse = input("Veuillez indiquer votre choix")
            # print('''
            #     1 - Modifier le numéro de voie
            #     2 - Modifier le complément
            #     3 - Modifier la voie
            #     4 - Modifier la ville
            #     5 - Modifier le code postal
            #     0 - Quitter
            # ''')
            # match edit_adresse : 
            #     case "1": 
            print("Choix 2")
        case "3":
            print("Choix 3")
        case "4":
            if len(dico_adresses) > 0:
                for el in range(0, len(dico_adresses)) :
                    print(f"{dico_adresses}")
            else: 
                print("Aucune adresse")
        case "0":
            break