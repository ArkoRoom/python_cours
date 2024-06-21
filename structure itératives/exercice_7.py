# Écrire un programme qui demande à l'utilisateur de saisir un nombre de départ. 
# Le programme doit ensuite calculer et afficher la factorielle de ce nombre.

while True : 
    start_number = int(input("Veuillez saisir un nombre : "))
    if start_number < 0 : 
        print("Erreur de saisi. Veuillez saisir un chiffre supérieur ou égal à zéro.")
    else : 
        break

if start_number == 0 : 
    result = 1
elif start_number > 0 : 
    result = 1 
    for i in range(1, start_number + 1) : 
        result *= i
print(f"Le factorielle de {start_number} est : {result}")