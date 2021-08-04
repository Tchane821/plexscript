import os
from os.path import isdir
#saisie
racine = input("Entrez le chemin de la racine des fichies a remonter\n")
if not isdir(racine):
    print("Erreur dans la saisie du dossier racine\n")
    exit(1)

ndr = input("Entrez le nom du dossier de destination\n") # Nom de Dossier de Reception
if not isdir(ndr):
    os.mkdir(ndr)

#extraction
def listefile(rac):
    res = []
    for pathh in os.listdir(rac) :
        if isdir(pathh) :
            for f in listefile(rac.join(pathh)):
                res.append(f)
        else :
            res.append(pathh)

print(listefile(racine))