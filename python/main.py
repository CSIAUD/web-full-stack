from os import listdir
from os.path import isfile, join

fileList = [f for f in listdir("./scripts") if isfile(join("./scripts", f))]
files = {}
functions = []

while True :
    for key, fileName in enumerate(fileList) :
        if fileName[-3:] != ".py" :
            continue
        
        exec(open("./scripts/"+fileName).read())

        name = fileName[:-3]
        functions.append(name)

        file = open("./scripts/"+fileName, 'r')
        firstLine = file.readline()
        if "@Name " in firstLine :
            temp = (firstLine.split("@Name ")[1]).split("\n")[0]
            if len(temp) > 0 :
                name = temp

        files[key] = {}
        files[key]['name'] = name
        files[key]['fn'] = fileName[:-3]
        files[key]['file'] = fileName

    print("===== EXERCICES ==========\n")

    for key, file in files.items() :
        print(f"{key + 1} - {file["name"]}")

    choice = input(f"\nMerci de choisir un nombre entre 1 et {len(files)} (ou q pour quitter)\n")
    print("\n========================\n\n")

    try :
        nb = int(choice)
        if nb >=1 and nb <= len((files)) :
            locals()["tp" + choice]()
            print("\n")
        else :
            print("/!\\ Compliqué de lancer quelque chose qui n'existe pas XD /!\\ \n\n")
    except :
        if choice.lower() == "q" or choice == "" :
            break
        print("/!\\ Une erreur est survenue, merci de réessayer /!\\ \n")

print("Bye ;)")