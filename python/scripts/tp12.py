# @Name Notes élève + gestion erreurs

def tp12():
    notes = []
    while True:
        choix = input("1.ajouter\n2.afficher\n2.moyenne\nq.quitter")
        match choix:
            case "1":
                note = input("note à ajouter ?")
                try :
                    note = int(note)
                except ValueError :
                    print("erreur")
            case "2":
            case "3":
            case "q":
                break