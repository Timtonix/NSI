from InquirerPy import prompt, inquirer
import api


questions = [
    {
        "name": "filtre",
        "type": "list",
        "message": "Choisissez un filtre à appliquer",
        "choices": ["Rouge", "Vert", "Bleu", "Gris", "Noir et Blanc", "Miroir", "Pixel", "Lumiere", "Coloriser"]

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
if couleur == "Lumiere":
    lum = inquirer.number("De combien voulez-vous augmenter la luminosité").execute()
    filtre.filtre_lum(int(lum))
if couleur == "Coloriser":
    rgb = inquirer.rawlist("Quelle couleur voulez vous augmenter ?", ["rouge", "vert", "bleu"]).execute()
    k = inquirer.number("De combien voulez-vous augmenter la couleur ?").execute()
    filtre.inc_color(rgb, int(k))
else:
    filtre.filtre_couleur(couleur)
