import os
#saisie
racine = input("Entrez le chemin de la racine des fichies a remonter")
if not racine.isdir() :
    print("Erreur dans la saisie du dossier racine")
    exit(1)

ndr = input("Entrez le nom du dossier de destination") # Nom de Dossier de Reception
if not ndr.isdir():
    os.mkdir(ndr)

#extraction
def listefile(rac):
    res = []
    for pathh in os.listdir(rac) :
        if pathh.isdir() :
            for f in listefile(rac.join(pathh)):
                res.append(f)
        else :
            res.append(pathh)

print(listefile(racine))