#!/usr/bin/python3
import sqlite3
import re
from utils import db
from tabulate import tabulate

'''
def menu_principal(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Creation d'un menu principal
        print("""Menu principal:
a)Affichage 
m)Modification
i)Infos sur le sujet
q)Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "a":
            reponse_valide = True
            menu_affichage(connexion)

        elif user_reponse == "m":
            reponse_valide = True
            menu_modification(connexion)

        elif user_reponse == "i":
            reponse_valide = True
            print("Sujet principal:")
            infos_sur_sujet(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('a','m','i','q')\n")

'''


def menu_principal(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Menu principal
        print("""Menu principal:
a) Affichage 
m) Modification
i) Infos sur le sujet
q) Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "a":
            reponse_valide = True
            menu_affichage(connexion)

        elif user_reponse == "m":
            reponse_valide = True
            menu_modification(connexion)

        elif user_reponse == "i":
            reponse_valide = True
            print("Sujet principal:")
            infos_sur_sujet(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('a','m','i','q')\n")


def menu_affichage(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Menu intermédiaire avant le menu d'affichage
        print("""Menu affichage:
1)Listes de toutes les informations de chaque classe
2)Informations personnalisées
r)Revenir au menu principal
q)Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "1":
            reponse_valide = True
            menu_affichage_tous(connexion)

        elif user_reponse == "2":
            reponse_valide = True
            menu_custom(connexion)

        elif user_reponse == "r":
            reponse_valide = True
            menu_principal(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('1','2', r','q')\n")


def menu_affichage_tous(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Creation d'un menu principal
        print("""Menu affichage:
1)Liste de tous les balayeurs avec leurs infos 
2)Liste de tous les quartiers avec leurs infos
3)Liste de tous les camions à ordure avec leurs infos
4)Liste de tous les models de camion à ordure avec leurs infos
5)Liste de tous les centres à ordure avec leurs infos
6)Liste de tous les programmations avec leurs infos
r)Revenir à la menu précédente
q)Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "1":
            reponse_valide = True
            select_tous_les_balayeurs_infos(connexion)

        elif user_reponse == "2":
            reponse_valide = True
            select_tous_les_quarties_infos(connexion)

        elif user_reponse == "3":
            reponse_valide = True
            select_tous_les_camions_infos(connexion)

        elif user_reponse == "4":
            reponse_valide = True
            select_tous_les_modeles_infos(connexion)

        elif user_reponse == "5":
            reponse_valide = True
            select_tous_les_centres_infos(connexion)

        elif user_reponse == "6":
            reponse_valide = True
            select_tous_les_programmations_infos(connexion)

        elif user_reponse == "r":
            reponse_valide = True
            menu_affichage(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('1','2','3','4','5','6','r','q')\n")


def menu_custom(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Creation d'un menu principal
        print("""Menu informations personnalisées:
1)Le balayeur va où, quand et avec quel camion 
2)Quel camion a quel équipe
3)Le nombre de camions actifs et inactifs
4)Le nombre de programmations d'un balayeur dans un ordre descendant
5)Les balayeurs qui travaillent dans une heure choisi
6)Les camions avec un espace vide suffisant pour les déchets
7)Le nombre de programmations pour un camion 
8)Les camions qui vont au centre et quartier donnés en même temps.
r)Revenir au menu précédent
q)Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "1":
            reponse_valide = True
            balayeur_quand_ou_comment(connexion)

        elif user_reponse == "2":
            reponse_valide = True
            quel_camion_possede_quel_equipe(connexion)

        elif user_reponse == "3":
            reponse_valide = True
            camions_utilises_ou_non(connexion)

        elif user_reponse == "4":
            reponse_valide = True
            balayeurs_nb_prog_descendant(connexion)

        elif user_reponse == "5":
            reponse_valide = True
            balayeur_travaille_heure_donne(connexion)

        elif user_reponse == "6":
            reponse_valide = True
            camions_avec_espace_vide_suffisant(connexion)

        elif user_reponse == "7":
            reponse_valide = True
            nombre_programmations_pour_camion(connexion)

        elif user_reponse == "8":
            reponse_valide = True
            camion_qui_va_centre_quartier_meme_temp(connexion)

        elif user_reponse == "r":
            reponse_valide = True
            menu_affichage(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('1','2','3','4','5','6','7','8','r','q')\n")


def menu_modification(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Creation d'un menu principal
        print("""Menu modification:
e)Éliminer des données
i)Inserer des données
m)Mettre à jour des données
r)Revenir à la menu précédente
q)Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "e":
            reponse_valide = True
            menu_eliminer(connexion)

        elif user_reponse == "i":
            reponse_valide = True
            menu_inserer(connexion)

        elif user_reponse == "m":
            reponse_valide = True
            menu_mettre_jour(connexion)

        elif user_reponse == "r":
            reponse_valide = True
            menu_principal(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('e','i','m','r','q')\n")


def menu_eliminer(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Creation d'un menu principal
        print("""Menu éliminer des données:
1)Elimine toutes les données 
2)Elimine les balayeurs 
3)Elimine les camions á ordures
4)Elimine les quartiers
5)Elimine les programmations
6)Elimine les centres d'ordure
7)Elimine les modèles de camion
r)Revenir à la menu précédente
q)Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "1":
            reponse_valide = True
            elimine_tous_les_donnees(connexion)

        elif user_reponse == "2":
            reponse_valide = True
            elimine_balayeur(connexion)

        elif user_reponse == "3":
            reponse_valide = True
            elimine_camion(connexion)

        elif user_reponse == "4":
            reponse_valide = True
            elimine_quartier(connexion)

        elif user_reponse == "5":
            reponse_valide = True
            elimine_programmation(connexion)

        elif user_reponse == "6":
            reponse_valide = True
            elimine_centre_ordure(connexion)

        elif user_reponse == "7":
            reponse_valide = True
            elimine_modele_camion(connexion)


        elif user_reponse == "r":
            reponse_valide = True
            menu_modification(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('1','2','3','4','5','6', '7', r','q'\n")


def menu_inserer(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Creation d'un menu principal
        print("""Menu insertion des données:
1)Inserer dans le tableau des balayeurs 
2)Inserer dans le tableau des quartiers
3)Inserer dans le tableau des camions à ordure
4)Inserer dans le tableau des modeles
5)Inserer dans le tableau des centres à ordure
6)Inserer dans le tableau des programmations
r)Revenir à la menu précédente
q)Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "1":
            reponse_valide = True
            inserer_dans_balayeurs(connexion)

        elif user_reponse == "2":
            reponse_valide = True
            inserer_dans_quartiers(connexion)

        elif user_reponse == "3":
            reponse_valide = True
            inserer_dans_camions(connexion)

        elif user_reponse == "4":
            reponse_valide = True
            inserer_dans_modeles(connexion)

        elif user_reponse == "5":
            reponse_valide = True
            inserer_dans_centres(connexion)

        elif user_reponse == "6":
            reponse_valide = True
            inserer_dans_programmations(connexion)


        elif user_reponse == "r":
            reponse_valide = True
            menu_modification(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('1','2','3','4','5','6','r','q')\n")


def menu_mettre_jour(connexion):
    reponse_valide = False
    while not reponse_valide:
        # Creation d'un menu principal
        print("""Menu insertion des données:
1)Mettre à jour un balayeur
2)Mettre à jour un quartier
3)Mettre à jour un camion à ordure
4)Mettre à jour un modele
5)Mettre à jour une centre à ordure
6)Mettre à jour une programmation
r)Revenir à la menu précédente
q)Quitter\n""")

        user_reponse = input("Votre choix: ")
        print("")
        if user_reponse == "1":
            reponse_valide = True
            mettre_jour_balayeur(connexion)

        elif user_reponse == "2":
            reponse_valide = True
            mettre_jour_quartier(connexion)

        elif user_reponse == "3":
            reponse_valide = True
            mettre_jour_camion(connexion)

        elif user_reponse == "4":
            reponse_valide = True
            mettre_jour_modele(connexion)

        elif user_reponse == "5":
            reponse_valide = True
            mettre_jour_centre(connexion)

        elif user_reponse == "6":
            reponse_valide = True
            mettre_jour_programmation(connexion)


        elif user_reponse == "r":
            reponse_valide = True
            menu_modification(connexion)

        elif user_reponse == "q":
            quit()

        else:
            print("Vous devez choisir entre les choix ('1','2','3','4','5','6','r','q')\n")


def infos_sur_sujet(connexion):
    """
    Affiche une résumé sur notre sujet
    """
    print("""Il existe de véritables problèmes de pollution au niveau municipal à Pittsburgh /Pennsylvanie (USA). 
