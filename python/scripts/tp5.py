# @Name Tri des prénoms en fonction de la taille

def tp5() :
    names = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Abdelkarim', 'Sandra']
    name = ""

    while True :
        name = input("Merci de rentrer les Prénoms un par un (q pour quitter)\n").lower()

        if name == "q" or name == "" :
            break

        names.append(name)

    small_name = []
    large_name = []

    for name in names :
        if len(name) < 6 :
            small_name.append(name)
        else :
            large_name.append(name)

    print("\nLes Petits prénoms :")
    for name in small_name : 
        print(name)

    print("\nLes Grands prénoms :")
    for name in large_name : 
        print(name)