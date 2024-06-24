# Définissez une liste globale taches_maintenance où chaque élément est un tuple contenant l'ID de la tâche,
# la description, et le statut ("En cours", "Terminé").
# Créez une fonction ajouter_tache pour ajouter une nouvelle tâche à la liste, en s'assurant que l'ID est
# unique.
# Implémentez une fonction mettre_a_jour_tache qui change le statut d'une tâche basée sur son ID.

tache_maintenance = []

def ajouter_tache(id: int, desc: str, statut: str) : 
    if desc == '':
        print("Erreur. Description ne peut être vide.")
    
    if statut != '':
        match statut :
            case "1":
                statut = "En cours"
            case "2": 
                statut = "Terminée"
            case "3":
                statut = "Non commencée"
    else : 
        print("Erreur. Statut ne peut être vide.")
    if rechercher_par_id(id) is None : 
        tache_maintenance.append((id, desc, statut))
    print(tache_maintenance)

def rechercher_par_id(id) : 
    tache_trouve = None
    for tache in tache_maintenance : 
        if tache[0] == id : 
            tache_trouve = tache
            break
        return tache_trouve
    
def mettre_a_jour_tache(id, desc, statut) : 
    tache = rechercher_par_id(id)
    if tache is not None : 
        tache_maintenance[tache_trouve[1]] = (id, desc, statut)

while True : 
    print('''
        1 - Ajouter une tâche
        2 - Modifier le statut d'une tâche
        3 - Afficher les tâches
        0 - Quitter
    ''')
    choix_menu = input("Merci d'indiquer votre choix : ")
    match choix_menu : 
        case "1":
            id = int(input("Veuillez saisir un nombre : "))
            desc = input("Veuillez saisir la description de la tâche : ")
            print('''
                1 - En cours
                2 - Terminée
                3 - Non commencée
            ''')
            statut = (input("Veuillez saisir l'état de la tâche : "))
            ajouter_tache(id, desc, statut)
        case "3":
            print("===== Liste des tâches =====")
            for i in enumerate(tache_maintenance) :
                print(f"***** Tache n°{i} *****")
                print(tache_maintenance)
                for j in tache_maintenance[i] : 
                    print(f"{j}")
        case "0": 
            break

print(tache_maintenance)
