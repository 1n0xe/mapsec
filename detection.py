# detection.py

def run_detection():
    print("Démarrage de la phase de détection...")
    
    # Demande à l'utilisateur d'entrer les ports identifiés précédemment
    input_ports = input("Entrez les ports identifiés précédemment (séparés par des virgules) : ")
    identified_ports = [int(port.strip()) for port in input_ports.split(",")]

    print("Ports identifiés précédemment :", identified_ports)
    print("\nOutils de détection :")
    print("\n(Valable pour tous les ports : chercher des vulnérabilités de version avec Searchsploit)")
    
    for port in identified_ports:
        print("\nPort:", port)
        detection_tools = get_detection_tools(port)
        if detection_tools:
            print("\n   Outils de détection suggérés :", ", ".join(detection_tools))
        else:
            print("   Aucun outil de détection suggéré pour ce port.")
    
    print("\nPhase de détection terminée.")

# Liste des ports courants lors d'un pentest
common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 8080, 3306, 1433, 1521, 5900, 5432, 6379, 27017, 11211]

# Fonction pour obtenir les outils de détection suggérés pour un port donné
def get_detection_tools(port):
    detection_tools = {
        21: ["Nessus", "OpenVAS", "Nmap", "Metasploit"],
        22: ["Nessus", "OpenVAS", "Nmap", "Metasploit"],
        23: ["Nessus", "OpenVAS", "Nmap"],
        25: ["Nessus", "OpenVAS", "Nmap"],
        53: ["Nessus", "OpenVAS", "Nmap"],
        80: ["Nikto", "OWASP ZAP", "Nessus", "OpenVAS", "Nmap"],
        110: ["Nessus", "OpenVAS", "Nmap"],
        139: ["Nessus", "OpenVAS", "Nmap"],
        443: ["SSLScan", "SSLyze", "Nessus", "OpenVAS", "Nmap"],
        445: ["Nessus", "OpenVAS", "Nmap"],
        3389: ["Nessus", "OpenVAS", "Nmap", "Metasploit"],
        8080: ["Nikto", "OWASP ZAP", "Nessus", "OpenVAS", "Nmap"],
        3306: ["Nessus", "OpenVAS", "Nmap", "SQLMap"],
        1433: ["Nessus", "OpenVAS", "Nmap", "SQLMap"],
        1521: ["Nessus", "OpenVAS", "Nmap"],
        5900: ["Nessus", "OpenVAS", "Nmap"],
        5432: ["Nessus", "OpenVAS", "Nmap", "SQLMap"],
        6379: ["Nessus", "OpenVAS", "Nmap"],
        27017: ["Nessus", "OpenVAS", "Nmap"],
        11211: ["Nessus", "OpenVAS", "Nmap"]
    }
    return detection_tools.get(port, [])

if __name__ == "__main__":
    run_detection()
