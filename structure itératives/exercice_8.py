# Écrire un programme de caisse qui permet à l'utilisateur de saisir le prix de plusieurs articles un par un. 
# Lorsqu'un prix de 0 est saisi, cela signifie la fin des saisies. 
# Le programme doit ensuite afficher le total à payer, demander à l'utilisateur le montant de son paiement, et calculer et afficher la monnaie à rendre, en décomposant cette monnaie en billets de 10 euros, 5 euros, et en pièces de 1 euro.

prix_article = int(input("Prix de l'article : "))
total_article = int()

while prix_article > 0 : 
    prix_article += total_article
    prix_article = float(input("Prix de l'article : "))

print(f"Le total à payer est de : {total_article}€.")
porte_monnaie = int(input("Quel est votre montant pour régler ? "))

total_rendu_monnaie = porte_monnaie - total_article
nb_billet10 = total_rendu_monnaie % 10
nb_billet5 = 0
nb_piece = 0
if nb_billet10 % 10 != 0 : 
    nb_billet5 = nb_billet10 / 5
    print(f"Total rendu : {total_rendu_monnaie} soit {nb_billet10} de 10€, {nb_billet5} billets de 5€.")
elif nb_billet5 != 0 : 
    nb_piece = nb_billet5 / 1
    print(f"Total rendu : {total_rendu_monnaie} soit {nb_billet10} de 10€, {nb_billet5} billets de 5€ et {nb_piece} de 1€.")
else : 
    print(f"Total rendu : {total_rendu_monnaie} soit {nb_billet10} de 10€.")