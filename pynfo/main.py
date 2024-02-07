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
    bitrate = audio.info.bitrate
    bitrate = bitrate//1000
    # Le sampling rate (fréquence d'échantillonnage) en Hz
    sampling = audio.info.sample_rate
    # Le bitrate mode (on ne l'utilisera pas ici)
    bit_rate_type = str(audio.info.bitrate_mode)[-3:]
    # Le ripper (extracteur) utilisé
    ripper = audio.info.encoder_info
    # Le mode (0 : Stereo ; 1 : Joint stereo ; 2 : Dual channel ; 3 : Mono)
    mode = audio.info.mode
    if mode == 0: mode = "Stereo"
    if mode == 1: mode = "Joint stereo"
    if mode == 2: mode = "Dual channel"
    if mode == 3: mode = "Mono"

    return {"album": {"artiste": artiste, "album": album, "genre": genre, "year": year, "ripper": ripper, "format": "mp3", "quality": bitrate, "channels": channels, "sampling": sampling, "mode": mode}, "track": {"numero": numero, "titre":titre, "longueur": longueur  }}
        
def centre_text(text):
    espace = 70-len(text)
    return " "*10 + text

def create_nfofile(title):
    try:
        open(title+".nfo", "x")
    except FileExistsError:
        print("Le fichier NFO existe déjà")
    return f"./{title}.nfo"

def album_div(artiste, album, template):
        print(type(template))
        template.append(tirets(template))
        template.append(centre_text(artiste + " - " + album))
        template.append(tirets(template))
        template.append("")
        return template

def album_info_div(info, template):
        template.append("Artist..............: " + info["album"]["artiste"])
        template.append("Album...............: " + info["album"]["album"])
        template.append("Genre...............: " + info["album"]["genre"])
        template.append(f"Year................: {info['album']['year']}")
        template.append("Ripper..............: " + info["album"]["ripper"])
        template.append("Format..............: " + info["album"]["format"])
        template.append(f"Quality.............: {info['album']['quality']} kps")
        template.append(f"Channels............: {info['album']['channels']}")
        template.append(f"Sampling rate.......: {info['album']['sampling']} Hz")
        template.append("Mode................: " + info["album"]["mode"])
        return template


def track_div(template):
    template.append(tirets)
    template.append(centre_text("Tracklisting"))
    template.append(tirets)
    template.append("")
    return template

def track_info(info, template):
    espace = 70 - len(f"{info['track']['numero']}. {info['album']['artiste']} - {info['track']['titre']}") - 7
    template.append(f"{info['track']['numero']}. {info['album']['artiste']} - {info['track']['titre']}{' '*espace}[{info['track']['longueur']}]")
    return template

def tirets(template):
    return "----------------------------------------------------------------------"


def read_nfo():
    with open("Dookie.nfo", "r") as f:
        print(f.read())

def nfo_file():
    mp3s = get_mp3_in_directory()
    actual_album = None
    template = []

    for mp3 in mp3s:
        info = get_info_for_one_mp3(mp3)
        if actual_album != info["album"]:
            actual_album = info["album"]
            nfo = create_nfofile(info["album"]["album"])
            album_div(info["album"]["artiste"], info["album"]["album"], template)
            album_info_div(info, template)
        print(template)
        
        track_info(info, template)
    print(template)


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


