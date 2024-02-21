import bdd
import os

class MachineVote:
    def __init__(self) -> None:
        self.candidats = bdd.Candidats()
    
    def voter(self, nom):
        pass
    
    def ajouter_candidat(self, nom):
        candidats = self.candidats.get_candidats_name()
        if nom in candidats:
            raise ValueError("Le candidat existe déjà")
        else:
            self.candidats.add_candidat(nom=nom)




class Ecran:
    def __init__(self) -> None:
        self.machine = MachineVote()
    

    def afficher_choix(self):
        candidats = self.machine.candidats.get_candidats_name()
        for candidat in candidats:
            print(candidat)
    

    def ajouter_candidat(self):
        os.system("clear")
        print("Quel est le nom du candidat que vous souhaitez ajouter ?")
        nom = input("Nom : ").strip()
        self.machine.ajouter_candidat(nom=nom)
        print("Le candidat a été ajouté")