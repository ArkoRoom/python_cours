### exercice

# Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec : 
# - numéro de voie 
# - complément 
# - intitulé de voie 
# - commune 
# - code postal 
# - Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire. 
# - Le logiciel devra permettre l'ajout, l'édition, la suppression et la visualisation des données par l'utilisateur. 

adresses = [] #  ou un set

while True:
    print('''
          1. Ajouter une adresse
          2. Editer une adresse
          3. Supprimer une adresse
          4. Afficher les adresses
          0. Quitter''')
    choix_menu = input("Merci d'indiquer votre choix : ")
    match choix_menu:
        case "1":
            print("===== Ajout d'adresse =====")
            nouvelle_adresse = {}
            numero_voie = input("Merci de saisir numéro de voie : ")
            nouvelle_adresse["numero_voie"] = numero_voie
            complement_adresse = input("Merci de saisir le complément d'adresse : ")
            nouvelle_adresse["complement_adresse"] = complement_adresse
            intitule_voie = input("Merci de saisir l'intitulé de la voie : ")
            nouvelle_adresse["intitule_voie"] = intitule_voie
            commune = input("Merci de saisir la commune : ")
            nouvelle_adresse["commune"] = commune
            code_postal = input("Merci de saisir le code postal : ")
            nouvelle_adresse["code_postal"] = code_postal
            adresses.append(nouvelle_adresse)
        case "2":
            print("===== Edition d'une adresse =====")
            index_adresse = int(input("Merci de saisir l'index de l'adresse : "))
            if index_adresse >= 0 and index_adresse < len(adresses):
                numero_voie = input("Merci de saisir numéro de voie : ")
                adresses[index_adresse]["numero_voie"] = numero_voie if numero_voie != '' else adresses[index_adresse]["numero_voie"]
                complement_adresse = input("Merci de saisir le complément d'adresse : ")
                adresses[index_adresse]["complement_adresse"] = complement_adresse if complement_adresse != '' else adresses[index_adresse]["complement_adresse"]
                intitule_voie = input("Merci de saisir l'intitulé de la voie : ")
                adresses[index_adresse]["intitule_voie"] = intitule_voie if intitule_voie != '' else adresses[index_adresse]["intitule_voie"]
                commune = input("Merci de saisir la commune : ")
                adresses[index_adresse]["commune"] = commune if commune != '' else adresses[index_adresse]["commune"]
                code_postal = input("Merci de saisir le code postal : ")
                adresses[index_adresse]["code_postal"] = code_postal if code_postal != '' else adresses[index_adresse]["code_postal"]
        case "3":
            print("===== Suppression d'une adresse =====")
            index_adresse = int(input("Merci de saisir l'index de l'adresse : "))
            if index_adresse >= 0 and index_adresse < len(adresses):
                adresses.remove(adresses[index_adresse])
        case "4":
            print("===== Affichage des adresses =====")
            for index, adresse in enumerate(adresses):
                print(f"-------Adresse n° {index}-------")
                for cle, valeur in adresse.items():
                    print(f"{cle} : {valeur}")
        case "0":
            break
            
