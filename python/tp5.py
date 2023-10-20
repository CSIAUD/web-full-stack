names = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Abdelkarim', 'Sandra']
name = ""

while True :
    name = input("Merci de rentrer les Prénoms un par un (q pour quitter)\n")

    if name == "q" or name == "Q" :
        break

    names.append(name)

small_name = []
large_name = []

for name in names :
    if len(name) < 6 :
        small_name.append(name)
    else :
        large_name.append(name)

print("Les Petits prénoms :")
for name in small_name : 
    print(name)

print("Les Grands prénoms :")
for name in large_name : 
    print(name)