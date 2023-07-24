import time

def get_user_input():
    ports_input = input("Entrez les ports ouverts séparés par des virgules (ex: 21,22,80): ")
    ports = list(map(int, ports_input.split(',')))
    return ports

def perform_actions(port):
    actions = []

    if port == 80:
        actions.append("Tentez un scan Nikto sur la cible avec la commande suivante : nikto -h http://(cible)/")
        actions.append("Effectuer un scan Dirb pour lister les pages ouvertes avec la commande suivante : dirb http://(cible)/")
        actions.append("Tentez d'identifier des vulnérabilités sur les applications Web avec la commande suivante : wpscan --url http://(cible)/")
    # Ajoutez d'autres conditions pour d'autres ports/protocoles

    return actions

def suggest_actions(ports):
    print("\nVoici les actions suggérées en fonction des ports ouverts :")
    for port in ports:
        actions = perform_actions(port)
        if actions:
            print(f"\nPour le port {port} :")
            for action in actions:
                print(f"  - {action}")

if __name__ == "__main__":
    # Phase 1 : Reconnaissance et collecte d'informations
    print("Phase 1 : Reconnaissance et collecte d'informations")
    time.sleep(1)
    print("Effectuez un scan de ports avec la commande suivante :")
    print("nmap -p- -A -T4 (cible)")

    open_ports = get_user_input()
    suggest_actions(open_ports)
    time.sleep(1)

    # Phase 2 : Analyse des vulnérabilités (à compléter)
    # Phase 3 : Exploitation des vulnérabilités (à compléter)
    # ...
