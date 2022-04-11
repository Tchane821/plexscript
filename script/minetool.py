import os
import shutil
import sys

# 3 actions : MAKE START STOP

if len(sys.argv) < 2:
    print("Log: Error: bad argument")
    exit(1)

action = sys.argv[1]
if action.lower() not in ["make", "start", "stop"]:
    print("Log: Error: bad action")
    exit(2)

if "-h" in sys.argv:
    print("help !")

# make
if action == "make":
    if len(sys.argv) != 5:
        print("Log: not enought argument to launch")
        f_name = input("Nom du dossier/du serveur\n\t ->")
        f_ressource = input("Chemin du dossier ressource\n\t ->")
        name_version = input("Version de minecraft\n\t ->")
    else:
        f_name = sys.argv[2]
        f_ressource = sys.argv[3]
        name_version = sys.argv[4]

    try:
        os.mkdir(f_name)
    except OSError:
        print("Log: Error: Can't create the minecraft serveur directorie")
        exit(4)

    fjar_version = f"{f_ressource}/{name_version}.jar"
    feula = f"{f_ressource}/eula.txt"
    try:
        shutil.copy(fjar_version, f"./{f_name}")
        shutil.copy(fjar_version, f"./{f_name}")
    except OSError:
        print("Log: Error: Can't move serveur jarfile and/or eula in destination")
        exit(5)

elif action == "start":
    pass

elif action == "stop":
    pass


print("Log: action done")
exit(0)

