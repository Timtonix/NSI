from InquirerPy import prompt, inquirer
from InquirerPy.validator import PathValidator
import api
from colorama import Fore
import wget

print(Fore.BLUE + r"""
 _________  ___  _____ ______   _________  ________          ________ ___  ___   _________  ________  _______      
|\___   ___\\  \|\   _ \  _   \|\___   ___\\   __  \        |\  _____\\  \|\  \ |\___   ___\\   __  \|\  ___ \     
\|___ \  \_\ \  \ \  \\\__\ \  \|___ \  \_\ \  \|\  \       \ \  \__/\ \  \ \  \\|___ \  \_\ \  \|\  \ \   __/|    
     \ \  \ \ \  \ \  \\|__| \  \   \ \  \ \ \  \\\  \       \ \   __\\ \  \ \  \    \ \  \ \ \   _  _\ \  \_|/__  
      \ \  \ \ \  \ \  \    \ \  \   \ \  \ \ \  \\\  \       \ \  \_| \ \  \ \  \____\ \  \ \ \  \\  \\ \  \_|\ \ 
       \ \__\ \ \__\ \__\    \ \__\   \ \__\ \ \_______\       \ \__\   \ \__\ \_______\ \__\ \ \__\\ _\\ \_______\
        \|__|  \|__|\|__|     \|__|    \|__|  \|_______|        \|__|    \|__|\|_______|\|__|  \|__|\|__|\|_______|                                                                                                     
""")
method = inquirer.select("Image locale ou sur le web ?", ["Locale", "Web"]).execute()
src_path = ""

# On demande si on veut une image locale ou distante
if method == "Locale":
        src_path = inquirer.filepath(
            message="Quelle image voulez-vous modifier :",
            default="",
            validate=PathValidator(is_file=True, message="Input is not a file"),
            only_files=True,
        ).execute()
else:
    lien = inquirer.text("Quel est le lien de l'image : ").execute()
    src_path = wget.download(lien)
    print(src_path)


# Demande l'image à modifier

questions = [
    {
        "name": "filtre",
        "type": "list",
        "message": "Choisissez un filtre à appliquer",
        "choices": ["Rouge", "Vert", "Bleu", "Gris", "Noir et Blanc", "Miroir", "Pixel", "Lumiere", "Coloriser"]

    }]

filtre = api.Filtre(src_path)
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

filtre.copie.close()
filtre.blank.close()