from random import randint
from machine import MachineVote
def test_1000_vote():
    machine = MachineVote()
    machine.reset_machine()
    machine.ajouter_candidats(["Samuel", "Timothe", "Max", "Jean", "Robin", "Alexandre"])
    for i in range(1000):
        machine.voter(str(randint(0, 5)))
    resultats = machine.resultats()
    assert resultats[0][1] > 1
