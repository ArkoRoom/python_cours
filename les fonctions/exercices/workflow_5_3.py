# Imaginez que vous avez une liste logs de chaînes de caractères, où chaque entrée représente un message
# log du système avec son niveau de priorité (ex: "ERROR: Échec de connexion", "INFO: Maintenance prévue à
# 23h00").
# Créez une fonction filtrer_logs qui accepte un niveau de priorité et retourne une nouvelle liste contenant
# uniquement les logs de ce niveau.
# Écrivez une fonction compter_logs qui retourne le nombre de logs pour chaque niveau de priorité, en
# utilisant une compréhension de dictionnaire.

liste_logs = ("ERROR : Echec de connection.", "INFO : Maintenance programmée à 23h00.", "WARN : Timed out.", "ERROR : Wrong passphrase.")

def filter_log(priority_level) : 
    for log in liste_logs : 
        if log.startswith(priority_level) : 
            print(log)

priority_level = input("Veuillez saisir la priorité que vous recherchez : ")
filter_log(priority_level)