from tools import ajouter_log_dans_fichier

while True:
    evenement = input("Merci de saisir l'evenement : ")
    if evenement == "0":
        break
    else:
        ajouter_log_dans_fichier("log.txt", evenement)