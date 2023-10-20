def choix1() :
    print("Le choix est 1")

def autreChoix(p) :
    if p == "2" or p == "3" :
        return True
    return False

nb = input("Entrez un nombre entre 1 et 3 compris :\n")

if nb == 1 :
    choix1()
else :
    if autreChoix(nb) :
        print(f"Le choix est {nb}")
    else :
        print("Le choix est en dehors de l'intervalle")