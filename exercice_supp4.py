# Écrire un programme qui demande à l'utilisateur de saisir le nombre de photocopies effectuées. 
# Le programme doit calculer et afficher le prix à payer en fonction du nombre de photocopies, selon les règles suivantes :
# - Moins de 10 copies : 0,15 euro par copie
# - Entre 10 et 19 copies : 0,10 euro par copie
# - 20 copies et plus : 0,05 euro par copie

nombre_de_photocopie = int(input("Combien de photocopies sont imprimées ? "))

if nombre_de_photocopie < 10 : 
    print(f"Vos photocopies ont coutées {nombre_de_photocopie * 0.15}€.")
elif nombre_de_photocopie >= 10 and nombre_de_photocopie <= 19 : 
    print(f"Vos photocopies ont coutées {nombre_de_photocopie * 0.10}€.")
else : 
    print(f"Vos photocopies ont coutées {nombre_de_photocopie * 0.05}€.")