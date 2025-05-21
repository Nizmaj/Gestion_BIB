from Fonctions.gestion_livres import *
from Fonctions.gestion_lecteurs import *
from Fonctions.suivi_emprunt import *

while True:
        print("1- Ajouter un livre")
        print("2- Supprimer un livre")
        print("3- Mettre à jour un livre")
        print("4- Ajouter un lecteur")
        print("5- Supprimer un lecteur")
        print("6- Mettre à jour un lecteur")
        print("7- Ajouter un emprunt")
        print("8- Supprimer un emprunt")
        print("9- afficher la liste des livres empruntés")
        print("10-afficher la liste des livres disponibles")
        
        entrée = input("entrée : ")

        if entrée == "1":
            ajout_livre()
        elif entrée == "2":
            supprimer_livre()
        elif entrée == "3":
            update_livre()
        elif entrée == "4":
            ajout_lecteur()
        elif entrée == "5":
            supprimer_lecteur()
        elif entrée == "6":
            update_lecteur(lecteurs)
        elif entrée == "7":
            ajout_emprunt()
        elif entrée == "8":
            supprimer_emprunt()
        elif entrée == "9":
            affiche_emprunts()
        elif entrée == "10":
            print(livres_dispo())
        elif entrée == "0":
            print("Au revoir !")
            break
        else:
            print("Erreur")

