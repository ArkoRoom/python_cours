import os

logs_file = "C:/Users/Administrateur/Documents/m2i_git/python_cours/TP fin de module/TP/TP 1/log_entries.txt"
choix_menu = None
logs_list = []

def read_logs(logs_file) : 
    open_folder = open(logs_file, "r")
    print(open_folder.read())

def transform_logs_in_list(logs_file) : 
    with open(logs_file, "r") as file:
        for line in file:
            log_list = [item.strip() for item in line.strip().split(",")]
            logs_list.append(log_list)
    return logs_list

def extract_failed_logs(logs_list) : 
    failed_logs = []
    for log in logs_list:
        if len(log) > 1 and log[4] == "FAILED":  # Vérifiez que le statut est à l'index correct
            failed_logs.append(log)
    return failed_logs
            

while True : 
    print('''
    1 - Consulter les logs
    2 - Consulter les logs FAILED
    3 - Consulter les IP des logs FAILED
    0 - Quitter
    ''')
    choix_menu = input("Veuillez choisir une action : ")
    match choix_menu : 
        case "1" : 
           read_logs(logs_file)
        case "2" : 
            logs_list = transform_logs_in_list(logs_file)
            failed_logs = extract_failed_logs(logs_list)
            for log in failed_logs:
                print(log)
        # case "3" : 
            # view_logs_failed()
        case "0" : 
            break
