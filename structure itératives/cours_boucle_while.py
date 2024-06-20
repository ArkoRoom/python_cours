# Les boucles while

# On définit la valeur de i afin de ne pas créer de boucle infinie
i = 0
while(i <= 10) : 
    print(f"i : {i}")
    # On ajoute 1 à i après chaque passage
    i += 1

# On définit la valeur à toto
val = "toto"
# On rentre dans la boucle
while(val == "toto") :
    # On verifie demande à l'utilisateur si c'est toto
    val = input("toto ?")

# Controle de la sortie de boucle 
for j in range (10) :
    print(f"j : {j}")
else : 
    print("Fin de la boucle")
