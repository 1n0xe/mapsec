# enumeration.py

def gather_information():
    print("Collecte d'informations pendant l'énumération...\n")

    # Étape 1 : Informations WHOIS
    print("1. Informations WHOIS")
    print("   Utilisez la commande 'whois' ou des outils en ligne pour récupérer les détails d'enregistrement de domaine.")
    print("   Exemple : whois exemple.com")

    # Étape 2 : Énumération DNS
    print("2. Énumération DNS")
    print("   Utilisez des outils comme 'dnsenum', 'dnsrecon' ou 'dig' pour rassembler des informations liées au DNS.")
    print("   Exemple : dnsenum exemple.com")

    # Étape 3 : Scan de réseau
    print("3. Scan de réseau")
    print("   Utilisez des outils comme 'nmap' pour repérer les hôtes actifs, les ports ouverts et les services en cours d'exécution.")
    print("   Exemple : nmap -sV -p 1-65535 exemple.com")

    # Étape 4 : Énumération de sous-domaines
    print("4. Énumération de sous-domaines")
    print("   Utilisez des outils comme 'Sublist3r', 'Amass' ou 'Subfinder' pour découvrir des sous-domaines.")
    print("   Exemple : sublist3r -d exemple.com")

    # Étape 5 : Scraping Web
    print("5. Scraping Web")
    print("   Utilisez des outils comme 'Wget' ou 'Curl' pour récupérer le contenu web et identifier les technologies utilisées.")
    print("   Exemple : wget -r -l 2 http://exemple.com")

    # Étape 6 : Réseaux Sociaux
    print("6. Réseaux Sociaux")
    print("   Vérifiez les plateformes de réseaux sociaux pour obtenir des informations publiques sur la cible.")
    print("   Recherchez les profils des employés, les annonces de l'entreprise, etc.")

    # Étape 7 : Google Dorking
    print("7. Google Dorking")
    print("   Utilisez des requêtes de recherche spécifiques sur Google (dorks) pour trouver des informations potentiellement sensibles.")
    print("   Exemple : site:exemple.com filetype:pdf")

    # Étape 8 : Recherche Shodan
    print("8. Recherche Shodan")
    print("   Utilisez Shodan pour rechercher des appareils connectés à Internet et leurs vulnérabilités.")
    print("   Exemple : shodan search exemple.com")

    # Étape 9 : Recherche Pastebin
    print("9. Recherche Pastebin")
    print("   Recherchez Pastebin pour des informations potentiellement divulguées liées à la cible.")
    print("   Exemple : site:pastebin.com exemple.com")

    # Étape 10 : Outils OSINT
    print("10. Outils OSINT")
    print("Utilisez des frameworks OSINT tels que 'Maltego', 'theHarvester' et 'SpiderFoot' pour l'automatisation de la collecte d'informations.\n")
    
    print("PENSEZ A PRENDRE DES NOTES (utilisez des outils comme Obsidian)\n")
    input("Une fois la collecte d'informations terminée, appuyez sur entrée pour passer à l'identification des services")
    

def identify_services():
    print("Identification des services pendant l'énumération...")

    # Étape 1 : Scanning des ports
    print("1. Scanning des ports")
    print("   Utilisez 'nmap' ou d'autres outils similaires pour scanner les ports ouverts.")
    print("   Exemple : nmap -p 1-65535 exemple.com")

    # Étape 2 : Identification des services
    print("2. Identification des services")
    print("   Analysez les résultats du scan pour identifier les services en cours d'exécution.")
    print("   Utilisez des outils comme 'nmap', 'Netcat' (nc), ou des scripts personnalisés.")
    print("   Exemple : nmap -sV -p 80,443 exemple.com")

    # Étape 3 : Analyse des versions
    print("3. Analyse des versions")
    print("   Utilisez les informations fournies par les outils pour déterminer les versions des services.")
    print("   Cela peut vous aider à trouver des vulnérabilités connues.")
    print("   Exemple : nmap -sV -p 80,443 exemple.com")

    # Étape 4 : Documentation
    print("4. Documentation")
    print("   Documentez les services identifiés et leurs versions pour référence future.")
    print("   Cela aidera à planifier la phase d'exploitation et à fournir des rapports.")

    print("Identification des services terminée.")
    input("Appuyez sur Entrée pour continuer...")  # Attendre l'entrée de l'utilisateur

def run_enumeration():
    print("L'énumération commence")

    gather_information()
    identify_services()

    print("Phase d'énumération complétée")

if __name__ == "__main__":
    run_enumeration()
