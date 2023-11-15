from InquirerPy import prompt, inquirer
import api


questions = [
    {
        "name": "filtre",
        "type": "list",
        "message": "Choisissez un filtre à appliquer",
        "choices": ["Rouge", "Vert", "Bleu", "Gris", "Noir et Blanc"]

    }]

filtre = api.Filtre()
couleur = prompt(questions)["filtre"]
if couleur == "Gris":
    filtre.filtre_gris()
if couleur == "Noir et Blanc":
    filtre.filtre_noir_blanc()
else:
    filtre.filtre_couleur()
