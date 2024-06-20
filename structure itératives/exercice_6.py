# Écrire un programme qui demande à l'utilisateur de saisir 20 nombres. 
# Le programme doit ensuite déterminer et afficher le plus grand de ces nombres ainsi que sa position (le numéro d'entrée).

count = 1
old_count = 1
previous_number = int(input("Veuillez saisir un chiffre : "))
while count < 5 : 
    new_number = int(input("Veuillez saisir un chiffre : "))
    count += 1
    if new_number > previous_number : 
        previous_number = new_number
        old_count = count
    else : 
        previous_number = previous_number
        old_count = old_count

if count == 5 :
    print(f"Le plus grand chiffre est : {previous_number} en position {old_count}")                                                                                                   