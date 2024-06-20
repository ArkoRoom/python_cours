# Écrire un programme qui permet de tester si un profil est valable pour 
# une candidature ou non selon ces trois critères :
# - L’âge minimum pour le poste est 30 ans
# - Le salaire maximum possible est 40 000 euros
# - Le nombre d’années d’expérience minimum est de 5 ans.
# - On affichera différents messages pour chaque condition non 
# respectée.
# - Il est possible de réaliser cet exercice avec une seule structure 
# conditionnelle ne comportant qu’une condition par clause (pas de 
# and/or)

age_candidat = int(input("Veuillez indiquer votre âge : "))
salaire_candidat = int(input("Veuillez entrer le salaire que vous demandez pour le poste : "))
experiences_candidat = int(input("Veuillez indiquer votre nombre d'années d'expériences : "))

if age_candidat < 30 : 
    print("Votre âge ne convient pas pour ce poste.")
elif salaire_candidat > 40000 : 
    print("Le salaire demandé pour ce poste est trop élevé.")
elif experiences_candidat < 5 : 
    print("Vous n'avez pas l'experience requise pour ce poste.")
else : 
    print("Vous êtes embauché !")

if age_candidat < 30 and age_candidat > 18 : 
    print("Votre âge ne convient pas pour ce poste.")
elif salaire_candidat > 40000 : 
    print("Le salaire demandé pour ce poste est trop élevé.")
elif experiences_candidat < 5 : 
    print("Vous n'avez pas l'experience requise pour ce poste.")
else : 
    print("Vous êtes embauché !")