from ports import *
import time

if __name__ == "__main__":
    # Phase 1 : Reconnaissance et énumération
    print(" // BIENVENUE SUR MAPSEC // ")
    time.sleep(2)
    print("Nous allons vous guider lors de vos pentests. Commençons dès maintenant ! :) ")
    time.sleep(2)
    print()
    print("Phase 1 : Reconnaissance et énumération")
    time.sleep(1)
    print("Avez-vous effectué la reconnaissance de la cible ?")
    reconnaissance = input("Répondez par Oui ou Non : ")

    if reconnaissance.lower() == "oui":
        print("Parfait ! Passons à la phase suivante.")
        time.sleep(1)

    elif reconnaissance.lower() == "non":
        print("Il est recommandé d'effectuer la reconnaissance de la cible avant de continuer.")
        time.sleep(1)
        print("Souhaitez-vous effectuer la reconnaissance maintenant ?")
        reconnaissance_now = input("Répondez par Oui ou Non : ")

        if reconnaissance_now.lower() == "oui":
            print()
            print("Phase 1 : Reconnaissance et collecte d'informations")
            print()
            time.sleep(1)
            print("Effectuez un scan de ports avec la commande suivante :")
            print("nmap -p- -A -T4 (cible)")

        elif reconnaissance_now.lower() == "non":
            print("Il est important d'effectuer la reconnaissance avant de continuer.")
            time.sleep(1)
            print("Voulez-vous arrêter le test ?")
            arreter_test1 = input("Répondez par Oui ou Non : ")

            if arreter_test1.lower() == "oui":
                print("Le test a été arrêté.")
                exit()
            elif arreter_test1.lower() == "non":
                print("Le test continue. Effectuez la reconnaissance avant de continuer.")
                print()
                print("Phase 1 : Reconnaissance et collecte d'informations")
                print()
                time.sleep(1)
                print("Effectuez un scan de ports avec la commande suivante :")
                print("nmap -p- -A -T4 (cible)")
                open_ports = get_user_input()
                suggest_actions(open_ports)
                time.sleep(1)

    # Phase 2 : Analyse des vulnérabilités
    print()
    print("Phase 2 : Analyse des vulnérabilités")
    print()
    time.sleep(1)
    print("Avez-vous identifié des vulnérabilités sur la cible ?")
    exploitation = input("Répondez par Oui ou Non : ")

    if exploitation.lower() == "oui":
        print("Parfait ! Passons à la phase suivante.")
        time.sleep(1)

    elif exploitation.lower() == "non":
        print("Il est recommandé d'analyser les vulnérabilités identifiées avant de continuer.")
        time.sleep(1)
        open_ports = get_user_input()
        suggest_actions(open_ports)
        time.sleep(1)


    # Phase 3 : Exploitation des vulnérabilités (à compléter)
    print()
    print("Phase 3 : Exploitation des vulnérabilités")
    print()
    time.sleep(1)
    print("Avez-vous réussi à exploiter les vulnérabilités sur la cible ?")
    exploitation = input("Répondez par Oui ou Non : ")

    if exploitation.lower() == "oui":
        print("Parfait ! Passons à la phase suivante.")
        time.sleep(1)

    elif exploitation.lower() == "non":
        print()
        print("Veuillez faire référence aux conseils donnés ci-dessus en fonction de vos ports ouverts")
        time.sleep(1)

    # Phase 4 : Post-exploitation
    print()
    print("Phase 4 : Post-Exploitation")
    print()
    time.sleep(1)
