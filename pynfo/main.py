from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from os import walk, path
import time


def get_mp3_in_directory():
    files = []
    cover=False
    for (dirpath, dirnames, filenames) in walk("."):
        for file in filenames:

            if file[-3:] == "mp3":
                files.append(dirpath+"/"+file)
            if file[-3:] in ["jpg", "png"]:
                cover = True
    mp3s = sort_mp3(files)
    return mp3s, cover

def sort_mp3(files: list):
    s_list = []
    n_list = []
    for mp3 in files:
        info = ID3(mp3)
        n = int(info["TRCK"].text[0])
        n_list.append(n)
    max = 0
    while n_list != []:
        for n in n_list:
            if n > max:
                max = n

        index = n_list.index(max)
        s_list.insert(0, files[index])
        n_list.pop(index)
        files.pop(index)
        max = 0
    return s_list
    


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
    if int(numero) < 10:
        numero = "0" + numero
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
    seconde = longueur
    longueur = calculate_time(longueur)
    # Le nombre de channels audio
    channels = audio.info.channels
    # Le débit (bitrate) en bits par seconde
    bitrate = audio.info.bitrate
    bitrate = bitrate//1000
    # Le sampling rate (fréquence d'échantillonnage) en Hz
    sampling = audio.info.sample_rate / 1000
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

    size = path.getsize(filename)

    return {"album": {"artiste": artiste, "album": album, "genre": genre, "year": year, "ripper": ripper, "format": "mp3", "quality": bitrate, "channels": channels, "sampling": sampling, "mode": mode}, "track": {"numero": numero, "titre":titre, "longueur": longueur , "seconde": seconde, "size": size}}
        

def calculate_time(temps):
    seconde = int(temps%60)
    minute = int(temps//60)
    if seconde < 10:
        seconde = f"0{seconde}"
    if minute > 9:
        return f"{minute}:{seconde}"
    return f"0{minute}:{seconde}"


def centre_text(text):
    espace = 70-len(text)
    espace = espace//2
    return " "*espace + text

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

def album_info_div(info, template, cover):
        """
        Récupère toutes les infos de l'album et les intègre dans la liste template
        """
        template.append("Artist..............: " + info["album"]["artiste"])
        template.append("Album...............: " + info["album"]["album"])
        template.append("Genre...............: " + info["album"]["genre"])
        template.append(f"Year................: {info['album']['year']}")
        template.append("Ripper..............: " + info["album"]["ripper"])
        template.append("Format..............: " + "MPEG Audio Layer 3 (MP3)")
        template.append(f"Quality.............: {info['album']['quality']} kps")
        template.append(f"Channels............: {info['album']['channels']}")
        template.append(f"Sampling rate.......: {info['album']['sampling']} kHz")
        template.append("Mode................: " + info["album"]["mode"])
        if cover:
            template.append("Cover...............: Front")

        template.append("")
        return template


def track_div(template):
    template.append(tirets(template=template))
    template.append(centre_text("Tracklisting"))
    template.append(tirets(template))
    template.append("")
    return template

def track_info(info, template):
    """
    Pour chaque track on met le numéro, l'artiste et le titre. Ainsi que la durée
    """
    espace = 70 - len(f"{info['track']['numero']}. {info['album']['artiste']} - {info['track']['titre']}") - 10
    template.append(f"  {info['track']['numero']}. {info['album']['artiste']} - {info['track']['titre']}{' '*espace}[{info['track']['longueur']}]")
    return template

def tirets(template):
    return "----------------------------------------------------------------------"


def last_info(template, p_time, total_size):
    template.append("")
    template.append("")
    template.append(f"Playing time........: {calculate_time(p_time)}")
    template.append(f"Total size..........: {total_size//2**20} Mb")



def read_nfo():
    with open("Dookie.nfo", "r") as f:
        print(f.read())

def nfo_file():
    mp3s, cover = get_mp3_in_directory()
    actual_album = None
    template = []
    nfo = None
    play_time = 0
    total_size = 0
    for mp3 in mp3s:
        info = get_info_for_one_mp3(mp3)
        play_time += info["track"]["seconde"]
        total_size += info["track"]["size"]
        if actual_album != info["album"]:
            actual_album = info["album"]
            nfo = create_nfofile(info["album"]["album"])
            album_div(info["album"]["artiste"], info["album"]["album"], template)
            album_info_div(info, template, cover)
            track_div(template)

        track_info(info, template)
    last_info(template, play_time, total_size)

    with open(nfo, "w") as f:
        for line in template:
            f.write(line + "\n")

s  = time.time()
nfo_file()
print(f"Terminé en {round(time.time() - s, 4)}s")

