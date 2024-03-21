import time
import security
import bdd
import os

class MachineVote:
    def __init__(self) -> None:
        self.candidats = bdd.Candidats()
        self.security = security.Security(len(self.candidats.get_candidats_name()), 2, "Banane")
    
    def voter(self, numéro: str):
        candidats = self.candidats.get_candidats_name()
        numéro = self.security.analyse(int(numéro))
        print(numéro)
        time.sleep(1)
        for candidat in enumerate(candidats):
            # J'aurais pu mettre en int mais je mets en str() le numéro du candidat
            if numéro == str(candidat[0]):
                self.candidats.voter(candidat[1])


    def ajouter_candidat(self, nom):
        print(self.candidats.candidat_exist(nom=nom))
        if self.candidats.candidat_exist(nom=nom):
            raise ValueError("Le candidat existe déjà")
        else:
            self.candidats.add_candidat(nom=nom)

    def ajouter_candidats(self, noms: list):
        for nom in noms:
            if self.candidats.candidat_exist(nom=nom):
                raise ValueError("Le candidat existe déjà")
            else:
                self.candidats.add_candidat(nom=nom)

    def reset_machine(self):
        self.candidats.clear_table()

    def resultats(self):
        return self.candidats.get_candidats()



class Ecran:
    def __init__(self) -> None:
        self.machine = MachineVote()
        self.main()
    

    def afficher_choix(self):
        candidats = self.machine.candidats.get_candidats_name()
        print("-"*30)
        for candidat in enumerate(candidats):
            print(f"| [ {candidat[0]} ]  > {candidat[1]}")
        print("-"*30)

    

    def ajouter_candidat(self):
        os.system("clear")
        print("Quel est le nom du candidat que vous souhaitez ajouter ?")
        nom = input("Nom : ").strip()
        self.machine.ajouter_candidat(nom=nom)
        print("Le candidat a été ajouté")
        time.sleep(2)
        self.ecran_admin()

    def ecran_vote(self):
        os.system("clear")
        print("Voici la liste des candidats :")
        self.afficher_choix()
        choix = input("Pour qui voulez-vous voter ?\n> ").strip()
        self.handle_choice(choix)
        self.ecran_vote()
    
    def handle_choice(self, choice):
        if choice == "m":
            self.ecran_admin()
        elif choice in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.machine.voter(choice)
        else:
            self.ecran_vote()

    def afficher_resultat(self):
        candidats = self.machine.candidats.get_candidats()
        for candidat in candidats:
            print(candidat)
        time.sleep(10)


    def ecran_admin(self):
        os.system("clear")
        print(""">Que voulez vous faire ?
              |> 1. Ajouter candidat
              |> 2. Voir les résultats
              |> 3. Réinitialiser
              |> 4. Mode vote
              |> 5. Quitter""")
        self.admin_choice(input("Mon choix >").strip())

    def admin_choice(self, choice):
        if choice == "1":
            self.ajouter_candidat()
        elif choice == "2":
            self.afficher_resultat()
        elif choice == "3":
            self.machine.reset_machine()
            print("Tout a été réinitialisé.")
            time.sleep(2)
            self.ecran_admin()
        elif choice == "4":
            self.ecran_vote()
        elif choice == "5":
            exit()
        else:
            self.ecran_admin()

    def main(self):
        self.ecran_vote()


if __name__ == "__main__":
    ecran = Ecran()