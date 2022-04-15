import os
import shutil
import sys
import glob

# magic number

RAMMIN = "512"
RAMMAX = "4096"
GUI = "FALSE"
f_source = "./mcressources"
help_flags = ["-h", "h", "help"]
HELP = "----- Help to minecraft serveur tool -----\n" \
       " You can call mine-tool with 4 actions:\n" \
       " make / start / stop / remove\n" \
       "\n" \
       "Make take 2 arguments:\n" \
       " 1.> Name of your serveur name \n" \
       " 2.> version of minecarft you want\n" \
       "\n" \
       "Start take 1 or 4 arguments\n" \
       " 1.> name of your serveur\n" \
       " 2*> quantity of ram Min in Mo\n" \
       " 3*> quantity of ram Max in Mo\n" \
       " 4*> need gui True or False\n" \
       "\n" \
       "Stop Not implemented yet\n" \
       "\n" \
       "Remove take 1 argumets:\n" \
       " 1.> name of serveur\n" \
       "\n"

# 4 actions : MAKE START STOP REMOVE

if len(sys.argv) < 2:
    print("Log: Error: bad argument")
    exit(1)

for a in sys.argv:
    if a in help_flags:
        print(HELP)
        exit(0)

action = sys.argv[1]
if action.lower() not in ["make", "start", "stop", "remove"]:
    print("Log: Error: bad action")
    exit(2)

if not os.path.isdir(f_source):
    print("Source file not found !")
    exit(999)

# --- Make -------------------------------------------------------------------------------------------------------------
if action == "make":
    if len(sys.argv) != 4:
        print("Log: not enought argument to launch")
        f_name = input("Nom du dossier/du serveur\n\t ->")
        name_version = input("Version de minecraft\n\t ->")
    else:
        f_name = sys.argv[2]
        name_version = sys.argv[3]

    try:
        os.mkdir(f_name)
    except OSError:
        print("Log: Error: Can't create the minecraft serveur directorie")
        exit(4)

    fjar_version = f"{f_source}/{name_version}.jar"
    feula = f"{f_source}/eula.txt"
    try:
        shutil.copy(fjar_version, f"./{f_name}")
        shutil.copy(feula, f"./{f_name}")
    except OSError:
        print("Log: Error: Can't move serveur jarfile and/or eula in destination")
        exit(5)


# --- Start ------------------------------------------------------------------------------------------------------------
elif action == "start":
    f_name_l = ""
    ram_min = ""
    ram_max = ""
    gui = ""
    f_jar = ""

    # argument take
    if len(sys.argv) < 3:
        print("Log: not enought argument to launch")
        f_name_l = input("Nom du dossier/du serveur a lancer\n\t ->")
        print(f"Log: Default value for MinRam = {RAMMIN}, MaxRan = {RAMMAX}, gui = {GUI}")
        ram_min = RAMMIN
        ram_max = RAMMAX
        gui = GUI
    else:
        f_name_l = sys.argv[2]
        if len(sys.argv) == 6:
            ram_min = sys.argv[3]
            ram_max = sys.argv[4]
            gui = sys.argv[5]
        else:
            print("Log: Error: Not correct numbers of arguments")
            exit(9)

    # argument check
    if not ram_min.isdigit() or not ram_max.isdigit():
        print("Log: Error: RAMMIN or/and RAMMAX are not a number")
        exit(7)
    if gui.upper() in ["T", "TRUE"]:
        gui = True
    elif gui.upper() in ["F", "FALSE"]:
        gui = False
    else:
        print("Log: Error: GUI not true, false, t, f")
        exit(8)
    try:
        j_files = glob.glob(f"./{f_name_l}/*.jar")
        if len(j_files) != 1:
            print("Select your jar\n")
            cpt = 0
            for p in j_files:
                print(f"{cpt} - {p}")
                cpt += 1
            idx = input("Pick the numbers of jar file:\n\t ->")
            if not idx.isdigit():
                print("Log: Error: it's not a number")
                exit(11)
            f_jar = j_files[int(idx)]
        else:
            f_jar = j_files[0]
    except OSError:
        print("Log: Error: wrong directory name")
        exit(10)

    # find java
    f_ouestjava = f"{f_source}/ouestjava.txt"
    with open(f_ouestjava) as oej:
        java = oej.readline()

    commande = f"{java} -jar ./{f_jar} -Xmx {ram_max}Mo -Xms {ram_min}Mo -nogui"
    if gui:
        commande = f"java -jar ./{f_jar} -Xmx {ram_max}Mo -Xms {ram_min}Mo"
    print(f"Log: launch commande : {commande}")
    os.system(commande)


# --- Stop -------------------------------------------------------------------------------------------------------------
elif action == "stop":
    # TODO
    pass


# --- Remove -----------------------------------------------------------------------------------------------------------
elif action == "remove":
    if len(sys.argv) != 3:
        print("Log: not enought argument to launch")
        f_name_r = input("Nom du dossier/du serveur\n\t ->")
    else:
        f_name_r = sys.argv[2]
    try:
        shutil.rmtree(f_name_r)
    except OSError:
        print("Log: Error: Can't remove some files")
        exit(6)

print("Log: action done")
exit(0)
