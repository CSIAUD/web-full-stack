# @Name Idem 6 + cacul Min / Max / température moyenne

def moyenne(tab) :
    return sum(tab)/len(tab)

def liste(tab) :
    dictTemp = {}
    for temp in tab :
        if temp in dictTemp.keys() :
            dictTemp[temp] = dictTemp[temp] + 1
        else :
            dictTemp[temp] = 1

    keys = sorted(dictTemp.keys())
    for key in keys :
        print(f"{key}°C")


def tp8() :
    tabTemp = []
    temp = ""

    while True :
        while True :
            temp = input("Merci de rentrer les températures une par une (q pour quitter)\n").lower()

            if temp == "q" or temp == "" :
                break

            try :
                tabTemp.append(int(temp))
            except :
                print("Une erreur est survenue")

            if len(tabTemp) >= 31 :
                break
        
        choix = "";
        while True :
            choix = input("===== MENU ==========\nmax  - Afficher la température maximale\nmin  - Afficher la température minimale\nmoy  - Afficher la température moyenne\nlist - Afficher toutes les températures par ordre croissant\nadd  - Continuer à ajouter des valeurs\nq    - Quitter le programme\n").lower()
            print("=====================\n\n")
            if choix == "max" : 
                print(f"Température Maximale atteinte : {max(tabTemp)}°C")
            elif choix == "min" : 
                print(f"Température Minimale atteinte : {min(tabTemp)}°C")
            elif choix == "moy" : 
                print(f"Température Moyenne : {round(moyenne(tabTemp), 2)}°C")
            elif choix == "add" : break
            elif choix == "list" : 
                liste(tabTemp)
            elif choix == "q" or choix == "" :
                break
            else :
                print("/!\\ Choix inconnu /!\\ ")
            
            print("\n");
            

        if choix == "q" or choix == "" :
            break

