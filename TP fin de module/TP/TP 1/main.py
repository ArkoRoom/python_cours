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
from datetime import datetime

liste_logs = "logs.txt"

def convertir_format_date() : 
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ajouter_log_dans_fichier(liste_logs, description_evenement) :
    if os.path.exists(liste_logs) :
        mode = 'a'
    else:
        mode = 'w'
    
    with open(liste_logs, mode) as fichier :
        fichier.write(f"{convertir_format_date()} - {description_evenement} \n")