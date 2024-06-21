# Écrire un programme de caisse qui permet à l'utilisateur de saisir le prix de plusieurs articles un par un. 
# Lorsqu'un prix de 0 est saisi, cela signifie la fin des saisies. 
# Le programme doit ensuite afficher le total à payer, demander à l'utilisateur le montant de son paiement, et calculer et afficher la monnaie à rendre, en décomposant cette monnaie en billets de 10 euros, 5 euros, et en pièces de 1 euro.

total_prix_article = 0.0

print("Merci de saisir les prix des articles un par un. Entrez")
while True : 
    prix = float(input("Prix de l'article (en euros) : "))
    if prix == 0 : 
        break
    if prix > 0 : 
        total_prix_article += prix
    else : 
        print("Merci de saisir un prix positif.")

print(f"Total à payer : {total_prix_article:2f}€")

montant_paye = float(input("Merci de saisir le montant que vous payez (en euros) : "))

if montant_paye >= total_prix_article : 
    monnaie = montant_paye - total_prix_article
    billets_de_10 = int(monnaie // 10)
    billets_de_5 = int(monnaie // 5)
    monnaie = monnaie % 5
    pieces_de_1 = int(monnaie)

    print(f"Monnaie à rendre : {montant_paye - total_prix_articles:.2f}euros")
    print(f"Billets de 10 euros : {billets_de_dix}")
    print(f"Billets de 5 euros : {billets_de_cinq}")
    print(f"pièce de 1 euro : {pieces_de_un}")
else:
    print("Le montant payé doit être plus grand que le total des articles")