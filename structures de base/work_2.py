# Exercice 1 
# Allouer de la bande passante selon les priorités
print("***** Exercice 1 *****")
total_bande_passante = float(input("Veuillez saisir le total de la bande passante : "))
priorite_web = int(input("Priorité pour le service Web (entre 1 et 3) : "))
priorite_mail = int(input("Priorité pour le service Mail (entre 1 et 3) : "))
priorite_bdd = int(input("Priorité pour le service BDD (entre 1 et 3) : "))
bande_web = float(input("Combien de Gbps vous faut-il ? "))
bande_mail = float(input("Combien de Gbps vous faut-il ? "))
bande_bdd = float(input("Combien de Gbps vous faut-il ? "))
cumul_bande_passante = bande_web + bande_mail + bande_bdd
bande_moitie = total_bande_passante / 2
bande_tier_reste = bande_moitie / 3
bande_deux_tiers = bande_tier_reste * 2

if total_bande_passante >= cumul_bande_passante : 
    print("La bande passante totale est suffisante")
else : 
    print("La bande passante va être répartie proportionnellement")

if total_bande_passante <= cumul_bande_passante : 
    match priorite_web : 
        case 1 :
            print(f"Le service Web reçoit {bande_moitie} de bande passante.")
        case 2 : 
            print(f"Le service Web reçoit {bande_deux_tiers} de bande passante.")
        case 3 : 
            print(f"Le service Web reçoit {bande_tier_reste} de bande passante. ")

    match priorite_mail : 
        case 1 :
            print(f"Le service Mail reçoit {bande_moitie} de bande passante.")
        case 2 : 
            print(f"Le service Mail reçoit {bande_deux_tiers} de bande passante.")
        case 3 : 
            print(f"Le service Mail reçoit {bande_tier_reste} de bande passante. ")

    match priorite_bdd : 
        case 1 :
            print(f"Le service BDD reçoit {bande_moitie} de bande passante.")
        case 2 : 
            print(f"Le service BDD reçoit {bande_deux_tiers} de bande passante.")
        case 3 : 
            print(f"Le service BDD reçoit {bande_tier_reste} de bande passante. ")
else : 
    print(f"Il reste {total_bande_passante - cumul_bande_passante} Gbps.")
    match priorite_web : 
        case 1 :
            print(f"Le service Web reçoit {bande_web} de bande passante.")
        case 2 : 
            print(f"Le service Web reçoit {bande_web / 2} de bande passante.")
        case 3 : 
            print(f"Le service Web reçoit {bande_web / 6} de bande passante. ")

    match priorite_mail : 
        case 1 :
            print(f"Le service Mail reçoit {bande_mail} de bande passante.")
        case 2 : 
            print(f"Le service Mail reçoit {bande_mail / 2} de bande passante.")
        case 3 : 
            print(f"Le service Mail reçoit {bande_mail / 6} de bande passante. ")

    match priorite_bdd : 
        case 1 :
            print(f"Le service BDD reçoit {bande_bdd} de bande passante.")
        case 2 : 
            print(f"Le service BDD reçoit {bande_bdd / 2} de bande passante.")
        case 3 : 
            print(f"Le service BDD reçoit {bande_bdd / 6} de bande passante. ")