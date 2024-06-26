from collections import defaultdict
from datetime import datetime

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

def count_ip_occurrences(failed_logs) : 
    ip_count = defaultdict(int)
    ip_list = []
    first_occurrence = {}
    last_occurrence = {}
    
    for log in failed_logs :
        if len(log) > 3 :
            ip_address = log[4]
            timestamp = log[0]
            
            if not isinstance(timestamp, datetime) :
                timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            
            ip_count[ip_address] += 1
            
            if ip_address not in ip_list:
                ip_list.append(ip_address)
            
            if ip_address not in first_occurrence:
                first_occurrence[ip_address] = timestamp
            
            last_occurrence[ip_address] = timestamp
    
    for ip in ip_list :
        print(f"IP: {ip}")
        print(f"  Première occurrence: {first_occurrence[ip]}")
        print(f"  Dernière occurrence: {last_occurrence[ip]}")
    
    return ip_count, ip_list
