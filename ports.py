import time


#CHOIX DES PORTS PAR L'UTILISATEUR
def get_user_input():
    ports_input = input("Entrez les ports ouverts que vous avez trouvés séparés par des virgules (ex: 21,22,80): ")
    ports = list(map(int, ports_input.split(',')))
    return ports

#PORTS
def perform_actions(port):
    actions = []
    if port == 80:
        actions.append("Tentez un scan Nikto sur la cible avec la commande suivante : nikto -h http://(cible)/")
        actions.append("Effectuer un scan Dirb pour lister les pages ouvertes avec la commande suivante : dirb http://(cible)/")
        actions.append("Tentez d'identifier des vulnérabilités sur les applications Web avec la commande suivante : wpscan --url http://(cible)/")
    # Ajoutez d'autres conditions pour d'autres ports/protocoles

    if port == 21:
        actions.append("Tentez un bruteforce de logins avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) ftp")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search ftp")

    if port == 22:
        actions.append("Tentez un bruteforce de logins avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) ssh")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search ssh")

    if port == 23:
        actions.append("Tentez un bruteforce de logins avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) telnet")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search telnet")

    if port == 25:
        actions.append("Tentez un bruteforce de logins avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) smtp")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search smtp")
        actions.append("Tentez une attaque phishing avec la commande : setoolkit puis l'option 1 et configurez votre mail frauduleux")

    if port == 53:
        actions.append("Tentez un DNS Cache Poisoning : dnschef --interface (interface) --fakeip (fake_ip) --nameserver (dns_server) --domain (target_domain)")
        actions.append("Tentez un DNS Zone Transfer : dig @(target_dns_server) (domain) AXFR")
        actions.append("Tentez un DNS Brute Forcing : fierce -dns (target_domain)")

    if port == 80:
        actions.append("Tentez un scan Nikto sur la cible avec la commande suivante : nikto -h http://(cible)/")
        actions.append("Effectuer un scan Dirb pour lister les pages ouvertes avec la commande suivante : dirb http://(cible)/")
        actions.append("Tentez d'identifier des vulnérabilités sur les applications Web avec la commande suivante : wpscan --url http://(cible)/")

    if port == 110:
        actions.append("Tentez un bruteforce de logins avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) pop3")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search pop3")

    if port == 135:
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search dcerpc")
        actions.append("Lancez un scan de vulnérabilités ciblant le port 135 à l'aide de l'interface Web ou de la ligne de commande d'OpenVAS")

    if port == 139:
        actions.append("Recherche de partages SMB accessibles ou mal configurés sur les systèmes Windows avec : enum4linux -S (target_ip)")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search netbios ou search smb")
        actions.append("Tentez un bruteforce de partage SMB avec : hydra -L (user_list) -P (password_list) smb://(target_ip)")

    if port == 143:
        actions.append("Tentez un bruteforce de logins avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) imap")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search imap")

    if port == 443:
        actions.append("Lancer un scan de vulnérabilités avec : nikto -h https://(target_ip)")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search ssl ou search tls")
        actions.append("Tentez un bruteforce de logins web avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) https-post-form '/path/to/login:username_field=^USER^&password_field=^PASS^:login_failed_message'")
        actions.append("Analyser les certificats SSL/TLS avec la commande : openssl s_client -connect (target_ip):443")

    if port == 445:
        actions.append("Enumerer les partages SMB avec la commande : smbclient -L //(target_ip)/ -U%")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search smb")
        actions.append("Scannez les vulnérabilités avec nmap : nmap -p 445 --script smb-vuln-* (target_ip)")
        actions.append("Tentez un bruteforce de partage SMB avec : hydra -L (user_list) -P (password_list) smb://(target_ip)")

    if port == 3306:
        actions.append("Tentez un bruteforce de logins avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) mysql")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search mysql")
        actions.append("Tentez une injection SQL avec la commande suivante : sqlmap -u 'https://(target_url)/path/to/vulnerable/page?parameter=value' --dbs")
        actions.append("Enumérer les utilsiateurs et les bases de données avec nmap : nmap -p 3306 --script mysql-enum (target_ip)")

    if port == 3389:
        actions.append("Tentez un bruteforce de logins avec la commande suivante : hydra -t 1 -l (user) -P (password_list) rdp://(target_ip)")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search rdp")
        actions.append("Scannez les vulnérabilités avec nmap : nmap -p 3389 --script 'rdp-*' (target_ip)")

    if port == 8080:
        actions.append("Tentez un scan Nikto sur la cible avec la commande suivante : nikto -h http://(cible):8080/")
        actions.append("Tentez une injection SQL avec la commande suivante : sqlmap -u 'http://(target_url):8080/path/to/vulnerable/page?parameter=value' --dbs")
        actions.append("Tentez un bruteforce de logins web avec la commande suivante : hydra -l (user) -P (password_list) (target_ip) http-post-form '/path/to/login:username_field=^USER^&password_field=^PASS^:login_failed_message' -s 8080")
        actions.append("Tentez une recherche metasploit avec la commande suivante : msfconsole puis recherchez des vulnérabilités avec : search http")
        actions.append("Utiliser BurpSuite pour analyser une potentielle vulnérabilité XSS")

    return actions


def suggest_actions(ports):
    print("\nVoici les actions suggérées en fonction des ports ouverts :")
    for port in ports:
        actions = perform_actions(port)
        if actions:
            print(f"\nPour le port {port} :")
            for action in actions:
                print(f"  - {action}")
