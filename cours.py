print("hello world")

ma_recuperation = input ("veuillez saisir une valeur : ")
print("vous avez entrez :", ma_recuperation)

# Les numériques
var_int = 25
var_float = 25.02
print(var_int, ", ", var_float)

# Typing
print(type(var_int))

# Les booléens
var_bool = True
print(var_bool)

# Conditions dans les print
print(4 > 5) # return false
print(4 >= 5) # return False
print(4 == 5) # return False
print(4 != 5) # return True

# Concatenation
var_chaine1 = "chaine 1"
var_chaine2 = "chaine 2"
var_concat = var_chaine1 + " " + var_chaine2
print(var_concat)

# Forcer ou changer le typing
My_age = 35
My_message = "Voici mon age : "
print(My_message + str(My_age))

# Concat avec .format()
Firstname = "Toto"
msg_firstname = "Je m'apelle {0} et j'ai {1} ans.".format(Firstname, My_age)
print(msg_firstname)

# Calcul dans un print
# **2 = carré
# **3 = cube
var1 = 12
print("{0:2d} {1:3d} {2:4d}".format(var1, var1**2, var1**3))