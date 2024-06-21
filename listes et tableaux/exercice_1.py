# Exercice Liste
# - Via l'utilisation d'une variable de type **liste**, vous devrez réaliser un logiciel permettant à l'utilisateur d'entrer une **série de notes**, dont le nombre possible à entrer sera soit (au choix de l'utilisateur) : 
# - saisie avant la saisie de notes 
# - permissif et pourra aller jusqu'à entrer une note négative qui stoppera la saisie des notes. 
# - Une fois la **saisie des notes terminée**, l'utilisateur aura à sa disposition un **affichage** lui permettant d'avoir la **note max**, la **note min** ainsi que la **moyenne** (possible de faire un menu pour choisir) 

liste_notes = []
note_minimum = 0
note_maximum = 0
choix_menu = None

while True:
    print('''
          1 - Ajouter une note
          2 - Afficher les notes
          3 - Afficher la plus grande note
          4 - Afficher la plus petite note
          5 - Afficher la moyenne
          0 - Quitter
    ''')
    choix_menu = input("Merci d'indiquer votre choix : ")
    match choix_menu:
        case "1":
            note = int(input("Merci de saisir une note : "))
            if note >= 0 and note <= 20:
                liste_notes.append(note)
            else:
                print("Merci de saisir une note entre 0 et 20")
        case "2":
            print("==== Liste des notes ====")
            for note in liste_notes:
                print(f"Note : {note}")
        case "3":
            if len(liste_notes) > 0:
                note_maximum = liste_notes[0]
                for i in range(1, len(liste_notes)):
                    if liste_notes[i] >note_maximum:
                        note_maximum = liste_notes[i]
                print(f"La note max est {note_maximum}")
            else: 
                print("Aucune note")
        case "4":
            if len(liste_notes) > 0:
                note_minimum = liste_notes[0]
                for i in range(1, len(liste_notes)):
                    if liste_notes[i] < note_minimum:
                        note_minimum = liste_notes[i]
                print(f"La note min est {note_minimum}")
            else: 
                print("Aucune note")
        case "5":
            if len(liste_notes) > 0:
                somme_note = 0
                for i in range(0, len(liste_notes)):
                    somme_note += liste_notes[i]
                print(f"La moyenne est {somme_note / len(liste_notes)}")
            else: 
                print("Aucune note")
        case "0":
            break
