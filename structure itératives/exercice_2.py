# Écrire un programme qui demande à l'utilisateur de saisir un nombre de départ. 
# Le programme doit ensuite afficher les 10 nombres suivants ce nombre de départ.
 
start_number = int(input("Veuillez saisir un nombre de départ : "))
for start_number in range(start_number, start_number + 10) : 
    start_number += 1
    print(f"Nombre : {start_number}")
    