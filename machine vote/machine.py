import bdd
import os

class MachineVote:
    def __init__(self) -> None:
        self.candidats = bdd.Candidats()
    
    def voter(self, numéro: str):
        candidats = self.candidats.get_candidats_name()
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




class Ecran:
    def __init__(self) -> None:
        self.machine = MachineVote()
    

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

    def ecran_vote(self):
        os.system("clear")
        print("Voici la liste des candidats :")
        self.afficher_choix()
        choix = input("Pour qui voulez-vous voter ?\n> ").strip()
        self.handle_choice(choix)
    
    def handle_choice(self, choice):
        if choice == "m":
            self.ecran_admin()
        
        if choice in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.machine.voter(choice)
        else:
            self.ecran_vote()

    def afficher_resultat(self):
        candidats = self.machine.candidats.get_candidats()
        for candidat in candidats:
            print(candidat)


    def ecran_admin(self):
        pass


    def main(self):
        self.ecran_vote()



if __name__ == "__main__":
    import sys

    ecran = Ecran()
    ecran.ecran_vote()
    ecran.afficher_resultat()