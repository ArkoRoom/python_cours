#### Analyse détaillée des logs de sécurité

# Améliorer la capacité à extraire, analyser, et rapporter des données depuis des fichiers log de manière automatisée.


# 1. **Lecture et analyse des logs:**
#    - Écrivez un script Python qui lit un fichier de logs. Chaque entrée de log contient la date, l'heure, l'utilisateur, l'adresse IP source, l'action (par exemple, "login_attempt"), et le résultat ("SUCCESS" ou "FAILURE").
#    - Exemple de log: `"2023-06-25 14:22:01, john_doe, 192.168.1.1, login_attempt, FAILED"`

# 2. **Filtrage des données:**
#    - Extraites les tentatives de connexion échouées et identifiez les adresses IP qui ont des tentatives échouées répétées.
#    - Générez un rapport qui liste ces adresses IP avec le nombre de tentatives échouées et la première et dernière tentative notée.

# 3. **Visualisation:**
#    - Utilisez une bibliothèque comme `matplotlib` pour visualiser le nombre de tentatives de connexion échouées par adresse IP sur un histogramme.

# 4. **Alerte:**
#    - Si une adresse IP dépasse un certain seuil de tentatives échouées, générer une alerte formatée prête à être envoyée à une équipe de réponse aux incidents.

import os
from tools import *

logs_file = "C:/Users/Administrateur/Documents/m2i_git/python_cours/TP fin de module/TP/TP 1/log_entries.txt"
choix_menu = None

while True : 
    print('''
    1 - Consulter les logs
    2 - Consulter les logs FAILED
    3 - Consulter les IP des logs FAILED
    0 - Quitter
    ''')
    choix_menu = input("Veuillez choisir une action : ")
    match choix_menu : 
        case "1" : 
           read_logs(logs_file)
        case "2" : 
            logs_list = transform_logs_in_list(logs_file)
            failed_logs = extract_failed_logs(logs_list)
            for log in failed_logs:
                print(log)
        # case "3" : 
            # view_logs_failed()
        case "0" : 
            break