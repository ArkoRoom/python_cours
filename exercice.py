# Exercice 1
# Calculez la consommation d'un datacenter par heure en Kwh
print("***** Exercice 1 *****")
consommation_kwh = input("Veuillez entrer la consommation (en Kwh) de votre Datacenter : ")
heures_fonctionnement = input("Veuillez entrer le nombre d'heures de fonctionnement de votre datacenter : ")
calcul_conso = float(consommation_kwh) * float(heures_fonctionnement)
print("Vous avez consommé ", calcul_conso, "Kwh aujourd'hui") 

# Exercice 2 
# Calculer le cout de refroidessiment d'un Datacenter
print("***** Exercice 2 *****")
prix_Kwh = input("Veuillez entrer le prix du Kwh : ")
conso_heure = input("Veuillez entrer le cout de votre consommation par heure : ")
heure_fonctio_refroi = input("Veuillez entrer le nombre d'heure de fonctionnement du systeme de refroidissement : ")
calcul_cout_refroidissement = float(prix_Kwh) * float(conso_heure) * float(heure_fonctio_refroi)
print("Votre datacenter coute ", calcul_cout_refroidissement, "€ par jour en refroidissement.")

# Exercice 3
# Calcul du temps restant sur batterie du Datacenter
print("***** Exercice 3 *****")
energie_batterie = input("Veuillez entrer l'énergie stockée dans les batterie en Kwh : ")
conso_data_moyenne_heure = input("Veuillez entrer la consommation moyenne du datacenter par heure en Kwh : ")
calcul_temps_batterie = float(energie_batterie) / float(conso_data_moyenne_heure)
print("Le datacenter peut tenir sur batterie ", calcul_temps_batterie, " heures")

# Exercice 4
# Verifier si le serveur est en ligne, sans utiliser de conditions
print("***** Exercice 4 *****")
verif_maintenance = input("Le serveur est-il en maintenance ?")
convert_bool = bool(verif_maintenance)
print("Le serveur est en maintenance : ", convert_bool)