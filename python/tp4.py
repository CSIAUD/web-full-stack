tab = []
str = ""

while True :
    str = input("Merci de rentrer les nombre un par un (q pour quitter)\n")

    if str == "q" or str == "Q" :
        break
    
    try :
        nb = int(str)
        if not nb in tab :
            tab.append(nb)
    except :
        print("Une erreur est survenue")

print("Voici la liste des valeurs entrées :")
for nb in tab : 
    print(nb)