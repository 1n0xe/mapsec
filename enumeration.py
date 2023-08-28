# enumeration.py

def gather_information():
    print("Collecte d'informations pendant l'énumération...\n")
    text1 = "1. Énumération DNS"
    formatted_text1 = "\033[1m\033[4m" + text1 + "\033[0m"
    # Étape 1 : Énumération DNS
    print(formatted_text1)
    print("   Utilisez des outils comme 'dnsenum', 'dnsrecon' ou 'dig' pour rassembler des informations liées au DNS.")
    text2 = "2. Scan de réseau"
    formatted_text2 = "\033[1m\033[4m" + text2 + "\033[0m"
    # Étape 2 : Scan de réseau
    print(formatted_text2)
    print("   Utilisez des outils comme 'nmap' pour repérer les hôtes actifs, les ports ouverts et les services en cours d'exécution.")
    text3 = "3. Énumération de sous-domaines"
    formatted_text3 = "\033[1m\033[4m" + text3 + "\033[0m"
    # Étape 3 : Énumération de sous-domaines
    print(formatted_text3)
    print("   Utilisez des outils comme 'Sublist3r', 'Amass' ou 'Subfinder' pour découvrir des sous-domaines.")
    text4 = "4. Scraping Web"
    formatted_text4 = "\033[1m\033[4m" + text4 + "\033[0m"
    # Étape 4 : Scraping Web
    print(formatted_text4)
    print("   Utilisez des outils comme 'Wget' ou 'Curl' pour récupérer le contenu web et identifier les technologies utilisées.")
    text5 = "5. Google Dorking"
    formatted_text5 = "\033[1m\033[4m" + text5 + "\033[0m"
    # Étape 5 : Google Dorking
    print(formatted_text5)
    print("   Utilisez des requêtes de recherche spécifiques sur Google (dorks) pour trouver des informations potentiellement sensibles.")
    text6 = "6. Outils OSINT"
    formatted_text6 = "\033[1m\033[4m" + text6 + "\033[0m"
    # Étape 6 : Outils OSINT
    print(formatted_text6)
    print("Utilisez des frameworks OSINT tels que 'Maltego', 'theHarvester' et 'SpiderFoot' pour l'automatisation de la collecte d'informations.\n")
    
    print("PENSEZ A PRENDRE DES NOTES (utilisez des outils comme Obsidian)\n")
    input("Une fois la collecte d'informations terminée, appuyez sur entrée pour passer à l'identification des services")
    

def identify_services():
    print("Identification des services pendant l'énumération...\n")
    text7 = "1. Scanning des ports"
    formatted_text7 = "\033[1m\033[4m" + text7 + "\033[0m"
    # Étape 1 : Scanning des ports
    print(formatted_text7)
    print("   Utilisez 'nmap' ou d'autres outils similaires pour scanner les ports ouverts.")
    text8 = "2. Identification des services"
    formatted_text8 = "\033[1m\033[4m" + text8 + "\033[0m"
    # Étape 2 : Identification des services
    print(formatted_text8)
    print("   Analysez les résultats du scan pour identifier les services en cours d'exécution.")
    print("   Utilisez des outils comme 'nmap', 'Netcat' (nc), ou des scripts personnalisés.")
    text9 = "3. Analyse des versions"
    formatted_text9 = "\033[1m\033[4m" + text9 + "\033[0m"
    # Étape 3 : Analyse des versions
    print(formatted_text9)
    print("   Utilisez les informations fournies par les outils comme nmap pour déterminer les versions des services.")
    print("   Cela peut vous aider à trouver des vulnérabilités connues.")
    text10 = "4. Documentation"
    formatted_text10 = "\033[1m\033[4m" + text10 + "\033[0m"
    # Étape 4 : Documentation
    print(formatted_text10)
    print("   Documentez les services identifiés et leurs versions pour référence future.")
    print("   Cela aidera à planifier la phase d'exploitation et à fournir des rapports.\n")

    print("Identification des services terminée.")
    input("Appuyez sur Entrée pour continuer...")

def run_enumeration():
    print("L'énumération commence")

    gather_information()
    identify_services()

    print("Phase d'énumération complétée")

if __name__ == "__main__":
    run_enumeration()
