# Écrire un programme qui demande à l'utilisateur de saisir un nombre entier. 
# Le programme doit vérifier si ce nombre est divisible par 3 et afficher un message approprié.

nombre_entier = int(input("Veuillez saisir un nombre entier : "))

if nombre_entier % 3 == 0 : 
    print(f"Le nombre {nombre_entier} est disible par 3")
else : 
    print(f"Le nombre {nombre_entier} n'est pas disible par 3")