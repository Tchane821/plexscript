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


def goodend():
    print("Log : Job Done")
    exit(0)


def badend(i):
    print("Log: Bad ending")
    exit(i)


# 4 actions : MAKE START REMOVE

if len(sys.argv) < 2:
    print("Log: Error: bad argument")
    badend(1)

for a in sys.argv:
    if a.lower() in help_flags:
        print(HELP)
        goodend()

action = sys.argv[1]
if action.lower() not in ["make", "start", "remove"]:
    print("Log: Error: bad action")
    badend(2)

if not os.path.isdir(f_source):
    print("Source file not found !")
    badend(3)

# --- Make -------------------------------------------------------------------------------------------------------------
if action == "make":
    if len(sys.argv) != 4:
        print("Log: not enought argument to launch")
        f_name_m = input("Nom du dossier du serveur\n\t ->")
        name_version = input("Version de minecraft\n\t ->")
    else:
        f_name_m = sys.argv[2]
        name_version = sys.argv[3]

    # make serveur directory
    try:
        os.mkdir(f_name_m)
    except OSError:
        print("Log: Error: Can't create the minecraft serveur directorie")
        badend(11)

    # copy file you need
    fjar_version = f"{f_source}/{name_version}.jar"
    feula = f"{f_source}/eula.txt"
    try:
        shutil.copy(fjar_version, f"./{f_name_m}")
        shutil.copy(feula, f"./{f_name_m}")
    except OSError:
        print("Log: Error: Can't move serveur jarfile and/or eula in destination")
        badend(12)


# --- Start ------------------------------------------------------------------------------------------------------------
elif action == "start":
    f_name_s = None
    f_jar = None
    ram_min = RAMMIN
    ram_max = RAMMAX
    gui = GUI

    # argument take
    if len(sys.argv) < 3:
        print("Log: not enought argument to launch")
        f_name_s = input("Nom du dossier/du serveur a lancer\n\t ->")
        print(f"Log: Default value for MinRam = {RAMMIN}, MaxRan = {RAMMAX}, gui = {GUI}")
    else:
        f_name_s = sys.argv[2]
        if len(sys.argv) == 6:
            ram_min = sys.argv[3]
            ram_max = sys.argv[4]
            gui = sys.argv[5]
        else:
            print("Log: Error: Not correct numbers of arguments")
            badend(21)

    # argument check
    if not ram_min.isdigit() or not ram_max.isdigit():
        print("Log: Error: RAMMIN or/and RAMMAX are not a number")
        badend(22)
    if gui.upper() in ["T", "TRUE"]:
        gui = True
    elif gui.upper() in ["F", "FALSE"]:
        gui = False
    else:
        print("Log: Error: GUI value are not [true, false, t, f] or upper equivalence")
        badend(23)

    # search jar to launch
    try:
        j_files = glob.glob(f"./{f_name_s}/*.jar")
        if len(j_files) != 1:
            print("Select your jar:\n")
            cpt = 0
            for p in j_files:
                print(f"{cpt} - {p}")
                cpt += 1
            idx = input("\nPick the numbers of jar file:\n\t ->")
            if not idx.isdigit():
                print("Log: Error: it's not a number")
                badend(24)
            f_jar = j_files[int(idx)]
        elif len(j_files) == 1:
            f_jar = j_files[0]
        else:
            print("Log: Error: no jar file found")
            badend(25)
    except OSError:
        print("Log: Error: wrong directory name")
        badend(26)

    # find java commande
    f_ouestjava = f"{f_source}/ouestjava.txt"
    try:
        with open(f_ouestjava) as oej:
            java = oej.readline()[:-1]
    except OSError:
        print(f"Log: Error: file {f_ouestjava} not found")
        badend(27)

    # launch commande
    os.chdir(f"./{f_name_s}")
    commande = f"{java} -Xmx{ram_max}M -Xms{ram_min}M -jar {os.path.basename(f_jar)} -nogui"
    if gui:
        commande = f"{java} -Xmx{ram_max}M -Xms{ram_min}M -jar {os.path.basename(f_jar)}"
    print(f"Log: launch commande : {commande}")
    os.system(commande)
    goodend()


# --- Remove -----------------------------------------------------------------------------------------------------------
elif action == "remove":
    if len(sys.argv) != 3:
        print("Log: not enought argument to launch")
        f_name_r = input("Nom du dossier/du serveur\n\t ->")
    else:
        f_name_r = sys.argv[2]
    try:
        r1 = input(f"Are you sure to del {f_name_r} (Yes/No) ??? \n\t ->")
        if r1.lower() in ["y", "yes"]:
            r2 = input(f"Realy sure !? (Yes/No)\n\t ->")
            if r2.lower() in ["y", "yes"]:
                shutil.rmtree(f_name_r)
        goodend()
    except OSError:
        print("Log: Error: Can't remove some files")
        badend(31)
