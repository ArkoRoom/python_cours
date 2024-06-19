# Exercice 1
# Calculez la consommation d'un datacenter par heure en Kwh
print("***** Exercice 1 *****")
consommation_kwh = float(input("Veuillez entrer la consommation (en Kwh) de votre Datacenter : "))
heures_fonctionnement = float(input("Veuillez entrer le nombre d'heures de fonctionnement de votre datacenter : "))
calcul_conso = consommation_kwh * heures_fonctionnement
print(f"Vous avez consommé {calcul_conso:.2f}Kwh aujourd'hui") 

# Exercice 2 
# Calculer le cout de refroidessiment d'un Datacenter
print("***** Exercice 2 *****")
prix_kwh = float(input("Veuillez entrer le prix du Kwh : "))
conso_heure = float(input("Veuillez entrer le cout de votre consommation par heure : "))
heure_fonctio_refroi = float(input("Veuillez entrer le nombre d'heure de fonctionnement du systeme de refroidissement : "))
calcul_cout_refroidissement = prix_kwh * conso_heure * heure_fonctio_refroi
print(f"Votre datacenter coute {calcul_cout_refroidissement:.2f}€ par jour en refroidissement.")

# Exercice 3
# Calcul du temps restant sur batterie du Datacenter
print("***** Exercice 3 *****")
energie_batterie = float(input("Veuillez entrer l'énergie stockée dans les batterie en Kwh : "))
conso_data_moyenne_heure = float(input("Veuillez entrer la consommation moyenne du datacenter par heure en Kwh : "))
calcul_temps_batterie = energie_batterie / conso_data_moyenne_heure
print(f"Le datacenter peut tenir sur batterie {calcul_temps_batterie:.2f} heures")

# Exercice 4
# Verifier si le serveur est en ligne, sans utiliser de conditions
print("***** Exercice 4 *****")
verif_maintenance = bool(input("Le serveur est-il en maintenance ? (Oui ou Non) "))
check_value = (verif_maintenance is "Oui") or (verif_maintenance is "")
print(check_value)
print("Le serveur est en maintenance : ", check_value)