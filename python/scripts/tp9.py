# @Name Création de la classe entreprise et création d'une entreprise

class Company:
    name = ""
    nbEmployees = 0
    ca = 0

    def __init__(self, name, nb, ca) -> None:
        self.name = name
        self.nbEmployees = int(nb)
        self.ca = int(ca)
        
    def display(self) -> None:
        print(f"L'entreprise {self.name} a {self.nbEmployees} employé{"s" if self.nbEmployees > 1 else ""} à son actif et un chiffre d'affaire de {self.ca} €")

def tp9() :
    ok = False
    while not ok :
        print("Bienvenue dans la création d'une entreprise")
        name = input("Nom de l'entreprise ? ")
        cls()

        nb = "a"
        while not nb.isnumeric():
            print("Bienvenue dans la création d'une entreprise")
            nb = input("Nombre d'employés ? ")
            cls()

        ca = "a"
        while not ca.isnumeric():
            print("Bienvenue dans la création d'une entreprise")
            ca = input("Chiffre d'affaire ? ")
            cls()

        print("Bienvenue dans la création d'une entreprise")
        response = input(f"Les valeurs sont correctes ? (O/N) \nNom de l'entreprise => {name}\nNombre d'employés => {nb}\nChiffre d'affaire => {ca}\n")
        cls()
        if(response.lower() != "n"):
            ok = True

    company = Company(name, nb, ca)
    company.display()