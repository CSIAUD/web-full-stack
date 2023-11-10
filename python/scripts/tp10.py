# @Name Création de plusieures entreprises et affichage

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

def tp10() :
    nbCompanies = int(input("Combien d'entreprises voulez-vous créer ? "))
    cls()
    companies = [] 

    while len(companies) < nbCompanies:
        ok = False
        id = len(companies) + 1
        while not ok :
            print(f"Création de l'entreprise N°{id}")
            name = input("Nom de l'entreprise ? ")
            cls()

            nb = "a"
            while not nb.isnumeric():
                print(f"Création de l'entreprise N°{id}")
                nb = input("Nombre d'employés ? ")
                cls()

            ca = "a"
            while not ca.isnumeric():
                print(f"Création de l'entreprise N°{id}")
                ca = input("Chiffre d'affaire ? ")
                cls()

            print(f"Création de l'entreprise N°{id}")
            response = input(f"Les valeurs sont correctes ? (O/N) \nNom de l'entreprise => {name}\nNombre d'employés => {nb}\nChiffre d'affaire => {ca}\n")
            cls()
            if(response.lower() != "n"):
                ok = True

        company = Company(name, nb, ca)
        companies.append(company)
    cls()
    for company in companies:
        company.display()