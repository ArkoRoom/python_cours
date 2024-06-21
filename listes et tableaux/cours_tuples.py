# Les Tuples
# Les tuples peyvent contenir tout types de données
# Ils ne peuvent en revanche pas etre modifier
# Les set() permettent d'optimiser les performances car ils respectent l'ordonnée mémoire

# Exemple de tuple
first_tuple = "toto", "tata", "tutu"

# Parcours le tuple
for el in first_tuple : 
    print(el)

# la fonction set() permet d'ajouter un element a un tuple mais ne permet pas d'obtenir de doublon
first_set = set()
first_set.add("element 1")
first_set.add(True)
first_set.add(10)
for el in first_set : 
    print(el)
    print(id(el))



