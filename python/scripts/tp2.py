# @Name Min / Max des input utilisateur

def tp2() :
    a, b, c = input("Entrer 3 valeurs entières séparée par un espace\n").split()
    a=int(a)
    b=int(b)
    c=int(c)

    print(f"La valeur minimale entre {a}, {b} et {c} est {min(a,b,c)}")
    print(f"La valeur maximale entre {a}, {b} et {c} est {max(a,b,c)}")