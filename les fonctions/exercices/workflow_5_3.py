# Imaginez que vous avez une liste logs de chaînes de caractères, où chaque entrée représente un message
# log du système avec son niveau de priorité (ex: "ERROR: Échec de connexion", "INFO: Maintenance prévue à
# 23h00").
# Créez une fonction filtrer_logs qui accepte un niveau de priorité et retourne une nouvelle liste contenant
# uniquement les logs de ce niveau.
# Écrivez une fonction compter_logs qui retourne le nombre de logs pour chaque niveau de priorité, en
# utilisant une compréhension de dictionnaire.

logs = ["ERROR: zerzerzer", "INFO: qssdqdqsdsqd", "WARNING:ssfsdfsdfsd", "INFO:sdfsdfds"]

def rechercher_par_niveau(niveau):
    logs_niveau = []
    for log in logs:
        if log.startswith(niveau):
            logs_niveau.append(log)
    return logs_niveau

def compter_logs():
    nombre_par_log = {}
    for log in logs:
        niveau = log.split(':')[0]
        if niveau in nombre_par_log:
            nombre_par_log[niveau] += 1
        else:
            nombre_par_log[niveau] = 1
    return nombre_par_log


### logs avec Erreur 
print(rechercher_par_niveau("ERROR"))

### logs avec info
print(rechercher_par_niveau("INFO"))

print(compter_logs())