# Créez une fonction ajouter_utilisateur qui prend comme arguments le nom de l'utilisateur et son rôle (ex:
# "Administrateur", "Visiteur", "Opérateur") et l'ajoute à un dictionnaire global utilisateurs, où le nom est la
# clé et le rôle est la valeur.
# Écrivez une fonction changer_role qui modifie le rôle d'un utilisateur existant. La fonction doit vérifier si
# l'utilisateur existe avant de changer le rôle.
# Développez une fonction afficher_utilisateurs qui imprime tous les utilisateurs et leurs rôles.

list_users = []

def add_user(name: str, role: str) :
    new_user = {}
    new_user["name"] = name
    new_user["role"] = role
    list_users.append(new_user)

def edit_user(index_user: int) : 
    if index_user >= 0 and index_user < len(list_users):
        name_user = input("Merci de saisir le nom de l'utilisateur : ")
        list_users[index_user]["name"] = name_user if name_user != '' else list_users[index_users]["name"]
        role_user = input("Merci de saisir le rôle de l'utilisateur : ")
        match role_user : 
            case "1": 
                list_users[index_user]["role"] = "Administrateur" if role_user != '' else list_users[index_user]["role"]
            case "2": 
                list_users[index_user]["role"] = "Visiteur" if role_user != '' else list_users[index_user]["role"]
            case "3": 
                list_users[index_user]["role"] = "Opérateur" if role_user != '' else list_users[index_user]["role"]

def delete_user(index_user: int) : 
    if index_user >= 0 and index_user < len(list_users):
        list_users.remove(list_users[index_user])

while True:
    print('''
          1. Ajouter un utilisateur
          2. Editer un profil d'utilisateur
          3. Supprimer un utilisateur
          4. Afficher les utilisateurs
          0. Quitter''')
    choix_menu = input("Merci d'indiquer votre choix : ")
    match choix_menu:
        case "1":
            print("===== Ajout d'un utilisateur =====")
            new_user = {}
            name_user = input("Merci de saisir le nom de l'utilisateur : ")
            print("===== Choix du rôle =====")
            print('''
                1 - Administrateur
                2 - Visiteur
                3 - Opérateur
            ''')
            role_user = input("Merci de saisir le rôle de l'utilisateur : ")
            match role_user : 
                case "1": 
                    role_user = "Administrateur"
                case "2": 
                    role_user = "Visiteur"
                case "3": 
                    role_user = "Opérateur"
            add_user(name_user, role_user)
        case "2":
            print("===== Edition d'un profil d'utilisateur =====")
            index_user = int(input("Merci de saisir l'index du profil utilisateur : "))
            edit_user(index_user)
        case "3":
            print("===== Suppression d'un profil utilisateur =====")
            index_user = int(input("Merci de saisir l'index du profil utilisateur : "))
            delete_user(index_user)
        case "4":
            print("===== Affichage des profils utilisateurs =====")
            for index, user in enumerate(list_users):
                print(f"------- Utilisateur n° {index} -------")
                for cle, valeur in user.items():
                    print(f"{cle} : {valeur}")
        case "0":
            break
            