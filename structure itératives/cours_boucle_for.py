# Les boucles for

# Compte jusqu'à 10 sans variable précise
for _ in range(0, 10) : 
    print("Je me répète !")

# Compte en prenant les elements du tableau
for element in [0, 1, 2, 3, 4, 5] :
    print(element)

# Compte de 0 à 10
for incr in range (10) :
    print("incr : ", incr)

# Compte de 1 à 11 sans prendre la première itération (0)
for incr1 in range (1, 11) : 
    print("incr1 : ", incr1)

# Compte toutes les 5 itérations
for i in range (0, 101, 5) :
    print("iterate : ", i)

# Compte la racine carré sur 11 ligne
for a in range (11) : 
    print(f"La puissance carré {a} est {a**2}")

# Continue et Break

# Continue permet de passer par dessus une itération en l'ignorant
# Break fait s'arrêter les itérations et stop la boucle avant son achèvement
for l in range (11) : 
    if i == 5 : 
        continue
    if i == 7 : 
        break

# Boucle dans une boucle

# La boucle se joue 3 fois avec 10 itérations par boucle
for k in range (3) :
    print(f"je suis dans la boucle {k}")
    for m in range (10): 
        print(f"m : {m}")