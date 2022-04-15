import os
import sys
from os.path import isdir
import glob

racine = ""
destination = ""

if len(sys.argv) == 3:
    racine = sys.argv[1]
    destination = sys.argv[2]
    print(f"Log: Argument: root: {sys.argv[1]} destination: {sys.argv[2]}")
else:
    # saisie
    racine = input("Entrez le chemin de la racine des fichies a remonter\n\t-> ")
    destination = input("Entrez le nom du dossier de destination\n\t-> ")

if not isdir(destination):
    try:
        os.mkdir(destination)
    except FileNotFoundError:
        print("Error : The path to destination is wrong")
        exit(1)

if not isdir(racine):
    print("Error : the root argument isn't correct\n")
    exit(2)

# extraction
path_to_file_list = glob.glob(racine + "/**", recursive=True)

# Filter video only
path_to_file_video_list = []
for path_to_file in path_to_file_list:
    if ".mkv" in path_to_file or ".avi" in path_to_file or ".mp4" in path_to_file:
        path_to_file_video_list.append(path_to_file)
        print(path_to_file)

# Validation de déplacement
print(f"Log: File video Found: {len(path_to_file_video_list)}\n"
      f"Souaitez vous les déplacer vers {destination}\n"
      f"(Yes | No)\n\t -> ", end='')
rep = input()
if rep.upper() == "NO" or rep.upper() == "N":
    print("Log: end of script with no error")
    exit(0)
elif rep.upper() == "YES" or rep.upper() == "Y":
    print("Log: Launch move")
else:
    print("Error: Validation error")
    exit(3)

# Move
v = 0
for f in path_to_file_video_list:
    f_name = os.path.basename(f)
    f_res = destination + "/" + f_name
    print(f"File : {f}, move to {f_res}")
    try:
        os.rename(f, f_res)
    except FileExistsError:
        f_res = os.path.dirname(f_res) + "/" + str(v) + '-' + os.path.basename(f_res)
        print(f"File {f_res} exit, so {f_res} rename to {f_res}")
        os.rename(f, f_res)
    v += 1

# fin
print("Log: End of script with no error")
exit(0)
