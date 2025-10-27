##########################################
# Lévesque, Jacob, <6307344>
##########################################
#Queston 1

import random


def generer_temperatures():
    """
    Génère aléatoirement 10 températures entre 20°C et 35°C,
    affiche chaque température avec le jour correspondant
    et un message selon la situation.
    """

    # Génération de 10 températures aléatoires entre 20.0 et 35.0
    temperatures = [round(random.uniform(20, 35), 1) for _ in range(10)]

    # Boucle sur chaque température avec son numéro de jour
    for i, temp in enumerate(temperatures, start=1):
        print(f"Jour {i} : {temp}°C", end=" → ")

        # Vérification des conditions
        if temp < 24:
            print("Trop froid")
        elif temp > 30:
            print("Trop chaud")
        else:
            print("OK")

    # Message de fin
    print("Fin")


# Appel de la fonction
generer_temperatures()




#Question 2

import math
import matplotlib.pyplot as plt


def croissance_bacterienne():
    """
    Demande la population initiale, calcule la croissance bactérienne
    et affiche un graphique de l'évolution au fil des heures.
    """

    # Demande à l'utilisateur la population initiale
    population_initiale = float(input("Entrez la population initiale de bactéries : "))

    # Constante de taux de croissance
    taux = math.pi / 5  # augmentation par heure

    # Liste des heures (par exemple sur 10 heures)
    heures = list(range(0, 11))

    # Calcul de la population à chaque heure : P(t) = P0 * e^(r*t)
    populations = [population_initiale * math.exp(taux * t) for t in heures]

    # Tracé du graphique
    plt.figure(figsize=(8, 5))
    plt.plot(heures, populations, 'b*', label='Population observée')  # marqueurs bleus en forme d'étoiles
    plt.plot(heures, populations, 'b--', alpha=0.5)  # ligne bleue pointillée pour lisibilité
    plt.axhline(y=50000, color='r', linestyle='--', label='Seuil = 50000')  # ligne rouge horizontale

    # Ajout du titre et des labels
    plt.title("Croissance bactérienne")
    plt.xlabel("Heures")
    plt.ylabel("Population")
    plt.grid(True)
    plt.legend()

    # Affichage du graphique
    plt.show()


# Appel de la fonction
croissance_bacterienne()




