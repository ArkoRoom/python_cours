def read_logs(logs_file) : 
    open_folder = open(logs_file, "r")
    print(open_folder.read())

def transform_logs_in_list(logs_file) : 
    logs_list = []
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
