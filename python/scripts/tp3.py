# @Name Le jeu du nombre mystere

import random

def tp3() :
    print(f"Bienvenue dans le jeu du nombre mystère")
    nbToFind = random.randint(1,100)
    nbFinded = False

    while not nbFinded :
        nb = int(input("Entrez un nombre entre 1 et 100 :\n"))
        if nb > nbToFind :
            print("C'est trop")
        elif nb < nbToFind :
            print("C'est plus")
        else :
            break

    print(f"Vous avez gagné, le nombre mystère était {nbToFind}")