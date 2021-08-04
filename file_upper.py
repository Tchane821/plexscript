import os
from os.path import isdir
import glob

#saisie
racine = input("Entrez le chemin de la racine des fichies a remonter\n")
if not isdir(racine):
    print("Erreur dans la saisie du dossier racine\n")
    exit(1)

ndr = input("Entrez le nom du dossier de destination\n") # Nom de Dossier de Reception
if not isdir(ndr):
    os.mkdir(ndr)

#extraction
path_to_file_list = glob.glob(racine + '*mp4 | *mkv | *avi' )

for path_to_file in path_to_file_list:
    print(path_to_file)