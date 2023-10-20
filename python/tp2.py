a, b, c = input("Entrer les 3 valeurs séparée par un espace\n").split()
a=int(a)
b=int(b)
c=int(c)

min = min(a,b,c)
max = max(a,b,c)

print(f"La valeur minimale entre {a}, {b} et {c} est {min}")
print(f"La valeur maximale entre {a}, {b} et {c} est {max}")