Les habitants se plaignent du manque des poubelles et le fait que les ordures ne sont pas ramassées de 
manière régulière. En vue d’avoir un environnement plus sain pour les habitants nous avons décidé de 
tout organiser en utilisant une base de données relationnelle et ainsi d’enregistrer les informations 
nécessaires pour mieux organiser le service.\n""")

    user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
    print("")
    if user_reponse == "o":
        # Reappel de fonction menu_affichage
        menu_principal(connexion)
    else:
        quit()


###################Fonction d'affichages######################

def select_tous_les_balayeurs_infos(connexion):
    """
    Affiche la liste de tous les balayeurs avec leurs infos.
    :param connexion: Connexion à la base de données
    """
    print("1.Liste de tous les balayeurs avec leurs infos\n")
    cur = connexion.cursor()
    cur.execute("""
                SELECT * 
                FROM Balayeurs
                """)
    rows = cur.fetchall()

    # Créer des titres de colonnes
    headers = ["idBalayeur", "pseudoBalayeur", "telBalayeur", "plaqueCamion"]

    # Formatage correct des données du tableau
    table_data = [headers] + rows

    # Imprimer le tableau à l'aide de tabulate
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

    print()
    user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        # Reappel de fonction menu_affichage_tous
        menu_affichage_tous(connexion)
    else:
        quit()


def select_tous_les_quarties_infos(connexion):
    """
    Affiche la liste de tous les quarties avec leurs infos.
    :param connexion: Connexion à la base de données
    """
    print("2.Liste de tous les quartiers avec leurs infos")
    cur = connexion.cursor()
    cur.execute("""
                SELECT * 
                FROM Quartiers
                """)

    rows = cur.fetchall()

    # Créer des titres de colonnes
    headers = ["codeQuartier", "nomQuartier", "popQuartier", "nb_poubQuartier"]

    # Formatage correct des données du tableau
    table_data = [headers] + rows

    # Imprimer le tableau à l'aide de tabulate
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

    print()
    user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non) : ").lower()
    print()
    if user_reponse == "o":
        # Reappel de fonction menu_affichage_tous
        menu_affichage_tous(connexion)
    else:
        quit()


def select_tous_les_camions_infos(connexion):
    """
    Affiche la liste de tous les camions avec leurs infos.
    :param connexion: Connexion à la base de données
    """
    print("3.Liste de tous les camions à ordure avec leurs infos")
    cur = connexion.cursor()
    cur.execute("""
                SELECT * 
                FROM CamionsOrdure
                """)
    rows = cur.fetchall()
    # Créer des titres de colonnes
    headers = ["plaqueCamion", "cap_eqCamion", "nomModele", "nomCentre", "qua_dechCamion"]

    # Formatage correct des données du tableau
    table_data = [headers] + rows

    # Imprimer le tableau à l'aide de tabulate
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

    print()
    user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        # Reappel de fonction menu_affichage_tous
        menu_affichage_tous(connexion)
    else:
        quit()


def select_tous_les_modeles_infos(connexion):
    """
    Affiche la liste de tous les modeles avec leurs infos.
    :param connexion: Connexion à la base de données
    """
    print("4.Liste de tous les models de camion à ordure avec leurs infos")
    cur = connexion.cursor()
    cur.execute("""
                SELECT * 
                FROM Modeles
                """)

    rows = cur.fetchall()

    # Créer des titres de colonnes
    headers = ["nomModele", "tailleModele", "cap_dep_maxModele"]

    # Formatage correct des données du tableau
    table_data = [headers] + rows

    # Imprimer le tableau à l'aide de tabulate
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

    print()
    user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        # Reappel de fonction menu_affichage_tous
        menu_affichage_tous(connexion)
    else:
        quit()


def select_tous_les_centres_infos(connexion):
    """
    Affiche la liste de tous les centres avec leurs infos.
    :param connexion: Connexion à la base de données
    """
    print("5.Liste de tous les centres à ordure avec leurs infos")
    cur = connexion.cursor()
    cur.execute("""
                SELECT * 
                FROM CentresOrdure
                """)

    rows = cur.fetchall()

    # Créer des titres de colonnes
    headers = ["nomCentre", "capCentre"]

    # Formatage correct des données du tableau
    table_data = [headers] + rows

    # Imprimer le tableau à l'aide de tabulate
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

    print()
    user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        # Reappel de fonction menu_affichage_tous
        menu_affichage_tous(connexion)
    else:
        quit()


def select_tous_les_programmations_infos(connexion):
    """
    Affiche la liste de toutes les programmations avec leurs infos.
    :param connexion: Connexion à la base de données
    """
    print("6.Liste de tous les programmations avec leurs infos")
    cur = connexion.cursor()
    cur.execute("""
                SELECT * 
                FROM Programmations
                """)

    rows = cur.fetchall()

    # Créer des titres de colonnes
    headers = ["codeQuartier", "plaqueCamion", "heureProg"]

    # Formatage correct des données du tableau
    table_data = [headers] + rows

    # Imprimer le tableau à l'aide de tabulate
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

    print()
    user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        # Reappel de fonction menu_affichage_tous
        menu_affichage_tous(connexion)
    else:
        quit()


####### FONCTIONS DE INFORMATIONS PERSONNALISES ########

def balayeur_quand_ou_comment(connexion):
    """
    Affiche la liste des balayeurs avec les informations suivantes :
    Le balayeur va où, quand et avec quel camion (représenté par sa plaque).
    :param connexion: Connexion à la base de données
    """
    print("2. Quel balayeur va où, quand et avec quel camion")
    cur = connexion.cursor()
    cur.execute("""
                    SELECT idBalayeur
                    FROM Balayeurs
                    """)
    liste_tuples = cur.fetchall()

    id_balayeurs = []
    for tup in liste_tuples:
        id_balayeurs.append(tup[0])

    reponse_valide = False
    while not reponse_valide:
        print("Liste des balayeurs:", id_balayeurs)

        try:
            idBalayeur = int(input("Veuillez choisir un balayeur: "))

        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")
            abandonner_prompt(menu_custom, connexion)
            continue

        print()
        if idBalayeur in id_balayeurs:
            reponse_valide = True

            try:
                cur = connexion.cursor()  # exemple de séléction-projection
                cur.execute("""
                            SELECT idBalayeur, nomQuartier, heureProg, plaqueCamion 
                            FROM Balayeurs JOIN Programmations USING(plaqueCamion) JOIN Quartiers USING(codeQuartier)
                            WHERE idBalayeur = ?
                            """, (idBalayeur,))

                rows = cur.fetchall()
                # Créer des titres de colonnes
                headers = ["idBalayeur", "nomQuartier", "heureProg", "plaqueCamion"]

                # Formatage correct des données du tableau
                table_data = [headers] + rows

                # Imprimer le tableau à l'aide de tabulate
                print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

            except sqlite3.Error as e:
                print("SQLite erreur:", e)

        else:
            print("L'id que vous avez saisi n'est pas dans la liste des balayeurs, veuillez réessayer!")
            abandonner_prompt(menu_custom, connexion)

    user_reponse = input(
        "Voulez-vous faire cette opération avec un autre balayeur (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        balayeur_quand_ou_comment(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print()
        if user_reponse == "o":
            # Reappel de fonction menu_custom
            menu_custom(connexion)
        else:
            quit()


from tabulate import tabulate


def quel_camion_possede_quel_equipe(connexion):
    """
    Affiche le camion choisi par l'utilisateur avec son équipe
    :param connexion: Connexion à la base de données
    """
    print("2. Quel camion a quelle équipe\n")
    cur = connexion.cursor()
    cur.execute("""
                    SELECT plaqueCamion
                    FROM CamionsOrdure
                    """)
    liste_tuples = cur.fetchall()

    plaqueCamions = [tup[0] for tup in liste_tuples]

    reponse_valide = False
    while not reponse_valide:
        print("Liste des plaques de camions:", plaqueCamions)
        try:
            plaqueCamion = int(input("Veuillez choisir une plaque d'immatriculation : "))

        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")
            abandonner_prompt(menu_custom, connexion)
            continue
        print()
        if plaqueCamion in plaqueCamions:
            reponse_valide = True
            try:
                cur.execute("""
                            SELECT plaqueCamion, nomModele, idBalayeur, pseudoBalayeur
                            FROM CamionsOrdure JOIN Balayeurs USING (plaqueCamion)
                            WHERE plaqueCamion = ?
                            """, (plaqueCamion,))
                rows = cur.fetchall()

                headers = ["Plaque Camion", "Nom Modèle", "ID Balayeur", "Pseudo Balayeur"]
                print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
                print()

            except sqlite3.Error as e:
                print("SQLite erreur:", e)

            user_reponse = input(
                "Voulez-vous faire une cette opération pour un autre camion  (o/toute autre touche pour dire non): ").lower()
            print()
            if user_reponse == "o":
                quel_camion_possede_quel_equipe(connexion)
            else:
                user_reponse = input(
                    "Voulez-vous faire une autre opération (o/toute autre touche pour dire non): ").lower()
                print()
                if user_reponse == "o":
                    # Reappel de fonction menu_custom
                    menu_custom(connexion)
                else:
                    quit()
        else:
            print("La plaque que vous avez saisie n'est pas dans la liste des camions, veuillez réessayer!")
            abandonner_prompt(menu_custom, connexion)


def camions_utilises_ou_non(connexion):
    """
    Affiche le nombre de camions qui sont activement en service et le nombre
    de camions qui sont inactifs en raison de maintenance ou panne.
    :param connexion: Connexion à la base de données
    """
    print("3. Les nombres des camions actifs et inactifs")

    cur = connexion.cursor()
    cur.execute("""  
                WITH camions_inactifs AS (
                    SELECT plaqueCamion
                    FROM CamionsOrdure
                    EXCEPT
                    SELECT plaqueCamion
                    FROM CamionsOrdure JOIN Programmations USING (plaqueCamion)
                )
                SELECT COUNT(*)
                FROM camions_inactifs
                        """)

    camions_inactifs_count = cur.fetchone()[0]
    print("Le nombre de camions inactifs : ", camions_inactifs_count)

    cur.execute("""  
                SELECT COUNT(plaqueCamion)
                FROM CamionsOrdure
                        """)

    tousCamions_count = cur.fetchone()[0]
    camions_actifs_count = tousCamions_count - camions_inactifs_count
    print("Le nombre de camions actifs : ", camions_actifs_count)
    print()

    # Récupération des plaques de camions actifs
    cur.execute("""
                SELECT DISTINCT plaqueCamion --j'ai ajouté un distinct ici suite à l'apparition de la plaque 101 deux fois.
                FROM CamionsOrdure JOIN Programmations USING (plaqueCamion)
                        """)
    rows_actifs = cur.fetchall()

    # Récupération des plaques de camions inactifs
    cur.execute("""
                SELECT plaqueCamion
                FROM CamionsOrdure
                EXCEPT
                SELECT plaqueCamion
                FROM CamionsOrdure JOIN Programmations USING (plaqueCamion)
                        """)
    rows_inactifs = cur.fetchall()

    # Créer des titres de colonnes pour les camions actifs et inactifs
    headers = ["plaqueCamion_Actif", "plaqueCamion_Inactif"]

    # Créer des données pour les deux tableaux
    max_len = max(len(rows_actifs), len(rows_inactifs))
    table_data = []
    for i in range(max_len):
        if i < len(rows_actifs):
            row_actif = rows_actifs[i][0] if rows_actifs[i] else ""
        else:
            row_actif = ""
        if i < len(rows_inactifs):
            row_inactif = rows_inactifs[i][0] if rows_inactifs[i] else ""
        else:
            row_inactif = ""
        table_data.append([str(row_actif).ljust(20), str(row_inactif).ljust(20)])

    # Imprimer les deux tableaux côte à côte
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    print()
    user_reponse = input("Voulez-vous refaire (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        camions_utilises_ou_non(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print()
        if user_reponse == "o":
            # Reappel de fonction menu_custom
            menu_custom(connexion)
        else:
            quit()


def balayeurs_nb_prog_descendant(connexion):
    """
    Affiche le nombre de programmations d'un balayeur dans un ordre descendant.
    :param connexion: Connexion à la base de données
    """
    print("4. Le nombre de programmations d'un balayeur dans un ordre descendant")

    try:
        cur = connexion.cursor()
        cur.execute("""
                    SELECT B.idBalayeur, COUNT(P.plaqueCamion) AS Nombre_Programmations
                    FROM Balayeurs B
                    LEFT JOIN Programmations P USING(plaqueCamion)
                    GROUP BY B.idBalayeur
                    ORDER BY Nombre_Programmations DESC
                    """)
        rows = cur.fetchall()

        # Créer le tableau de données
        headers = ["ID Balayeur", "Nombre de Programmations"]
        table_data = []
        for row in rows:
            table_data.append(row)

        # Imprimer le tableau
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    except sqlite3.Error as e:
        print("Erreur SQLite:", e)

    print()
    user_reponse = input("Voulez-vous refaire cette opération (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        balayeurs_nb_prog_descendant(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print()
        if user_reponse == "o":
            # Reappel de fonction menu_custom
            menu_custom(connexion)
        else:
            quit()


def balayeur_travaille_heure_donne(connexion):
    """
    Affiche les balayeurs qui travaillent pour une heure choisi.
    :param connexion: Connexion à la base de données
    """
    print("5. Les balayeurs qui travaillent dans une heure choisi")
    cur = connexion.cursor()

    cur.execute("""
                    SELECT heureProg
                    FROM Programmations
                    """)
    liste_heures = cur.fetchall()

    heures = [heure[0] for heure in liste_heures]

    reponse_valide = False
    while not reponse_valide:
        print("Liste des heures de travail:", heures)
        heure_travail = input("Veuillez choisir une heure de travail (HH:MM) : ")
        print("")
        if heure_travail in heures:
            reponse_valide = True
            try:
                cur.execute("""
                            SELECT B.idBalayeur, B.pseudoBalayeur, B.telBalayeur, B.plaqueCamion
                            FROM Balayeurs B JOIN Programmations P USING(plaqueCamion)
                            WHERE P.heureProg = ?
                            """, (heure_travail,))
                rows = cur.fetchall()

                headers = ["ID Balayeur", "Pseudo Balayeur", "Téléphone Balayeur", "Plaque Camion"]
                print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
                print()

            except sqlite3.Error as e:
                print("SQLite erreur:", e)

            user_reponse = input(
                "Voulez-vous faire cette opération pour une autre heure (o/toute autre touche pour dire non): ").lower()
            print()
            if user_reponse == "o":
                balayeur_travaille_heure_donne(connexion)

            else:
                user_reponse = input(
                    "Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
                print()
                if user_reponse == "o":
                    # Reappel de fonction menu_custom
                    menu_custom(connexion)
                else:
                    quit()
        else:
            print("Erreur: Vous devez choisir une heure de travail qui se trouve dans la liste des heures.\n")
            abandonner_prompt(menu_custom, connexion)


def camions_avec_espace_vide_suffisant(connexion): #  on ne compte pas les camions inactifs.
    print("6. Les camions avec un espace vide suffisant pour les déchets")

    cur = connexion.cursor()

    while True:
        # On demande à l'utilisateur la quantité minimale d'espace vide souhaitée
        try:
            quantite_minimale = int(input("Veuillez saisir la quantité minimale d'espace vide souhaitée: "))

        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")
            abandonner_prompt(menu_custom, connexion)
            continue

        break

    cur.execute("""  
                SELECT C.plaqueCamion, C.qua_dechCamion, M.cap_dep_maxModele 
                FROM CamionsOrdure C JOIN Modeles M USING(nomModele) 
                WHERE M.cap_dep_maxModele - C.qua_dechCamion >= ?;
                        """, (quantite_minimale,))

    rows = cur.fetchall()
    # On crée les en-têtes des colonnes
    headers = ["plaqueCamion", "qua_dechCamion", "cap_dep_maxModele"]

    # On formate correctement les données du tableau
    table_data = [headers] + rows

    # On affiche le tableau avec tabulate
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

    print()
    user_reponse = input("Voulez-vous refaire cette opération (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        camions_avec_espace_vide_suffisant(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre opération (o/toute autre touche pour dire non): ").lower()
        print()
        if user_reponse == "o":
            # On rappelle la fonction pour revenir au menu
            menu_custom(connexion)
        else:
            quit()


def nombre_programmations_pour_camion(connexion):
    print("7. Le nombre de programmations pour un camion ")
    cur = connexion.cursor()
    cur.execute("""
                        SELECT plaqueCamion
                        FROM CamionsOrdure
                        """)

    liste_tuples = cur.fetchall()
    plaque_camions = []
    for tup in liste_tuples:
        plaque_camions.append(tup[0])

    reponse_valide = False
    while not reponse_valide:
        print("Liste des plaques:", plaque_camions)
        try:
            plaque_camion = int(input("Veuillez saisir la plaque du camion: "))

        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")
            abandonner_prompt(menu_custom, connexion)
            continue
        print()
        if plaque_camion in plaque_camions:
            reponse_valide = True
            try:
                cur = connexion.cursor()
                cur.execute("""
                                SELECT COUNT(P.plaqueCamion) as NombreProgrammations
                                FROM Programmations P
                                WHERE P.plaqueCamion = ?
                                GROUP BY P.plaqueCamion
                            """, (plaque_camion,))

                rows = cur.fetchall()

                # Créer des titres de colonnes
                headers = ["NombreProgrammations"]

                # Formatage correct des données du tableau
                table_data = [headers] + rows

                # Imprimer le tableau à l'aide de tabulate

                print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
            except sqlite3.Error as e:
                print("SQLite erreur:", e)
        else:
            print("Le plaque que vous avez saisi n'est pas dans la liste des plaques, veuillez réessayer!")
            abandonner_prompt(menu_custom, connexion)

    print()
    user_reponse = input("Voulez-vous refaire cette opération (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        nombre_programmations_pour_camion(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print()
        if user_reponse == "o":
            # Reappel de fonction menu_custom
            menu_custom(connexion)
        else:
            quit()


def camion_qui_va_centre_quartier_meme_temp(connexion):
    """
    Affiche les camions allant vers un centre et une quartier donnés.
    :param connexion: Connexion à la base de données
    """
    print("8.Afficher les camions qui vont au centre et quartier donnés en même temps.")

    cur = connexion.cursor()

    # Obtenir la liste des centres
    cur.execute("""
                    SELECT nomCentre
                    FROM CentresOrdure
                    """)
    liste_centres = cur.fetchall()
    centres = [centre[0] for centre in liste_centres]

    # Obtenir la liste des quartiers
    cur.execute("""
                    SELECT nomQuartier
                    FROM Quartiers
                    """)
    liste_quartiers = cur.fetchall()
    quartiers = [quartier[0] for quartier in liste_quartiers]

    reponse_valide = False
    while not reponse_valide:
        # Sélectionner un centre par l'utilisateur
        print("Liste des centres:", centres)
        selected_centre = input("Veuillez choisir un centre : ")
        print()

        # Sélectionner une ville par l'utilisateur
        print("Liste des quartiers:", quartiers)
        selected_quartier = input("Veuillez choisir une quartier : ")
        print()

        if selected_centre in centres and selected_quartier in quartiers:
            reponse_valide = True
            try:
                # Trouver les camions allant vers le centre et la quartier donnés
                cur.execute("""
                    SELECT plaqueCamion
                    FROM CamionsOrdure 
                    JOIN CentresOrdure USING(nomCentre)
                    WHERE nomCentre = ? 
                    INTERSECT
                    SELECT C.plaqueCamion
                    FROM CamionsOrdure C
                    JOIN Programmations P USING(plaqueCamion)
                    JOIN Quartiers Q USING(codeQuartier)
                    WHERE Q.nomQuartier = ?
                """, (selected_centre, selected_quartier))

                rows = cur.fetchall()

                # Afficher le tableau
                headers = ["plaqueCamion"]
                print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
                print()

            except sqlite3.Error as e:
                print("Erreur SQLite :", e)

            user_reponse = input(
                "Voulez-vous faire cette opération pour un autre centre et quartier (o/toute autre touche pour dire non): ").lower()
            print()
            if user_reponse == "o":
                camion_qui_va_centre_quartier_meme_temp(connexion)
            else:
                user_reponse = input(
                    "Voulez-vous faire une autre opération (o/toute autre touche pour dire non): ").lower()
                print()
                if user_reponse == "o":
                    # Réappeler le menu
                    menu_custom(connexion)
                else:
                    quit()

        else:
            print(
                "Le(s) nom(s) que vous avez saisi n'est pas dans la liste des Centres ou Quartiers, veuillez réessayer!")
            abandonner_prompt(menu_custom, connexion)


######################## FONCTIONS D'ELIMINATION ##############################
def elimine_tous_les_donnees(connexion):
    print("1.Elimination de toutes les données")

    try:
        db.mise_a_jour_bd(connexion, "data/suppressions_data_from_table.sql")
        print("Toutes les données supprimé avec succès.\n")
    except sqlite3.Error as e:
        print("SQLite erreur:", e)

    user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        # Reappel de fonction menu_eliminer
        menu_eliminer(connexion)
    else:
        quit()


def elimine_balayeur(connexion):
    cur = connexion.cursor()
    cur.execute("""
                    SELECT idBalayeur
                    FROM Balayeurs
                    """)
    liste_tuples = cur.fetchall()

    id_balayeurs = []
    for tup in liste_tuples:
        id_balayeurs.append(tup[0])

    reponse_valide = False
    while not reponse_valide:

        # Afficher le tableau
        cur.execute("""
                        SELECT * 
                        FROM Balayeurs
                        """)
        rows = cur.fetchall()

        # Créer des titres de colonnes
        headers = ["idBalayeur", "pseudoBalayeur", "telBalayeur", "plaqueCamion"]

        # Formatage correct des données du tableau
        table_data = [headers] + rows

        # Imprimer le tableau à l'aide de tabulate
        print("Liste des balayeurs:")
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        print()

        try:
            balayeur_a_eliminer = int(input("Veuillez choisir un balayeur: "))

        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")
            abandonner_prompt(menu_eliminer, connexion)
            continue

        print()
        if balayeur_a_eliminer in id_balayeurs:
            reponse_valide = True
            try:
                cur = connexion.cursor()

                # Eliminer le Balayeur selon son pseudo
                cur.execute("""
                                DELETE FROM Balayeurs
                                WHERE idBalayeur = ?
                                """, (balayeur_a_eliminer,))

                # Sauvegarde les modifications
                connexion.commit()

                print(f"Le balayeur {balayeur_a_eliminer} a été supprimé avec succès.")

            except sqlite3.Error as e:
                print("SQLite erreur:", e)

            user_reponse = input(
                "Voulez-vous eliminer un autre balayeur (o/toute autre touche pour dire non): ").lower()
            print("")
            if user_reponse == "o":
                elimine_balayeur(connexion)
            else:
                user_reponse = input(
                    "Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
                print("")
                if user_reponse == "o":
                    # Reappel de fonction menu_eliminer
                    menu_eliminer(connexion)
                else:
                    quit()
        else:
            print("Vous devez choisir un id balayeur qui se trouve dans la liste données \n")
            abandonner_prompt(menu_eliminer, connexion)


def elimine_camion(connexion):
    cur = connexion.cursor()

    # Création la liste des plaqueCamions selon la table CamionsOrdure
    cur.execute("""
                    SELECT plaqueCamion
                    FROM CamionsOrdure
                    """)

    liste_tuples_camions = cur.fetchall()
    plaque_camions = []
    for tup in liste_tuples_camions:
        plaque_camions.append(tup[0])

    # Création la liste des plaqueCamions selon la table Programmations
    cur.execute("""
                SELECT plaqueCamion
                FROM Programmations
                """)

    liste_tuples_prog = cur.fetchall()
    plaque_camions_in_prog = []
    for tup in liste_tuples_prog:
        plaque_camions_in_prog.append(tup[0])

    # Création la liste des plaqueCamions selon la table Balayeurs
    cur.execute("""
                SELECT plaqueCamion
                FROM Balayeurs
                """)

    liste_tuples_balayeur = cur.fetchall()
    plaque_camions_in_balayeurs = []
    for tup in liste_tuples_balayeur:
        plaque_camions_in_balayeurs.append(tup[0])

    reponse_valide = False
    while not reponse_valide:

        # Afficher le tableau
        cur.execute("""
                        SELECT * 
                        FROM CamionsOrdure
                                """)
        rows = cur.fetchall()

        # Créer des titres de colonnes
        headers = ["plaqueCamion", "cap_eqCamion", "nomModele", "nomCentre", "qua_dechCamion"]

        # Formatage correct des données du tableau
        table_data = [headers] + rows

        # Imprimer le tableau à l'aide de tabulate
        print("Liste des plaques de camion à ordure:")
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        print()
        try:
            camion_a_eliminer = int(input("Veuillez choisir un plaque de camion à ordure: "))

        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")
            abandonner_prompt(menu_eliminer, connexion)
            continue
        print()

        if camion_a_eliminer in plaque_camions:
            reponse_valide = True
            cur = connexion.cursor()
            if (camion_a_eliminer in plaque_camions_in_prog) or (camion_a_eliminer in plaque_camions_in_balayeurs):
                reponse_certain = input(
                    "Foreign Key: Cette plaque se trouve dans d'autres classes, êtes-vous sûr de la supprimer et changer ces classes aussi (o/toute autre touche pour dire non): ").lower()
                if reponse_certain == "o":
                    try:
                        # Élimine la ligne qui contient la plaque camion dans Programmations
                        cur.execute("""
                                    DELETE FROM Programmations
                                    WHERE plaqueCamion = ?
                        """, (camion_a_eliminer,))

                        # Élimine la ligne qui contient la plaque camion dans Balayeurs
                        cur.execute("""
                                        DELETE FROM Balayeurs
                                        WHERE plaqueCamion = ?
                                        """, (camion_a_eliminer,))

                        # Élimine la ligne qui contient la plaque camion dans CamionsOrdure
                        cur.execute("""
                                        DELETE FROM CamionsOrdure
                                        WHERE plaqueCamion = ?
                                        """, (camion_a_eliminer,))

                        # Sauvegarde les modifications
                        connexion.commit()
                        print(
                            f"Le camion à ordure {camion_a_eliminer} a été supprimé avec succès dans toutes les classes concernées.")

                    except sqlite3.Error as e:
                        print("SQLite erreur:", e)

                else:
                    print("Alors on ne peut pas éliminer ce camion!")

            else:  # Comme le foreign key n'a pas été utilisé ailleurs, la plaque se supprimera seulement de la classe des camions à ordure.
                try:
                    cur.execute("""
                                    DELETE FROM CamionsOrdure
                                    WHERE plaqueCamion = ?
                                    """, (camion_a_eliminer,))
                    # Sauvegarde les modifications
                    connexion.commit()
                    print(f"Le camion à ordure {camion_a_eliminer} a été supprimé avec succès.")

                except sqlite3.Error as e:
                    print("SQLite erreur:", e)

            user_reponse = input(
                "Voulez-vous eliminer un autre camion à ordure (o/toute autre touche pour dire non): ").lower()
            print()
            if user_reponse == "o":
                elimine_camion(connexion)
            else:
                user_reponse = input(
                    "Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
                print()
                if user_reponse == "o":
                    # Reappel de fonction menu_eliminer
                    menu_eliminer(connexion)
                else:
                    quit()
        else:
            print("Vous devez choisir une plaque de camion à ordure qui se trouve dans la liste données \n")
            abandonner_prompt(menu_eliminer, connexion)


def elimine_quartier(connexion):
    cur = connexion.cursor()

    # Création la liste des codeQuartiers selon la table Quartiers
    cur.execute("SELECT codeQuartier FROM Quartiers")
    liste_tuples_quartiers = cur.fetchall()
    code_quartiers = []
    for tup in liste_tuples_quartiers:
        code_quartiers.append(tup[0])

    # Création la liste des codeQuartiers selon la table Programmations
    cur.execute("SELECT codeQuartier FROM Programmations")
    liste_tuples_prog = cur.fetchall()
    code_quartiers_in_prog = []
    for tup in liste_tuples_prog:
        code_quartiers_in_prog.append(tup[0])

    reponse_valide = False
    while not reponse_valide:

        # Afficher le tableau
        cur.execute("""
                        SELECT * 
                        FROM Quartiers
                                """)
        rows = cur.fetchall()

        # Créer des titres de colonnes
        headers = ["codeQuartier", "nomQuartier", "popQuartier", "nb_poubQuartier"]

        # Formatage correct des données du tableau
        table_data = [headers] + rows

        # Imprimer le tableau à l'aide de tabulate
        print("Liste des quartiers:")
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        print()

        try:
            quartier_a_eliminer = int(input("Veuillez entrer le code du quartier à supprimer (un nombre entier): "))

        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")
            abandonner_prompt(menu_eliminer, connexion)
            continue

        print()
        if quartier_a_eliminer in code_quartiers:
            reponse_valide = True
            cur = connexion.cursor()
            if quartier_a_eliminer in code_quartiers_in_prog:
                reponse_certain = input(
                    "Foreign Key: Ce code de quartier se trouve dans d'autres classes, êtes-vous sûr de la supprimer et changer ces classes aussi (o/toute autre touche pour dire non): ").lower()
                if reponse_certain == "o":
                    try:
                        # Élimine la ligne qui contient le code quartier dans Programmations
                        cur.execute("""
                                        DELETE FROM Programmations
                                        WHERE codeQuartier = ?
                                        """, (quartier_a_eliminer,))

                        # Élimine la ligne qui contient le code quartier dans Programmations
                        cur.execute("""
                                        DELETE FROM Quartiers 
                                        WHERE codeQuartier = ?
                                        """, (quartier_a_eliminer,))
                        # Sauvegarde les modifications
                        connexion.commit()
                        print(
                            f"Le quartier {quartier_a_eliminer} a été supprimé avec succès dans toutes les classes concernées.")

                    except sqlite3.Error as e:
                        print("Erreur lors de la suppression du quartier :", e)
                else:
                    print("Alors on ne peut pas éliminer ce quartier!")

            else:  # Comme le foreign key n'a pas été utilisé ailleurs, le quartier se supprimera seulement de la classe des quartiers.
                try:
                    # Élimine la ligne qui contient le code quartier dans Programmations
                    cur.execute("""
                                    DELETE FROM Quartiers 
                                    WHERE codeQuartier = ?
                                    """, (quartier_a_eliminer,))
                    # Sauvegarde les modifications
                    connexion.commit()
                    print(f"Le quartier {quartier_a_eliminer} a été supprimé avec succès.")

                except sqlite3.Error as e:
                    print("SQLite erreur:", e)

            user_reponse = input(
                "Voulez-vous supprimer un autre quartier (o/toute autre touche pour dire non): ").lower()
            print()
            if user_reponse == "o":
                elimine_quartier(connexion)
            else:
                user_reponse = input(
                    "Voulez-vous effectuer une autre opération (o/toute autre touche pour dire non): ").lower()
                print()
                if user_reponse == "o":
                    # Reappel de fonction menu_eliminer
                    menu_eliminer(connexion)
                else:
                    quit()
        else:
            print("Vous devez choisir un code de quartier qui se trouve dans la liste données \n")
            abandonner_prompt(menu_eliminer, connexion)


def elimine_programmation(connexion):
    cur = connexion.cursor()
    cur.execute("SELECT codeQuartier, plaqueCamion, heureProg FROM Programmations")
    programmations = cur.fetchall()

    codes_quartiers = set()
    plaques_camions = set()

    for prog in programmations:
        code_quartier = prog[0]
        plaque_camion = prog[1]
        codes_quartiers.add(code_quartier)
        plaques_camions.add(plaque_camion)

    reponse_valide = False
    while not reponse_valide:

        # Afficher le tableau
        cur.execute("""
                        SELECT * 
                        FROM Programmations
                                """)

        rows = cur.fetchall()
        # Créer des titres de colonnes

        headers = ["codeQuartier", "plaqueCamion", "heureProg"]
        # Formatage correct des données du tableau

        table_data = [headers] + rows
        # Imprimer le tableau à l'aide de tabulate
        print("Liste des Programmations:")
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        print()

        try:
            code_quartier = int(input("Veuillez entrer le code du quartier de la programmation à supprimer : "))
            plaque_camion = int(input("Veuillez entrer la plaque du camion de la programmation à supprimer : "))

        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")
            abandonner_prompt(menu_eliminer, connexion)
            continue
        print("")

        if (code_quartier, plaque_camion) in [(prog[0], prog[1]) for prog in programmations]:
            reponse_valide = True
            try:
                cur.execute("DELETE FROM Programmations WHERE codeQuartier = ? AND plaqueCamion = ?",
                            (code_quartier, plaque_camion))

                # Pour méttre a jour la quantité du dechet dans la camionsOrdure
                db.mise_a_jour_bd(connexion, "data/view.sql")
                connexion.commit()
                print(
                    f"Programmation concernant le quartier de code {code_quartier} et le camion de plaque {plaque_camion} supprimée avec succès.")
                print()
            except sqlite3.Error as e:
                print("Erreur lors de la suppression de la programmation :", e)

            user_reponse = input(
                "Voulez-vous supprimer une autre programmation (o/toute autre touche pour dire non): ").lower()
            print("")
            if user_reponse == "o":
                elimine_programmation(connexion)
            else:
                user_reponse = input(
                    "Voulez-vous effectuer une autre opération (o/toute autre touche pour dire non): ").lower()
                print("")
                if user_reponse == "o":
                    menu_eliminer(connexion)
                else:
                    quit()
        else:
            print("La programmation que vous avez saisie n'existe pas, veuillez réessayer!")
            abandonner_prompt(menu_eliminer, connexion)


def elimine_centre_ordure(connexion):
    cur = connexion.cursor()

    # Création la liste des nomCentres selon la table CentresOrdure
    cur.execute("SELECT nomCentre FROM CentresOrdure")
    liste_tuples_centres = cur.fetchall()
    nom_centres = []
    for tup in liste_tuples_centres:
        nom_centres.append(tup[0])

    # Création la liste des nomCentres selon la table CamionsOrdure
    cur.execute("SELECT nomCentre FROM CamionsOrdure")
    liste_tuples_camions = cur.fetchall()
    nom_centres_in_camions = []
    for tup in liste_tuples_camions:
        nom_centres_in_camions.append(tup[0])

    reponse_valide = False
    while not reponse_valide:

        # Afficher le tableau
        cur.execute("""
                        SELECT * 
                        FROM CentresOrdure
                                        """)
        rows = cur.fetchall()

        # Créer des titres de colonnes
        headers = ["nomCentre", "capCentre"]

        # Formatage correct des données du tableau
        table_data = [headers] + rows

        # Imprimer le tableau à l'aide de tabulate
        print("Liste des centres:")
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        print()

        try:
            centre_a_eliminer = input("Veuillez entrer le nom du centre à supprimer : ")

        except ValueError:
            print("Erreur: Veuillez entrer une texte.")
            abandonner_prompt(menu_eliminer, connexion)
            continue

        print()
        if centre_a_eliminer in nom_centres:
            reponse_valide = True
            cur = connexion.cursor()
            if centre_a_eliminer in nom_centres_in_camions:
                reponse_certain = input(
                    "Foreign Key: Ce nom de centre se trouve dans d'autres classes, êtes-vous sûr de la supprimer et changer ces classes aussi (o/toute autre touche pour dire non): ").lower()
                if reponse_certain == "o":
                    try:
                        # Élimine la ligne dans Programmations qui contient le plaque du camion qui a le nom du centre dans CamionsOrdure
                        cur.execute(""" 
                                        DELETE FROM Programmations 
                                        WHERE plaqueCamion IN (
                                            SELECT CO.plaqueCamion
                                            FROM CamionsOrdure CO
                                            WHERE CO.nomCentre = ?)
                                        """, (centre_a_eliminer,))

                        # Élimine la ligne dans Balayeurs qui contient le plaque du camion qui a le nom du centre dans CamionsOrdure
                        cur.execute(""" 
                                        DELETE FROM Balayeurs 
                                        WHERE plaqueCamion IN (
                                            SELECT CO.plaqueCamion
                                            FROM CamionsOrdure CO
                                            WHERE CO.nomCentre = ?)
                                        """, (centre_a_eliminer,))

                        # Élimine la ligne qui contient le nom centre dans CamionsOrdure
                        cur.execute("""
                                    DELETE FROM CamionsOrdure 
                                    WHERE nomCentre = ?
                                    """, (centre_a_eliminer,))

                        # Élimine la ligne qui contient le nom centre dans CentresOrdure
                        cur.execute("""
                                    DELETE FROM CentresOrdure 
                                    WHERE nomCentre = ?
                                    """, (centre_a_eliminer,))
                        # Sauvegarde les modifications
                        connexion.commit()
                        print(
                            f"Centre de collecte d'ordures {centre_a_eliminer} supprimé avec succès dans toutes les classes concernées..")

                    except sqlite3.Error as e:
                        print("Erreur lors de la suppression du centre de collecte d'ordures :", e)

                else:
                    print("Alors on ne peut pas éliminer ce centre!")

            else:  # Comme le foreign key n'a pas été utilisé ailleurs, la centre se supprimera seulement de la classe des centres.
                try:
                    # Élimine la ligne qui contient le nom centre dans CentresOrdure
                    cur.execute("""
                                       DELETE FROM CentresOrdure 
                                       WHERE nomCentre = ?
                                       """, (centre_a_eliminer,))
                    # Sauvegarde les modifications
                    connexion.commit()
                    print(f"Centre de collecte d'ordures {centre_a_eliminer} supprimé avec succès.")

                except sqlite3.Error as e:
                    print("SQLite erreur:", e)

            user_reponse = input(
                "Voulez-vous supprimer un autre centre de collecte d'ordures (o/toute autre touche pour dire non): ").lower()
            print()
            if user_reponse == "o":
                elimine_centre_ordure(connexion)
            else:
                user_reponse = input(
                    "Voulez-vous effectuer une autre opération (o/toute autre touche pour dire non): ").lower()
                print()
                if user_reponse == "o":
                    menu_eliminer(connexion)
                else:
                    quit()
        else:
            print("Vous devez choisir un nom de centre qui se trouve dans la liste données \n")
            abandonner_prompt(menu_eliminer, connexion)


def elimine_modele_camion(connexion):
    cur = connexion.cursor()

    # Création la liste des nomModele selon la table Modeles
    cur.execute("SELECT nomModele FROM Modeles")
    liste_tuples_modeles = cur.fetchall()
    nom_modeles = []
    for tup in liste_tuples_modeles:
        nom_modeles.append(tup[0])

    # Création la liste des nomModeles selon la table CamionsOrdure
    cur.execute("SELECT nomModele FROM CamionsOrdure")
    liste_tuples_camions = cur.fetchall()
    nom_modeles_in_camions = []
    for tup in liste_tuples_camions:
        nom_modeles_in_camions.append(tup[0])

    reponse_valide = False
    while not reponse_valide:

        # Afficher le tableau
        cur.execute("""
                        SELECT * 
                        FROM Modeles
                                        """)
        rows = cur.fetchall()

        # Créer des titres de colonnes
        headers = ["nomModele","tailleModele", "cap_dep_maxModele"] # Ici, j'ai ajouté les noms Modeles qui n'étaient pas visibles sur l'affichage.

        # Formatage correct des données du tableau
        table_data = [headers] + rows

        # Imprimer le tableau à l'aide de tabulate
        print("Liste des modeles:")
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        print()

        try:
            modele_a_eliminer = input("Veuillez entrer le nom de modèle à supprimer : ")

        except ValueError:
            print("Erreur: Veuillez entrer une texte.")
            abandonner_prompt(menu_eliminer, connexion)
            continue

        print()
        if modele_a_eliminer in nom_modeles:
            reponse_valide = True
            cur = connexion.cursor()
            if modele_a_eliminer in nom_modeles_in_camions:
                reponse_certain = input(
                    "Foreign Key: Ce nom de modele se trouve dans d'autres classes, êtes-vous sûr de la supprimer et changer ces classes aussi (o/toute autre touche pour dire non): ").lower()
                if reponse_certain == "o":
                    try:
                        # Élimine la ligne dans Programmations qui contient la plaque du camion qui est du modèle à supprimer.
                        cur.execute(""" 
                                        DELETE FROM Programmations 
                                        WHERE plaqueCamion IN (
                                            SELECT CO.plaqueCamion
                                            FROM CamionsOrdure CO
                                            WHERE CO.nomModele = ?)
                                        """, (modele_a_eliminer,))

                        # Élimine la ligne dans Balayeurs qui contient la plaque du camion qui est de modèle à supprimer.
                        cur.execute(""" 
                                        DELETE FROM Balayeurs 
                                        WHERE plaqueCamion IN (
                                            SELECT CO.plaqueCamion
                                            FROM CamionsOrdure CO
                                            WHERE CO.nomModele = ?)
                                        """, (modele_a_eliminer,))

                        # Élimine la ligne qui contient le nom de modèle dans CamionsOrdure
                        cur.execute("""
                                    DELETE FROM CamionsOrdure 
                                    WHERE nomModele = ?
                                    """, (modele_a_eliminer,))

                        # Élimine la ligne qui contient le nom de modèle dans Modeles
                        cur.execute("""
                                    DELETE FROM Modeles 
                                    WHERE nomModele = ?
                                    """, (modele_a_eliminer,))
                        # Sauvegarde les modifications
                        connexion.commit()
                        print(
                            f"Le modèle {modele_a_eliminer} supprimé avec succès dans toutes les classes concernées..")

                    except sqlite3.Error as e:
                        print("Erreur lors de la suppression du modèle choisi :", e)

                else:
                    print("Alors on ne peut pas éliminer ce modèle!")

            else:  # Comme le foreign key n'a pas été utilisé ailleurs, la centre se supprimera seulement de la classe des centres.
                try:
                    # Élimine la ligne qui contient le nom de modèle dans Modeles
                    cur.execute("""
                                       DELETE FROM Modeles 
                                       WHERE nomModele = ?
                                       """, (modele_a_eliminer,))
                    # Sauvegarde les modifications
                    connexion.commit()
                    print(f"Centre de collecte d'ordures {modele_a_eliminer} supprimé avec succès.")

                except sqlite3.Error as e:
                    print("SQLite erreur:", e)

            user_reponse = input("Voulez-vous supprimer un autre modèle (o/toute autre touche pour dire non): ").lower()
            print()
            if user_reponse == "o":
                elimine_modele_camion(connexion)
            else:
                user_reponse = input(
                    "Voulez-vous effectuer une autre opération (o/toute autre touche pour dire non): ").lower()
                print()
                if user_reponse == "o":
                    menu_eliminer(connexion)
                else:
                    quit()
        else:
            print("Vous devez choisir un nom de modèle qui se trouve dans la liste données \n")
            abandonner_prompt(menu_eliminer, connexion)


########################Fonction Inserer#########################
def inserer_dans_balayeurs(connexion):
    print("1.Inserer dans le tableau des balayeurs")
    cur = connexion.cursor()
    while True:
        try:
            while True:
                id_balayeur = (input("Veuillez saisir l'ID du balayeur: "))
                # On controlle si id_balayeur est un entier de 2 chiffres
                if id_balayeur.isdigit() and len(id_balayeur) == 2:
                    # On controlle si cette id_balayeur existe déja
                    cur.execute("SELECT * FROM Balayeurs WHERE idBalayeur = ?", (id_balayeur,))
                    if cur.fetchone():
                        print("Erreur: Un balayeur avec cet ID existe déjà. Veuillez saisir un ID unique.")
                        abandonner_prompt(menu_inserer, connexion)
                        continue  # Essayer encore
                    break
                print("Erreur: L'id du baalyeur doit être un nombre entier de 2 chiffres.")
                abandonner_prompt(menu_inserer, connexion)
            while True:
                pseudo_balayeur = input("Veuillez saisir le pseudo du balayeur: ")
                # On controlle si pseudo_balayeur est un mot
                if pseudo_balayeur.strip() and pseudo_balayeur.isalpha():
                    break
                print("Erreur: Le pseudo du balayeur doit être un mot.")
                abandonner_prompt(menu_inserer, connexion)
            while True:
                tel_balayeur = input("Veuillez saisir le numéro de téléphone du balayeur: ")
                # On controlle si tel_balayeur est un entier de 9 chiffres
                if tel_balayeur.isdigit() and len(tel_balayeur) == 9:
                    break
                print("Erreur: Le numéro de téléphone doit être un entier de 9 chiffres.")
                abandonner_prompt(menu_inserer, connexion)
            while True:
                plaque_camion = input("Veuillez saisir la plaque du camion du balayeur: ")
                # On controlle si plaque_camion est un entier de 3 chiffres
                if plaque_camion.isdigit() and len(plaque_camion) == 3:
                    # On contrôle si cette plaque_camion existe dans la table CamionsOrdure
                    cur.execute("SELECT * FROM CamionsOrdure WHERE plaqueCamion = ?", (plaque_camion,))
                    if not cur.fetchone():
                        print("Attention: Ce numéro de plaque de camion n'existe pas dans la table CamionsOrdure.")
                        reponse = input(
                            "Voulez-vous quand même ajouter ce camion à la table CamionsOrdure (o/toute autre touche pour dire non): ").lower()
                        if reponse.lower() != "o":
                            print("Donc vous allez chosir selon la liste des plaques")
                            abandonner_prompt(menu_inserer, connexion)
                            while True:
                                cur.execute("SELECT plaqueCamion FROM CamionsOrdure")
                                available_camions = [row[0] for row in cur.fetchall()]
                                print("Liste de plaques de camion : ", available_camions)
                                plaque_camion = int(
                                    input("Alors veuillez saisir le plaque du camion selon la liste : "))
                                if plaque_camion in available_camions:
                                    break
                                else:
                                    print(
                                        "Erreur: Ce plaque de camion n'existe pas dans la liste des plaques disponibles. Veuillez choisir un plaque valide.")
                                    abandonner_prompt(menu_inserer, connexion)
                        else:
                            inserer_dans_camions(connexion, plaque_camion)
                            break
                    break
                print("Erreur: La plaque du camion doit être un nombre entier de 3 chiffres.")
                abandonner_prompt(menu_inserer, connexion)
            # Si toutes passes bien On ajout a la table
            cur.execute("""
                            INSERT INTO Balayeurs (idBalayeur, pseudoBalayeur, telBalayeur, plaqueCamion)
                            VALUES (?, ?, ?, ?)
                            """, (id_balayeur, pseudo_balayeur, tel_balayeur, plaque_camion))

            # Sauvegarde les modifications
            connexion.commit()

            print("Le balayeur a été inséré avec succès à la table Balayeurs.")
            break  # Arrêt du boucle

        except ValueError as ve:
            print("Erreur:", ve)

        except sqlite3.Error as e:
            print("SQLite erreur:", e)
    user_reponse = input("Voulez-vous inserer un autre balayeur (o/toute autre touche pour dire non): ").lower()
    print("")
    if user_reponse == "o":
        inserer_dans_balayeurs(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            # Reappel de fonction menu_inserer
            menu_inserer(connexion)
        else:
            quit()


def inserer_dans_quartiers(connexion, code_quartier=None):
    print("2.Inserer dans le tableau des quartiers")
    if code_quartier:
        ne_rentre_pas = True
    else:
        ne_rentre_pas = False
    cur = connexion.cursor()
    while True:
        try:
            if not code_quartier:
                while True:
                    code_quartier = (input("Veuillez saisir le code du quartier: "))
                    # On controlle si code_quartier est un entier de 2 chiffres
                    if code_quartier.isdigit() and len(code_quartier) == 2:
                        # On controlle si cette code_quartier existe déja
                        cur.execute("SELECT * FROM Quartiers WHERE codeQuartier = ?", (code_quartier,))
                        if cur.fetchone():
                            print(
                                "Erreur: Un quartier avec cet code existe déjà. Veuillez saisir un code quartier unique.")
                            abandonner_prompt(menu_inserer, connexion)
                            continue  # Essayer encore
                        break
                    print("Erreur: Le code du quartier doit être un nombre entier de 2 chiffres.")
                    abandonner_prompt(menu_inserer, connexion)
            while True:
                nom_quartier = input("Veuillez saisir le nom du quartier: ")
                # On controlle si nom_quartier est un mot
                if nom_quartier.strip() and nom_quartier.isalnum():
                    break
                print("Erreur: Le nom du quartier doit être un mot.")
                abandonner_prompt(menu_inserer, connexion)
            while True:
                pop_quartier = input("Veuillez saisir le population du quartier: ")
                # On controlle si pop_quartier est un entier
                if pop_quartier.isdigit():
                    break
                print("Erreur: Le population du quartier doit être un entier .")
                abandonner_prompt(menu_inserer, connexion)
            while True:
                nb_poubelles = input("Veuillez saisir le nombre des poubelles du quartier: ")
                # On controlle si nb_poubelles est un entier de 2 chiffres
                if nb_poubelles.isdigit() and len(nb_poubelles) == 2:
                    break
                print("Erreur: Le nombre des poubelles du quartier doit être un nombre entier de 2 chiffres.")
                abandonner_prompt(menu_inserer, connexion)
            # Si toutes passes bien On ajout a la table
            cur.execute("""
                                INSERT INTO Quartiers (codeQuartier, nomQuartier, popQuartier, nb_poubQuartier)
                                VALUES (?, ?, ?, ?)
                                """, (code_quartier, nom_quartier, pop_quartier, nb_poubelles))

            # Sauvegarde les modifications
            connexion.commit()

            print("Le quartier a été inséré avec succès à la table Quartiers.")
            break  # Arrêt du boucle

        except ValueError as ve:
            print("Erreur:", ve)

        except sqlite3.Error as e:
            print("SQLite erreur:", e)
    if not ne_rentre_pas:
        user_reponse = input("Voulez-vous inserer un autre quartier (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            inserer_dans_balayeurs(connexion)
        else:
            user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
            print("")
            if user_reponse == "o":
                # Reappel de fonction menu_inserer
                menu_inserer(connexion)
            else:
                quit()


def inserer_dans_camions(connexion, plaque_camion=None):
    print("3.Inserer dans le tableau des camions à ordure")
    if plaque_camion:
        ne_rentre_pas = True
    else:
        ne_rentre_pas = False

    cur = connexion.cursor()
    while True:
        try:
            if not plaque_camion:
                while True:
                    plaque_camion = input("Veuillez saisir la plaque du camion: ")
                    # On vérifie si plaque_camion est un entier de 3 chiffres
                    if plaque_camion.isdigit() and len(plaque_camion) == 3:
                        # On vérifie si cette plaque_camion existe déjà dans la table CamionsOrdure
                        cur.execute("SELECT * FROM CamionsOrdure WHERE plaqueCamion = ?", (plaque_camion,))
                        if cur.fetchone():
                            print("Erreur: Un camion avec cette plaque existe déjà. Veuillez saisir une plaque unique.")
                            abandonner_prompt(menu_inserer, connexion)
                            continue  # Réessayer
                        break
                    print("Erreur: La plaque du camion doit être un nombre entier de 3 chiffres.")
                    abandonner_prompt(menu_inserer, connexion)

            while True:
                cap_eq_camion = input("Veuillez saisir la capacité d'équipe du camion: ")
                # On controlle si cap_eq_camion est un entier de 2 chiffres
                if cap_eq_camion.isdigit() and len(cap_eq_camion) == 2:
                    break
                print("Erreur: la capacité d'équipe du camion doit être un entier de 2 chiffres.")
                abandonner_prompt(menu_inserer, connexion)

            while True:
                nom_modele = input("Veuillez saisir le nom de modèle du camion: ")
                # On contrôle si cette nom_modele existe dans la table Modeles
                cur.execute("SELECT * FROM Modeles WHERE nomModele = ?", (nom_modele,))
                if not cur.fetchone():
                    print("Attention: Ce nom de modèle  n'existe pas dans la table Modeles.")
                    reponse = input(
                        "Voulez-vous quand même ajouter ce modèle à la table Modeles (o/toute autre touche pour dire non): ").lower()
                    if reponse.lower() != "o":
                        print("Donc vous allez chosir selon la liste modelès")
                        abandonner_prompt(menu_inserer, connexion)
                        while True:
                            cur.execute("SELECT nomModele FROM Modeles")
                            available_modeles = [row[0] for row in cur.fetchall()]
                            print("liste de noms de modèle : ", available_modeles)
                            nom_modele = input("Alors veuillez saisir le nom de modèle selon la liste : ")
                            if nom_modele in available_modeles:
                                break
                            else:
                                print(
                                    "Erreur: Ce nom de modèle n'existe pas dans la liste des modèles disponibles. Veuillez choisir un nom valide.")
                                abandonner_prompt(menu_inserer, connexion)
                    else:
                        inserer_dans_modeles(connexion, nom_modele)
                        break
                break
            cur = connexion.cursor()  # cette partie est ajouté apres
            while True:
                cur.execute("SELECT nomCentre FROM CentresOrdure")
                available_centres = [row[0] for row in cur.fetchall()]
                print("liste de noms de centre : ", available_centres)
                nom_centre = input("Veuillez saisir le nom du centre du camion: ")
                if nom_centre in available_centres:
                    break
                else:
                    print(
                        "Erreur: Ce nom de centre n'existe pas dans la liste des centres disponibles. Veuillez choisir un nom valide.")
                    abandonner_prompt(menu_inserer, connexion)
            # Si toutes les informations sont valides, insérer le camion dans la table CamionsOrdure
            cur.execute("""
                INSERT INTO CamionsOrdure (plaqueCamion,cap_eqCamion, nomModele, nomCentre)
                VALUES (?, ?, ?, ?)
            """, (plaque_camion,cap_eq_camion, nom_modele, nom_centre))

            # Pour méttre a jour la quantité du dechet dans la camionsOrdure
            db.mise_a_jour_bd(connexion, "data/view.sql")

            connexion.commit()
            print("Le camion a été ajouté avec succès à la table CamionsOrdure.")
            break

        except ValueError as ve:
            print("Erreur:", ve)

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)
    if not ne_rentre_pas:
        user_reponse = input("Voulez-vous insérer un autre camion (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            inserer_dans_camions(connexion)
        else:
            user_reponse = input("Voulez-vous faire une autre opération (o/toute autre touche pour dire non): ").lower()
            print("")
            if user_reponse == "o":
                # Reappel de la fonction menu_inserer
                menu_inserer(connexion)
            else:
                quit()


def inserer_dans_modeles(connexion, nom_modele=None):
    print("4.Inserer dans le tableau des modeles")
    if nom_modele:
        ne_rentre_pas = True
    else:
        ne_rentre_pas = False

    cur = connexion.cursor()
    while True:
        try:
            if not nom_modele:
                while True:
                    nom_modele = input("Veuillez saisir la nom de modèle: ")
                    # On controlle si cette nom_modele existe déja
                    cur.execute("SELECT * FROM Modeles WHERE nomModele = ?", (nom_modele,))
                    if cur.fetchone():
                        print(
                            "Erreur: Un modele avec ce nom existe déjà. Veuillez saisir un autre nom de modèle unique.")
                        abandonner_prompt(menu_inserer, connexion)
                        continue  # Essayer encore
                    break

            while True:
                # On controlle si taille_modele est dans la liste [‘Petit’, ‘Moyen’, ‘Grand’]
                liste_taille = ["Petit", "Moyen", "Grand"]
                print("Liste des tailles de modèle : ", liste_taille)
                taille_modele = input("Veuillez saisir le taille du modèle: ")
                if taille_modele in liste_taille:
                    break
                else:
                    print(
                        "Erreur: Ce taille de modèle n'existe pas dans la liste des tailles disponibles. Veuillez choisir un taille valide.")
                    abandonner_prompt(menu_inserer, connexion)

            while True:
                cap_dep_max = input("Veuillez saisir la capacité maximum du camion: ")
                # On controlle si cap_dep_max est un entier de 3 chiffres
                if cap_dep_max.isdigit() and len(cap_dep_max) == 3:
                    break
                print("Erreur: a capacité maximum du camion doit être un entier de 3 chiffres.")
                abandonner_prompt(menu_inserer, connexion)

            # Si toutes les informations sont valides, insérer le camion dans la table CamionsOrdure
            cur.execute("""
                INSERT INTO Modeles (nomModele, tailleModele, cap_dep_maxModele)
                VALUES (?, ?, ?)
            """, (nom_modele, taille_modele, cap_dep_max))
            connexion.commit()
            print("Le modèle a été ajouté avec succès à la table Modeles.")
            break

        except ValueError as ve:
            print("Erreur:", ve)

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    if not ne_rentre_pas:
        user_reponse = input("Voulez-vous insérer un autre modèle (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            inserer_dans_camions(connexion)
        else:
            user_reponse = input("Voulez-vous faire une autre opération (o/toute autre touche pour dire non): ").lower()
            print("")
            if user_reponse == "o":
                # Reappel de la fonction menu_inserer
                menu_inserer(connexion)
            else:
                quit()


def inserer_dans_centres(connexion):
    print("5.Inserer dans le tableau des centres à ordure")
    cur = connexion.cursor()
    while True:
        try:
            while True:
                nom_centre = (input("Veuillez saisir le nom du centre: "))
                # On controlle si cette nom_centre existe déja
                cur.execute("SELECT * FROM CentresOrdure WHERE nomCentre = ?", (nom_centre,))
                if cur.fetchone():
                    print("Erreur: Un centre avec ce nom existe déjà. Veuillez saisir un nom unique.")
                    abandonner_prompt(menu_inserer, connexion)
                    continue  # Essayer encore
                break

            while True:
                cap_centre = input("Veuillez saisir le capacité de centre: ")
                # On controlle si cap_centre est un entier
                if cap_centre.isdigit():
                    break
                print("Erreur: Le capacité de centre doit être un entier .")
                abandonner_prompt(menu_inserer, connexion)

            # Si toutes passes bien On ajout a la table
            cur.execute("""
                                INSERT INTO CentresOrdure (nomCentre, capCentre)
                                VALUES (?, ?)
                                """, (nom_centre, cap_centre))

            # Sauvegarde les modifications
            connexion.commit()

            print("Le centre a été inséré avec succès à la table CentresOrdures.")
            break  # Arrêt du boucle

        except ValueError as ve:
            print("Erreur:", ve)

        except sqlite3.Error as e:
            print("SQLite erreur:", e)
    user_reponse = input("Voulez-vous insérer un autre centre (o/toute autre touche pour dire non): ").lower()
    print("")
    if user_reponse == "o":
        inserer_dans_centres(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            # Reappel de fonction menu_inserer
            menu_inserer(connexion)
        else:
            quit()


def inserer_dans_programmations(connexion):
    print("6.Inserer dans le tableau des programmations")
    cur = connexion.cursor()
    cles_primaires_unique = False
    while True:
        try:
            while not cles_primaires_unique:
                while True:
                    code_quartier = input("Veuillez saisir le code du quartier: ")
                    # On controlle si code_quartier est un entier de 2 chiffres
                    if code_quartier.isdigit() and len(code_quartier) == 2:
                        # On contrôle si cette code_quartier existe dans la table Quartiers
                        cur.execute("SELECT * FROM Quartiers WHERE codeQuartier = ?", (code_quartier,))
                        if not cur.fetchone():
                            print("Attention: Ce code quartier  n'existe pas dans la table Quartiers.")
                            reponse = input(
                                "Voulez-vous quand même ajouter ce quartier à la table Quartier (o/toute autre touche pour dire non): ").lower()
                            if reponse.lower() != "o":
                                print("Donc vous allez chosir selon la liste de codes de quartier")
                                abandonner_prompt(menu_inserer, connexion)
                                while True:
                                    cur.execute("SELECT codeQuartier FROM Quartiers")
                                    available_quartiers = [row[0] for row in cur.fetchall()]
                                    print("liste des codes de quartier : ", available_quartiers)
                                    code_quartier = int(
                                        input("Alors veuillez saisir le code de quartier selon la liste : "))
                                    if code_quartier in available_quartiers:
                                        break
                                    else:
                                        print(
                                            "Erreur: Ce nom de modèle n'existe pas dans la liste des modèles disponibles. Veuillez choisir un nom valide.")
                                        abandonner_prompt(menu_inserer, connexion)
                            else:
                                inserer_dans_quartiers(connexion, code_quartier)
                                break
                        break
                    print("Erreur: le code de quartier doit être un entier de 2 chiffres.")
                    abandonner_prompt(menu_inserer, connexion)
                while True:
                    plaque_camion = input("Veuillez saisir la plaque du camion: ")
                    # On controlle si plaque_camion est un entier de 3 chiffres
                    if plaque_camion.isdigit() and len(plaque_camion) == 3:
                        # On contrôle si cette plaque_camion existe dans la table CamionsOrdures
                        cur.execute("SELECT * FROM CamionsOrdure WHERE plaqueCamion = ?", (plaque_camion,))
                        if not cur.fetchone():
                            print("Attention: Ce plaque camion  n'existe pas dans la table CamionsOrdure.")
                            reponse = input(
                                "Voulez-vous quand même ajouter ce plaque à la table CamionsOrdure (o/toute autre touche pour dire non): ").lower()
                            if reponse.lower() != "o":
                                print("Donc vous allez chosir selon la liste plaques")
                                abandonner_prompt(menu_inserer, connexion)
                                while True:
                                    cur.execute("SELECT plaqueCamion FROM CamionsOrdure")
                                    available_plaques = [row[0] for row in cur.fetchall()]
                                    print("liste des plaques de camion : ", available_plaques)
                                    plaque_camion = int(
                                        input("Alors veuillez saisir la plaque du camion selon la liste : "))
                                    if plaque_camion in available_plaques:
                                        break
                                    else:
                                        print(
                                            "Erreur: Cette plaque de camion n'existe pas dans la liste des plaques disponibles. Veuillez choisir un plaque valide.")
                                        abandonner_prompt(menu_inserer, connexion)
                            else:
                                inserer_dans_camions(connexion, plaque_camion)
                                break
                        if check_capacity_and_insert(connexion, code_quartier, plaque_camion):
                            break
                        else:
                            abandonner_prompt(menu_inserer, connexion)
                            continue
                    print("Erreur: la plaque de camion doit être un entier de 3 chiffres.")
                    abandonner_prompt(menu_inserer, connexion)

                # On contrôlle si cette deux clés primaires éxiste déjà dans une meme ligne du tableau Programmations
                cur.execute("SELECT * FROM Programmations WHERE codeQuartier = ? and plaqueCamion = ?",
                            (code_quartier, plaque_camion))
                if cur.fetchone():
                    print(
                        "Erreur: Il existe deja cette code_quartier et plaque_camion dans la meme ligne du table Programmations (clés primaires en même temp)!!!")
                    print("Donc veuillez réesayer")
                    abandonner_prompt(menu_inserer, connexion)
                else:
                    cles_primaires_unique = True

            while True:
                heure_prog = input("Veuillez saisir l'heure de la programmation (HH:MM): ")
                # Créer un motif regex pour le contrôle (TRIGGER)
                heure_pattern = re.compile(r'^(0[5-9]|1[0-8]):[0-5][0-9]$')
                # Vérifier s'il correspond au modèle de heure saisi
                if heure_pattern.match(heure_prog):
                    break
                print("Erreur: Le format de l'heure doit être HH:MM et entre 05:00 et 18:59.")
                abandonner_prompt(menu_inserer, connexion)

            # Si toutes passes bien On ajout a la table
            cur.execute("""
                                INSERT INTO Programmations (codeQuartier, plaqueCamion, heureProg)
                                VALUES (?, ?, ?)
                                """, (code_quartier, plaque_camion, heure_prog))

            # Pour méttre a jour la quantité du dechet dans la camionsOrdure
            db.mise_a_jour_bd(connexion, "data/view.sql")

            # Sauvegarde les modifications
            connexion.commit()

            print("Le programmation a été inséré avec succès à la table Programmations.")
            break  # Arrêt du boucle

        except ValueError as ve:
            print("Erreur:", ve)

        except sqlite3.Error as e:
            print("SQLite erreur:", e)

    user_reponse = input("Voulez-vous inserer un autre programmations (o/toute autre touche pour dire non): ").lower()
    print("")
    if user_reponse == "o":
        inserer_dans_programmations(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            # Reappel de fonction menu_inserer
            menu_inserer(connexion)
        else:
            quit()


########################Fonction Mettre à Jour#########################


def mettre_jour_balayeur(connexion):
    print("1.Mettre à jour un balayeur\n")

    # Fonction pour afficher liste des balayeurs avec leur ids et leur pseudos
    def afficher_liste_balayeurs(connexion):
        cur = connexion.cursor()
        try:
            cur.execute("SELECT idBalayeur, pseudoBalayeur FROM Balayeurs")
            rows = cur.fetchall()
            # Créer des titres de colonnes
            headers = ["idBalayeur", "pseudoBalayeur", ]
            # Formatage correct des données du tableau
            table_data = [headers] + rows

            # Imprimer le tableau à l'aide de tabulate
            print("Liste des balayeurs:")
            print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    cur = connexion.cursor()
    while True:
        try:
            afficher_liste_balayeurs(connexion)
            print()

            id_balayeur = input("Veuillez saisir l'ID du balayeur à mettre à jour: ")
            # Vérifie que l'identifiant Balayeurun a été correctement saisi
            cur.execute("SELECT * FROM Balayeurs WHERE idBalayeur = ?", (id_balayeur,))
            balayeur = cur.fetchone()
            if balayeur:
                print("Balayeur trouvé. Voici les informations actuelles:\n")
                print("ID du balayeur:", balayeur[0])
                print("Pseudo du balayeur:", balayeur[1])
                print("Numéro de téléphone du balayeur:", balayeur[2])
                print("Plaque du camion du balayeur:", balayeur[3])
                print()

                # Demande à l'utilisateur quelles sont les informations qu'il souhaite mettre à jour
                print("Quelle information souhaitez-vous mettre à jour ?")
                print("1) Pseudo du balayeur")
                print("2) Numéro de téléphone du balayeur")
                print("3) Plaque du camion du balayeur")
                choix = input("Votre choix (1/2/3): ")

                if choix == "1":
                    while True:
                        nouveau_pseudo = input("Veuillez saisir le nouveau pseudo du balayeur: ")
                        # On controlle si nouveau_pseudo est un mot
                        if nouveau_pseudo.strip() and nouveau_pseudo.isalpha():
                            break
                        print("Erreur: Le pseudo du balayeur doit être un mot.")
                        abandonner_prompt(menu_mettre_jour, connexion)
                    cur.execute("UPDATE Balayeurs SET pseudoBalayeur = ? WHERE idBalayeur = ?",
                                (nouveau_pseudo, id_balayeur))
                    print("Pseudo du balayeur mis à jour avec succès.")
                    break
                elif choix == "2":
                    while True:
                        nouveau_tel = input("Veuillez saisir le nouveau numéro de téléphone du balayeur: ")
                        # On controlle si tel_balayeur est un entier de 9 chiffres
                        if nouveau_tel.isdigit() and len(nouveau_tel) == 9:
                            break
                        print("Erreur: Le numéro de téléphone doit être un entier de 9 chiffres.")
                        abandonner_prompt(menu_mettre_jour, connexion)
                    cur.execute("UPDATE Balayeurs SET telBalayeur = ? WHERE idBalayeur = ?", (nouveau_tel, id_balayeur))
                    print("Numéro de téléphone du balayeur mis à jour avec succès.")
                    break
                elif choix == "3":
                    while True:
                        nouvelle_plaque = input("Veuillez saisir la nouvelle plaque du camion du balayeur: ")
                        # On controlle si nouvelle_plaque est un entier de 3 chiffres
                        if nouvelle_plaque.isdigit() and len(nouvelle_plaque) == 3:
                            cur.execute("SELECT * FROM CamionsOrdure WHERE plaqueCamion = ?", (nouvelle_plaque,))
                            if not cur.fetchone():
                                print(
                                    "Attention: Ce numéro de plaque de camion n'existe pas dans la table CamionsOrdure.")
                                print("Donc vous allez chosir selon la liste des plaques")
                                abandonner_prompt(menu_mettre_jour, connexion)
                                while True:
                                    cur.execute("SELECT plaqueCamion FROM CamionsOrdure")
                                    available_camions = [row[0] for row in cur.fetchall()]
                                    print("Liste des plaques de camion : ", available_camions)
                                    plaque_camion = int(
                                        input("Alors veuillez saisir la plaque du camion selon la liste : "))
                                    if plaque_camion in available_camions:
                                        break
                                    else:
                                        print(
                                            "Erreur: Cette plaque de camion n'existe pas dans la liste des plaques disponibles. Veuillez choisir un plaque valide.")
                                        abandonner_prompt(menu_mettre_jour, connexion)

                            cur.execute("UPDATE Balayeurs SET plaqueCamion = ? WHERE idBalayeur = ?",
                                        (nouvelle_plaque, id_balayeur))
                            print("Plaque du camion du balayeur mis à jour avec succès.")
                            break
                        print("Erreur: La plaque du camion doit être un nombre entier de 3 chiffres.")
                        abandonner_prompt(menu_mettre_jour, connexion)
                else:
                    print("Choix invalide.")
                    abandonner_prompt(menu_mettre_jour, connexion)
            else:
                print(
                    "Erreur: Ce id de balayeur n'existe pas dans la liste des balayeurs disponibles. Veuillez choisir un id valide.")
                abandonner_prompt(menu_mettre_jour, connexion)

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    user_reponse = input("Voulez-vous mettre à jour un autre balayeur (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        mettre_jour_balayeur(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print()
        if user_reponse == "o":
            # Reappel de fonction menu_mettre_jour
            menu_mettre_jour(connexion)
        else:
            quit()


def mettre_jour_quartier(connexion):
    print("2.Mettre à jour un quartier\n")

    # Fonction pour afficher liste des quartiers avec leur codes et leur noms
    def afficher_liste_quartiers(connexion):
        cur = connexion.cursor()
        try:
            cur.execute("SELECT codeQuartier, nomQuartier FROM Quartiers")
            rows = cur.fetchall()
            # Créer des titres de colonnes
            headers = ["codeQuartier", "nomQuartier"]

            # Formatage correct des données du tableau
            table_data = [headers] + rows

            # Imprimer le tableau à l'aide de tabulate
            print("Liste des quartiers:")
            print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    cur = connexion.cursor()
    while True:
        try:
            afficher_liste_quartiers(connexion)
            print()

            code_quartier = input("Veuillez saisir le code du quartier à mettre à jour: ")
            # Vérifie que l'identifiant code_quartier a été correctement saisi
            cur.execute("SELECT * FROM Quartiers WHERE codeQuartier = ?", (code_quartier,))
            quartier = cur.fetchone()
            if quartier:
                print("Quartier trouvé. Voici les informations actuelles:\n")
                print("Code du quartier:", quartier[0])
                print("Nom du quartier:", quartier[1])
                print("Population du quartier:", quartier[2])
                print("Nombre des poubelles du quartier:", quartier[3])
                print()

                # Demande à l'utilisateur quelles sont les informations qu'il souhaite mettre à jour
                print("Quelle information souhaitez-vous mettre à jour ?")
                print("1) Nom du quartier")
                print("2) Population du quartier")
                print("3) Nombre des poubelles du quartier")
                choix = input("Votre choix (1/2/3): ")

                if choix == "1":
                    while True:
                        nouveau_nom = input("Veuillez saisir le nouveau nom du quartier: ")
                        # On controlle si nouveau_nom est un mot
                        if nouveau_nom.strip() and nouveau_nom.isalnum():
                            break
                        print("Erreur: Le nom du quartier doit être un mot.")
                        abandonner_prompt(menu_mettre_jour, connexion)
                    cur.execute("UPDATE Quartiers SET nomQuartier = ? WHERE codeQuartier = ?",
                                (nouveau_nom, code_quartier))
                    print("Nom du quartier mis à jour avec succès.")
                    break

                elif choix == "2":
                    while True:
                        nouveau_population = input("Veuillez saisir le nouveau population du quartier: ")
                        # On controlle si nouveau_population est un entier de 9 chiffres
                        if nouveau_population.isdigit():
                            break
                        print("Erreur: Le population du quartier doit être un entier .")
                        abandonner_prompt(menu_mettre_jour, connexion)
                    cur.execute("UPDATE Quartiers SET popQuartier = ? WHERE codeQuartier = ?",
                                (nouveau_population, code_quartier))
                    print("Population du quartier mis à jour avec succès.")
                    break

                elif choix == "3":
                    while True:
                        nouvelle_nb_poubelles = input("Veuillez saisir la nouvelle nombre des poubelles du quartier: ")
                        # On controlle si nouvelle_nb_poubelles est un entier de 2 chiffres
                        if nouvelle_nb_poubelles.isdigit() and len(nouvelle_nb_poubelles) == 2:
                            break
                        print("Erreur: Le nombre des poubelles du quartier doit être un nombre entier de 2 chiffres.")
                        abandonner_prompt(menu_mettre_jour, connexion)
                    cur.execute("UPDATE Quartiers SET nb_poubQuartier = ? WHERE codeQuartier = ?",
                                (nouvelle_nb_poubelles, code_quartier))
                    print("Nombre des poubelles du quartier mis à jour avec succès.")
                    break

                else:
                    print("Choix invalide.")
                    abandonner_prompt(menu_mettre_jour, connexion)
            else:
                print(
                    "Erreur: Ce code de quartier n'existe pas dans la liste des quartiers disponibles. Veuillez choisir un code valide.")
                abandonner_prompt(menu_mettre_jour, connexion)

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    user_reponse = input("Voulez-vous mettre à jour un autre quartier (o/toute autre touche pour dire non): ").lower()
    print("")
    if user_reponse == "o":
        mettre_jour_quartier(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            # Reappel de fonction menu_mettre_jour
            menu_mettre_jour(connexion)
        else:
            quit()


def mettre_jour_camion(connexion):
    print("3.Mettre à jour un camion\n")

    # Fonction pour afficher liste des camions avec leur plaques et leur models
    def afficher_liste_camion(connexion):
        cur = connexion.cursor()
        try:
            cur.execute("SELECT plaqueCamion, nomModele FROM CamionsOrdure")
            rows = cur.fetchall()
            # Créer des titres de colonnes
            headers = ["plaqueCamion", "nomModele"]

            # Formatage correct des données du tableau
            table_data = [headers] + rows

            # Imprimer le tableau à l'aide de tabulate
            print("Liste des camions:")
            print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    cur = connexion.cursor()
    while True:
        try:
            afficher_liste_camion(connexion)
            print()
            plaque_camion = input("Veuillez saisir la plaque du camion à mettre à jour: ")
            # Vérifie que l'identifiant plaque_camion a été correctement saisi
            cur.execute("SELECT * FROM CamionsOrdure WHERE plaqueCamion = ?", (plaque_camion,))
            camion = cur.fetchone()
            if camion:
                print("Camion trouvé. Voici les informations actuelles:\n")
                print("Plaque du camion:", camion[0])
                print("Capacité d'équipe du camion:", camion[1])
                print("Nom de modèle du camion:", camion[2])
                print("Nom de centre du camion:", camion[3])
                print("Quantité de déchet du camion:", camion[4])
                print()

                # Demande à l'utilisateur quelles sont les informations qu'il souhaite mettre à jour
                print("Quelle information souhaitez-vous mettre à jour ?")
                print("1) Capacité d'équipe du camion")
                print("2) Nom de modèle du camion")
                print("3) Nom de centre du camion")
                choix = input("Votre choix (1/2/3): ")

                if choix == "1":
                    while True:
                        nouveau_cap_eq = input("Veuillez saisir le nouveau capacité d'équipe du camion: ")
                        # On controlle si cap_eq_camion est un entier de 2 chiffres
                        if nouveau_cap_eq.isdigit() and len(nouveau_cap_eq) == 2:
                            break
                        print("Erreur: la capacité d'équipe du camion doit être un entier de 2 chiffres.")
                        abandonner_prompt(menu_mettre_jour, connexion)
                    cur.execute("UPDATE CamionsOrdure SET cap_eqCamion = ? WHERE plaqueCamion = ?",
                                (nouveau_cap_eq, plaque_camion))
                    print("Capacité d'équipe du camion mis à jour avec succès.")
                    break

                elif choix == "2":
                    while True:
                        nouvelle_modele = input("Veuillez saisir la nouvelle nom de modèle du camion ")
                        cur.execute("SELECT * FROM Modeles WHERE nomModele = ?", (nouvelle_modele,))
                        if not cur.fetchone():
                            print("Attention: Ce nom de modèle du camion n'existe pas dans la table Modeles.")
                            print("Donc vous allez chosir selon la liste des modelès")
                            abandonner_prompt(menu_mettre_jour, connexion)
                            while True:
                                cur.execute("SELECT nomModele FROM Modeles")
                                available_modeles = [row[0] for row in cur.fetchall()]
                                print("Liste de modèle du camion : ", available_modeles)
                                nouvelle_modele = input("Alors veuillez saisir le modèle du camion selon la liste : ")
                                if nouvelle_modele in available_modeles:
                                    break
                                else:
                                    print(
                                        "Erreur: Ce modèle de camion n'existe pas dans la liste des modèles disponibles. Veuillez choisir un modèle valide.")
                                    abandonner_prompt(menu_mettre_jour, connexion)

                        cur.execute("UPDATE CamionsOrdure SET nomModele = ? WHERE plaqueCamion = ?",
                                    (nouvelle_modele, plaque_camion))
                        print("Nom de modèle du camion mis à jour avec succès.")
                        break
                    break
                elif choix == "3":
                    while True:
                        nouvelle_centre = input("Veuillez saisir la nouvelle nom de centre du camion ")
                        cur.execute("SELECT * FROM CentresOrdure WHERE nomCentre = ?", (nouvelle_centre,))
                        if not cur.fetchone():
                            print("Attention: Ce nom de centre n'existe pas dans la table CentresOrdure.")
                            print("Donc vous allez chosir selon la liste des centres")
                            abandonner_prompt(menu_mettre_jour, connexion)
                            while True:
                                cur.execute("SELECT nomCentre FROM CentresOrdure")
                                available_centres = [row[0] for row in cur.fetchall()]
                                print("Liste de centres  : ", available_centres)
                                nouvelle_centre = input("Alors veuillez saisir le nom du centre selon la liste : ")
                                if nouvelle_centre in available_centres:
                                    break
                                else:
                                    print(
                                        "Erreur: Ce nom du centre n'existe pas dans la liste des centres disponibles. Veuillez choisir un nom valide.")
                                    abandonner_prompt(menu_mettre_jour, connexion)

                        cur.execute("UPDATE CamionsOrdure SET nomCentre = ? WHERE plaqueCamion = ?",
                                    (nouvelle_centre, plaque_camion))
                        print("Nom du centre du camion mis à jour avec succès.")
                        break
                    break

                else:
                    print("Choix invalide.")
                    abandonner_prompt(menu_mettre_jour, connexion)
            else:
                print(
                    "Erreur: Ce plaque de camion n'existe pas dans la liste des plaques disponibles. Veuillez choisir un plaque valide.")
                abandonner_prompt(menu_mettre_jour, connexion)

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    user_reponse = input("Voulez-vous mettre à jour un autre camion (o/toute autre touche pour dire non): ").lower()
    print()
    if user_reponse == "o":
        mettre_jour_camion(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print()
        if user_reponse == "o":
            # Reappel de fonction menu_mettre_jour
            menu_mettre_jour(connexion)
        else:
            quit()


def mettre_jour_modele(connexion):
    print("4.Mettre à jour un modèle\n")

    # Fonction pour afficher liste des modeles avec leur nomes et leur tailles
    def afficher_liste_modeles(connexion):
        cur = connexion.cursor()
        try:
            cur.execute("SELECT nomModele, tailleModele FROM Modeles")
            rows = cur.fetchall()
            # Créer des titres de colonnes
            headers = ["nomModele", "tailleModele"]

            # Formatage correct des données du tableau
            table_data = [headers] + rows

            # Imprimer le tableau à l'aide de tabulate
            print("Liste des modeles:")
            print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))


        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    cur = connexion.cursor()
    while True:
        try:
            afficher_liste_modeles(connexion)
            print()
            nom_modele = input("Veuillez saisir le nom du modèle à mettre à jour: ")
            # Vérifie que le nom modèle a été correctement saisi
            cur.execute("SELECT * FROM Modeles WHERE nomModele = ?", (nom_modele,))
            modele = cur.fetchone()
            if modele:
                print("Modèle trouvé. Voici les informations actuelles:\n")
                print("Nom du modèle:", modele[0])
                print("Taille du modèle:", modele[1])
                print("Capacité maximum du modèle:", modele[2])
                print()

                # Demande à l'utilisateur quelles sont les informations qu'il souhaite mettre à jour
                print("Quelle information souhaitez-vous mettre à jour ?")
                print("1) Taille du modèle")
                print("2) Capacité maximum du modèle")
                choix = input("Votre choix (1/2): ")

                if choix == "1":
                    while True:
                        # On controlle si taille_modele est dans la liste [‘Petit’, ‘Moyen’, ‘Grand’]
                        liste_taille = ["Petit", "Moyen", "Grand"]
                        print("Liste des tailles de modèle : ", liste_taille)
                        nouveau_taille = input("Veuillez saisir le nouveau taille du modèle: ")
                        if nouveau_taille in liste_taille:
                            break
                        else:
                            print("Erreur: Ce taille de modèle n'existe pas dans la liste des tailles disponibles. Veuillez choisir un taille valide.")
                            abandonner_prompt(menu_inserer, connexion)
                    cur.execute("UPDATE Modeles SET tailleModele = ? WHERE nomModele = ?", (nouveau_taille, nom_modele))
                    print("Taille du modèle mis à jour avec succès.")
                    break

                elif choix == "2":
                    while True:
                        nouveau_cap_dep = input("Veuillez saisir le nouveau capacité maximum du modèle: ")
                        # On controlle si nouveau_cap_dep est un entier de 3 chiffres
                        if nouveau_cap_dep.isdigit() and len(nouveau_cap_dep) == 3:
                            break
                        print("Erreur: a capacité maximum du camion doit être un entier de 3 chiffres.")
                        abandonner_prompt(menu_mettre_jour, connexion)


                    if check_capacity_and_mettre_jour(connexion, nom_modele, nouveau_cap_dep):
                        cur.execute("UPDATE Modeles SET cap_dep_maxModele = ? WHERE nomModele = ?",
                                    (nouveau_cap_dep, nom_modele))
                        print("Capacité maximum du modèle mis à jour avec succès.")
                        break
                    else :
                        abandonner_prompt(menu_mettre_jour, connexion)
                        continue


                else:
                    print("Choix invalide.")
                    abandonner_prompt(menu_mettre_jour, connexion)
            else:
                print(
                    "Erreur: Ce nom du modèle n'existe pas dans la liste des modèles disponibles. Veuillez choisir un nom valide.")
                abandonner_prompt(menu_mettre_jour, connexion)

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    user_reponse = input("Voulez-vous mettre à jour un autre modèle (o/toute autre touche pour dire non): ").lower()
    print("")
    if user_reponse == "o":
        mettre_jour_modele(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            # Reappel de fonction menu_mettre_jour
            menu_mettre_jour(connexion)
        else:
            quit()


def mettre_jour_centre(connexion):
    print("6.Mettre à jour un programmation\n")

    # Fonction pour afficher liste des centres avec leur noms et leur capacités
    def afficher_liste_centres(connexion):
        cur = connexion.cursor()
        try:
            cur.execute("SELECT nomCentre, capCentre FROM CentresOrdure")
            rows = cur.fetchall()
            # Créer des titres de colonnes
            headers = ["nomCentre", "capCentre"]

            # Formatage correct des données du tableau
            table_data = [headers] + rows

            # Imprimer le tableau à l'aide de tabulate
            print("Liste des centres:")
            print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    cur = connexion.cursor()
    while True:
        try:
            afficher_liste_centres(connexion)
            print()
            nom_centre = input("Veuillez saisir le nom du centre à mettre à jour: ")
            # Vérifie que le nom_centre a été correctement saisi
            cur.execute("SELECT * FROM CentresOrdure WHERE nomCentre = ?", (nom_centre,))
            centre = cur.fetchone()
            if centre:
                print("Centre trouvé. Voici les informations actuelles:\n")
                print("Nom du centre:", centre[0])
                print("Capacité du centre:", centre[1])
                print()

                # Demande à l'utilisateur quelles sont les informations qu'il souhaite mettre à jour
                print("Quelle information souhaitez-vous mettre à jour ?")
                print("1) Capacité du modèle")
                choix = input("Votre choix (1): ")

                if choix == "1":
                    while True:
                        nouveau_cap = input("Veuillez saisir le nouveau capacité du centre: ")
                        # On controle si cap_centre est un entier
                        if nouveau_cap.isdigit():
                            break
                        else:
                            print("Erreur: Le capacité de centre doit être un entier .")
                            abandonner_prompt(menu_inserer, connexion)
                    cur.execute("UPDATE CentresOrdure SET capCentre = ? WHERE nomCentre = ?", (nouveau_cap, nom_centre))
                    print("Capacité du centre mis à jour avec succès.")
                    break

                else:
                    print("Choix invalide.")
                    abandonner_prompt(menu_mettre_jour, connexion)
            else:
                print(
                    "Erreur: Ce nom du centre n'existe pas dans la liste des centres disponibles. Veuillez choisir un nom valide.")
                abandonner_prompt(menu_mettre_jour, connexion)

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    user_reponse = input("Voulez-vous mettre à jour un autre centre (o/toute autre touche pour dire non): ").lower()
    print("")
    if user_reponse == "o":
        mettre_jour_centre(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre operation (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            # Reappel de fonction menu_mettre_jour
            menu_mettre_jour(connexion)
        else:
            quit()


def mettre_jour_programmation(connexion):
    print("6.Mettre à jour une programmation\n")

    # Fonction pour afficher liste des programmations
    def afficher_liste_programmation(connexion):
        cur = connexion.cursor()
        try:
            cur.execute("SELECT * FROM Programmations")
            rows = cur.fetchall()
            # Créer des titres de colonnes
            headers = ["codeQuartier", "plaqueCamion", "heureProg"]

            # Formatage correct des données du tableau
            table_data = [headers] + rows

            # Imprimer le tableau à l'aide de tabulate
            print("Liste des programmations:")
            print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))


        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    cur = connexion.cursor()
    while True:
        try:
            afficher_liste_programmation(connexion)
            print()
            code_quartier = input("Veuillez saisir le code du quartier à mettre à jour: ")
            plaque_camion = input("Veuillez saisir la plaque du camion à mettre à jour: ")
            print()

            # Vérifie si le code_quartier et plaque_camion existent dans la table des programmations
            cur.execute("SELECT * FROM Programmations WHERE codeQuartier = ? AND plaqueCamion = ?",
                        (code_quartier, plaque_camion))
            programmation = cur.fetchone()

            if programmation:
                print("Programmation trouvée. Voici les informations actuelles:\n")
                print("Code du quartier:", programmation[0])
                print("Plaque du camion:", programmation[1])
                print("Heure:", programmation[2])
                print()

                # Demande à l'utilisateur quelles sont les informations qu'il souhaite mettre à jour
                print("Quelles informations souhaitez-vous mettre à jour ?")
                print("1) Heure")
                choix = input("Votre choix (1): ")


                if choix == "1":
                    nouvelle_heure = input("Veuillez saisir la nouvelle heure (HH:MM): ")
                    # Créer un motif regex pour le contrôle (TRIGGER)
                    heure_pattern = re.compile(r'^(0[5-9]|1[0-8]):[0-5][0-9]$')
                    # Vérifier s'il correspond au modèle de heure saisi
                    if heure_pattern.match(nouvelle_heure):
                        cur.execute(
                            "UPDATE Programmations SET heureProg = ? WHERE codeQuartier = ? AND plaqueCamion = ?",
                            (nouvelle_heure, code_quartier, plaque_camion))
                        print("Heure mise à jour avec succès.")
                        break

                    print("Erreur: Le format de l'heure doit être HH:MM et entre 05:00 et 18:59.")
                    abandonner_prompt(menu_inserer, connexion)

                else:
                    print("Choix invalide.")
                    abandonner_prompt(menu_mettre_jour, connexion)
            else:
                print("Erreur: Cette programmation n'existe pas. Veuillez saisir des informations valides.")
                abandonner_prompt(menu_mettre_jour, connexion)

        except sqlite3.Error as e:
            print("Erreur SQLite:", e)

    user_reponse = input(
        "Voulez-vous mettre à jour une autre programmation (o/toute autre touche pour dire non): ").lower()
    print("")
    if user_reponse == "o":
        mettre_jour_programmation(connexion)
    else:
        user_reponse = input("Voulez-vous faire une autre opération (o/toute autre touche pour dire non): ").lower()
        print("")
        if user_reponse == "o":
            # Reappel de fonction menu_mettre_jour
            menu_mettre_jour(connexion)
        else:
            quit()


# Une fonction pour poser à l'utilisateur s'il veut continuer ou abandonner et retoruner au menu précédent
def abandonner_prompt(menu_a_returner, connexion):
    while True:
        user_input = input("Voulez-vous abandonner (o/toute autre touche pour dire non): ").lower()
        if user_input == "o":
            menu_a_returner(connexion)
        else:
            return


def mise_a_jour_bd_trigger_2(conn: sqlite3.Connection, file: str):
    """Exécute sur la base de données toutes les commandes contenues dans le
    fichier fourni en argument.

    Les commandes dans le fichier `file` doivent être séparées par un
    point-virgule.

    :param conn: Connexion à la base de données
    :type conn: sqlite3.Connection
    :param file: Chemin d'accès au fichier contenant les requêtes
    :type file: str
    """

    # Lecture du fichier et placement des requêtes dans un tableau
    sqlQueries = []

    with open(file, 'r') as f:
        createSql = f.read()
        sqlQueries = createSql.split("/")

    # Exécution de toutes les requêtes du tableau
    cursor = conn.cursor()
    for query in sqlQueries:
        cursor.execute(query)
    # Validation des modifications
    conn.commit()




import sqlite3

def mise_a_jour_bd_trigger(conn: sqlite3.Connection, file: str):
    """Exécute sur la base de données toutes les commandes contenues dans le
    fichier fourni en argument, en prenant en compte les triggers.

    Les commandes dans le fichier `file` doivent être séparées par un
    caractère différent de ';', ici '/' est utilisé comme séparateur pour
    les triggers.

    :param conn: Connexion à la base de données
    :type conn: sqlite3.Connection
    :param file: Chemin d'accès au fichier contenant les requêtes
    :type file: str
    """

    # Lecture du fichier et placement des requêtes dans un tableau
    sqlQueries = []

    with open(file, 'r') as f:
        createSql = f.read()
        sqlQueries = createSql.split("/")

    # Exécution de toutes les requêtes du tableau
    cursor = conn.cursor()

    for query in sqlQueries:
        cursor.execute(query)

    # Validation des modifications
    conn.commit()

########################Une fonction manuel pour le trigger ##################
#On controlle si le qua_dech_camion <= cap_dep_maxModele avec une insert
def check_capacity_and_insert(conn, code_quartier, plaque_camion):
    cur = conn.cursor()

    # Obtenir la quantité de dechet du camion
    cur.execute("SELECT qua_dechCamion FROM CamionsOrdure WHERE plaqueCamion = ?", (plaque_camion,))
    qua_dech_camion = cur.fetchone()[0]
    if qua_dech_camion is None:
        qua_dech_camion = 0
    # Obtenir la quantité totale de déchets dans le quartier
    cur.execute("SELECT nb_poubQuartier FROM Quartiers WHERE codeQuartier = ?", (code_quartier,))
    dech_quartier = cur.fetchone()[0]


    # Obtenir le capacité maximale du modèle
    cur.execute("SELECT cap_dep_maxModele FROM Modeles JOIN CamionsOrdure USING(nomModele) WHERE plaqueCamion = ?", (plaque_camion,))
    cap_max_modele = cur.fetchone()[0]

    # Si la capacité du camion est inférieure à la quantité totale de déchets dans le camion(apres insértion), afficher un message d'erreur et ne pas effectuer l'opération.
    if cap_max_modele < qua_dech_camion + dech_quartier:
        print("Erreur : La quantité de déchet du camion a été dépassée. Veuillez sélectionner un autre camion")
        return False

    return True

#On controlle si le qua_dech_camion <= cap_dep_maxModele avec une mettre_jour
def check_capacity_and_mettre_jour(conn, nom_modele,nouveau_cap_dep):
    cur = conn.cursor()

    # Obtenir la quantité de dechet du camion
    cur.execute("SELECT qua_dechCamion FROM CamionsOrdure JOIN Modeles USING(nomModele) WHERE nomModele = ?", (nom_modele,))
    qua_dech_camion = cur.fetchone()[0]
    if qua_dech_camion is None:
        qua_dech_camion = 0

    # Si la capacité du camion(apres mettre à jour) est inférieur à la quantité totale de déchets, afficher un message d'erreur et ne pas effectuer l'opération.
    if int(nouveau_cap_dep) < qua_dech_camion:
        print("Erreur : Capacité nouvelle du camion inférieur à la quantité de déchet du camion. Veuillez sélectionner un autre capacité")
        return False

    return True

########################Fonction Main############################
def main():
    # Nom de la BD à créer
    db_file = "data/ramassage_poubelles.db"

    # Créer une connexion a la BD
    connexion = db.creer_connexion(db_file)

    # Remplir la BD
    db.mise_a_jour_bd(connexion, "data/suppressions_table.sql")
    db.mise_a_jour_bd(connexion, "data/creation_tables.sql")
    db.mise_a_jour_bd(connexion, "data/inserts_correct.sql")
    db.mise_a_jour_bd(connexion, "data/view.sql")
    # On a implementé manuelement les triggers en python
    # mise_a_jour_bd_trigger(connexion, "data/triggers.sql")

    # Appel du fonction pour le menu principal
    menu_principal(connexion)


if __name__ == "__main__":
    main()
