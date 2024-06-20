# Écrire un programme qui demande à l'utilisateur de saisir 20 nombres. 
# Le programme doit ensuite déterminer et afficher le plus grand de ces nombres.

count = 1
previous_number = int(input("Veuillez saisir un chiffre : "))
while count < 5 : 
    count += 1
    new_number = int(input("Veuillez saisir un chiffre : "))
    if new_number > previous_number : 
        previous_number = new_number
    else : 
        previous_number = previous_number

if count == 5 :
    print(f"Le plus grand chiffre est : {previous_number}")