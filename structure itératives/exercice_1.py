# Écrire un programme qui demande à l'utilisateur de saisir un nombre compris entre 10 et 20. 
# Tant que le nombre saisi n'est pas dans cet intervalle, le programme doit continuer à demander un nombre et indiquer si le nombre saisi est trop grand ou trop petit. 
# Lorsque l'utilisateur saisit un nombre correct, le programme se termine.

user_choice = int(input("Veuillez saisir un nombre compris entre 10 et 20 : "))
while user_choice > 20 or user_choice < 10 :
    if user_choice < 10 : 
        print(f"Le nombre {user_choice} est trop petit.")
        user_choice = int(input("Veuillez saisir un nombre compris entre 10 et 20 : "))
    elif user_choice > 20 : 
        print(f"Le nombre {user_choice} est trop grand.")
        user_choice = int(input("Veuillez saisir un nombre compris entre 10 et 20 : "))
else : 
    print(f"Le nombre {user_choice} est compris entre 10 et 20. \nFin du programme.")
    