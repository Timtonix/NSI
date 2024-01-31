from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from os import walk


def get_mp3_in_directory():
    files = []
    for (dirpath, dirnames, filenames) in walk("."):
        for file in filenames:
            if file[-3:] == "mp3":
                files.append(dirpath+"/"+file)

    print(files)
    return files
    
def get_nfo_in_directory():
    files = []
    for (dirpath, dirnames, filenames) in walk("."):
        for file in filenames:
            if file[-3:] == "nfo":
                files.append(dirpath+"/"+file)

    print(files)
    return files

def get_info_for_one_mp3(filename):
    info = ID3(filename)
    # Numero de la pistes
    numero = info["TRCK"].text[0]
    # Titre de la piste
    titre = info["TIT2"].text[0]
    # Nom de l'artiste ou du goupe
    artiste = info['TPE1'].text[0]
    # Nom de l'album
    album = info["TALB"].text[0]
    # Genre de l'album
    genre = info["TCON"].text[0]
    # Année de sortie
    year = info["TDRC"].text[0]


    audio = MP3(filename)
    # Longugeur en secondes de la piste
    longueur = audio.info.length
    # Le nombre de channels audio
    channels = audio.info.channels
    # Le débit (bitrate) en bits par seconde
    audio.info.bitrate
    # Le sampling rate (fréquence d'échantillonnage) en Hz
    audio.info.sample_rate
    # Le bitrate mode (on ne l'utilisera pas ici)
    bit_rate_type = str(audio.info.bitrate_mode)[-3:]
    # Le ripper (extracteur) utilisé
    ripper = audio.info.encoder_info
    # Le mode (0 : Stereo ; 1 : Joint stereo ; 2 : Dual channel ; 3 : Mono)
    mode = audio.info.mode

    return {"album": {"artiste": artiste, "album": album, "genre": genre, "year": year}, "track": {"numero": numero, "titre":titre}}


def centre_text(text):
    espace = 70-len(text)
    return " "*10 + text

def create_nfofile(title):
    try:
        open(title+".nfo", "x")
    except FileExistsError:
        print("Le fichier NFO existe déjà")
    return f"./{title}.nfo"


def album_div(artiste, album, nfofile):
    with open(nfofile, "w") as f:
        f.write(centre_text(artiste + " - " + album))
        

def read_nfo():
    with open("Dookie.nfo", "r") as f:
        print(f.read())

def nfo_file():
    mp3s = get_mp3_in_directory()
    actual_album = None
    for mp3 in mp3s:
        info = get_info_for_one_mp3(mp3)
        actual_album = info["album"]
        nfo = create_nfofile(info["album"]["album"])
        album_div(info["album"]["artiste"], info["album"]["album"], nfo)

nfo_file()
"""
Notes : 
- Prend tous les fichiers mp3 dans un directory
- Retourne un .nfo avec autant d'album que l'on a.

Infos Album :
- Artist
- Album
- Genre
- Year
- Ripper
- Format
- Quality
- Channels
- Sampling Rate
- Mode
- Cover

"""


