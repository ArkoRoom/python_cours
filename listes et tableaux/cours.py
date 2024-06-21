# Les listes
# Les listes contiennent des elements mutables.

# un exemple de liste
first_list = ['bonjour', 'toto', 10, True]

print(first_list)

# Ajoute un element a la liste
first_list.append(50.00)

# Affiche la longueur de la liste
print(len(first_list))

# Comparer des elements d'une liste
# Attention ! Il faut que les elements de la liste soient du même type ou qu'un filtre soit créer
# first_list.sort()

# Parcourir une liste
for element in first_list : 
    print(element)

# Liste avec un index sur la longueur de la liste
for i in range(len(first_list)) : 
    print(f"index {i} : {first_list[i]}")

# Modifier un element d'une liste
second_list = [3, 4, 5, 8, 12]
print(second_list)
for i in range(len(second_list)) : 
    second_list[i] *= 3
    print(f"index {i} : {second_list[i]}")