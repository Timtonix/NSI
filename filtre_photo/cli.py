from InquirerPy import prompt, inquirer
import api


questions = [
    {
        "name": "filtre",
        "type": "list",
        "message": "Choisissez un filtre à appliquer",
        "choices": ["Rouge", "Vert", "Bleu", "Gris", "Noir et Blanc", "Miroir", "Pixel", "Lumiere"]

    }]

filtre = api.Filtre()
couleur = prompt(questions)["filtre"]
if couleur == "Gris":
    filtre.filtre_gris()
if couleur == "Noir et Blanc":
    filtre.filtre_noir_blanc()
if couleur == "Miroir":
    filtre.filtre_miroir()
if couleur == "Pixel":
    pixel = inquirer.number("De combien voulez-vous pixeliser l'image ?").execute()
    filtre.pixeln(int(pixel))
else:
    filtre.filtre_couleur(couleur)
