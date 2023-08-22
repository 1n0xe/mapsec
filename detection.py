# detection.py

def run_detection():
    print("Recherche de vulnérabilités en cours de détection...")

    # Étape 1 : Demander les ports trouvés précédemment
    input_ports = input("Entrez les ports trouvés précédemment (séparés par des virgules) : ")
    ports = [int(port.strip()) for port in input_ports.split(",")]

    # Étape 2 : Résultats personnalisés pour les ports les plus utilisés
    print("Analyse des vulnérabilités pour les ports trouvés :")
    for port in ports:
        if port in common_ports:
            vulnerabilities = get_vulnerabilities(port)
            print(f"Port {port} - Vulnérabilités potentielles : {', '.join(vulnerabilities)}")
        else:
            print(f"Port {port} - Pas de vulnérabilité connue")

    print("Recherche de vulnérabilités terminée.")
    input("Appuyez sur Entrée pour continuer...")  # Attendre l'entrée de l'utilisateur

# Liste des ports courants lors d'un pentest
common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 8080, 3306, 1433, 1521, 5900, 5432, 6379, 27017, 11211]

# Fonction pour obtenir les vulnérabilités potentielles d'un port donné (pour l'exemple)
def get_vulnerabilities(port):
    vulnerabilities = {
        21: ["Vuln1", "Vuln2"],
        22: ["Vuln3"],
        80: ["Vuln4", "Vuln5"],
        # Ajoutez plus de vulnérabilités pour les autres ports
    }
    return vulnerabilities.get(port, [])
