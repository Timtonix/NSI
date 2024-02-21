import bdd
import os

class MachineVote:
    def __init__(self) -> None:
        self.candidats = bdd.Candidats()
    
    def voter(self, nom):
        pass
    
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
        print(candidats)
        for candidat in candidats:
            print(candidat)
    

    def ajouter_candidat(self):
        os.system("clear")
        print("Quel est le nom du candidat que vous souhaitez ajouter ?")
        nom = input("Nom : ").strip()
        self.machine.ajouter_candidat(nom=nom)
        print("Le candidat a été ajouté")

if __name__ == "__main__":
    ecran = Ecran()
    ecran.ajouter_candidat()
    ecran.afficher_choix()