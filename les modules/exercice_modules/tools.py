from datetime import datetime
import os
def convertir_format_datetime_pour_log():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ajouter_log_dans_fichier(nom_fichier, description_evenement):
    if os.path.exists(nom_fichier):
        mode = 'a'
    else:
        mode = 'w'
    
    with open(nom_fichier, mode) as fichier:
        fichier.write(f"{convertir_format_datetime_pour_log()} - {description_evenement} \n")
