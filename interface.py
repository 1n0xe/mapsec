import tkinter as tk
from ports import *
import time

def start_test():
    # Phase 1 : Reconnaissance et énumération
    output_text.delete("1.0", tk.END) # Efface le texte précédent de la sortie
    output_text.insert(tk.END, "// BIENVENUE SUR MAPSEC // \n")
    time.sleep(2)
    output_text.insert(tk.END, "Nous allons vous guider lors de vos pentests. Commençons dès maintenant ! :) \n\n")
    time.sleep(2)
    output_text.insert(tk.END, "Phase 1 : Reconnaissance et énumération\n")
    time.sleep(1)
    reconnaissance = reconnaissance_entry.get().lower()

    if reconnaissance == "oui":
        output_text.insert(tk.END, "Parfait ! Passons à la phase suivante.\n")
        time.sleep(1)

    elif reconnaissance == "non":
        output_text.insert(tk.END, "Il est recommandé d'effectuer la reconnaissance de la cible avant de continuer.\n")
        time.sleep(1)
        reconnaissance_now = reconnaissance_now_entry.get().lower()

        if reconnaissance_now == "oui":
            output_text.insert(tk.END, "\nPhase 1 : Reconnaissance et collecte d'informations\n\n")
            time.sleep(1)
            output_text.insert(tk.END, "Effectuez un scan de ports avec la commande suivante :\n")
            output_text.insert(tk.END, "nmap -p- -A -T4 (cible)\n")

            open_ports = get_user_input()
            suggest_actions(open_ports)
            time.sleep(1)

        elif reconnaissance_now == "non":
            output_text.insert(tk.END, "Il est important d'effectuer la reconnaissance avant de continuer.\n")
            time.sleep(1)
            arreter_test1 = arreter_test1_entry.get().lower()

            if arreter_test1 == "oui":
                output_text.insert(tk.END, "Le test a été arrêté.\n")
                return
            elif arreter_test1 == "non":
                output_text.insert(tk.END, "Le test continue. Effectuez la reconnaissance avant de continuer.\n\n")
                time.sleep(1)
                output_text.insert(tk.END, "Phase 1 : Reconnaissance et collecte d'informations\n\n")
                time.sleep(1)
                output_text.insert(tk.END, "Effectuez un scan de ports avec la commande suivante :\n")
                output_text.insert(tk.END, "nmap -p- -A -T4 (cible)\n")
                open_ports = get_user_input()
                suggest_actions(open_ports)
                time.sleep(1)

    # Phase 2 : Analyse des vulnérabilités
    output_text.insert(tk.END, "Phase 2 : Exploitation\n\n")
    time.sleep(1)
    exploitation = exploitation_entry.get().lower()

    if exploitation == "oui":
        output_text.insert(tk.END, "Parfait ! Passons à la phase suivante.\n")
        time.sleep(1)

    #elif exploitation == "non":
        output_text.insert(tk.END, "Il est recommandé d'
