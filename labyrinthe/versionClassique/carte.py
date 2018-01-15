import random


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    dico={"nord":nord,"est":est,"sud":sud,"ouest":ouest,"tresor":tresor,"pion":pions}
    return dico
# True=mur
# False= pas de mur

carte=Carte(True,False,False,True,2,[1,2])
def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zero,un ou deux murs
    paramètre: c une carte
    """
    cpt=0
    res=True
    for key in ["nord","est","ouest","sud"]:
        if c[key]:
            cpt+=1
    if cpt>3:
        res=False
    return res

assert estValide(carte)==True

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    res=True # True signifie qu'il y a un mur dans la direction
    if not c["nord"]:
        res=False
    return res

assert murNord(carte)==True

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    res=True
    if not c["sud"]:
        res=False
    return res

assert murSud(carte)==False

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    res=True
    if not c["est"]:
        res=False
    return res

assert murEst(carte)==False

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    res=True
    if not c["ouest"]:
        res=False
    return res

assert murOuest(carte)==True

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["pion"]

assert getListePions(carte)==[1,2]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["pion"].append(listePions)

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c["pion"])

assert getNbPions(carte)==2

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètre: c une carte
    """
    res=False
    if pion in c["pion"]:
        res=True
    return res

assert possedePion(carte,2)==True
def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["tresor"]

assert getTresor(carte)==2

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    valeur_intermediaire=c["tresor"]
    c["tresor"]=0
    return valeur_intermediaire

assert prendreTresor(carte)==2

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    Cette fonction modifie la carte mais ne retourne rien
    """
    valeur_intermediaire=c["tresor"]
    c["tresor"]=tresor
    return valeur_intermediaire

#assert mettreTresor(carte,1)==2 # faire attention car ne fonctionne qu'une seule fois car
                            # après l'on change la valeur de tresor

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion in c["pion"]:
        c["pion"].remove(pion)
    #else rien

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c["pion"]:
        c["pion"].append(pion)
    #else rien

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    c={"nord":c["ouest"],"est":c["nord"],"sud":c["est"],"ouest":c["sud"],"tresor":c["tresor"],"pion":c["pion"]}

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    c={"nord":c["est"],"est":c["sud"],"sud":c["ouest"],"ouest":c["nord"],"tresor":c["tresor"],"pion":c["pion"]}

def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    Nrandom=random.choice(range(5))
    liste=["Horaire","AntiHoraire"]
    dirRandom=random.choice(liste)
    for i in range(Nrandom):
        if dirRandom=="Horaire":
            tournerHoraire(c)
        else:
            tournerAntiHoraire(c)

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire
    est de la forme bNbEbSbO où bN, bE, bS et bO valent
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre: c est une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    res=''
    # cle=["nord","est","sud","ouest"]
    # for i in range(len(cle)) :
    #     if c[cle[i]]:
    #         res=res+'1'
    #     else:
    #         res=res+'0'
    #     resultat=int(res,2)
    # return resultat # pour convertir une chaine de caractère qui est dans une base spécifique
    if c['nord']:
        res+='1'
    else:
        res+='0'
    if c['est']:
        res+='1'
    else:
        res+='0'
    if c['sud']:
        res+='1'
    else:
        res+='0'
    if c['ouest']:
        res+='1'
    else:
        res+='0'
    return int(res,2)

exemple=Carte(False,False,False,False,2,[1,2])
exemple2=Carte(False,True,True,True,0,[])
assert coderMurs(exemple)==0
assert coderMurs(carte)==9
assert coderMurs(exemple2)==7

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    valeur_binaire=bin(code)
    liste=list(valeur_binaire)
    i=0+len(liste)
    while i<6:  # pour que tous les chiffre binaire fasse une liste de 6
        liste.append(0)
        i+=1
    mur=['nord','est','sud','ouest']
    i=2
    i1=0
    while i<len(liste):
        if liste[i]=='1':
            c[mur[i1]]=True
        else:
            c[mur[i1]]=False
        i+=1
        i1+=1
    return c    # ATTENTION CE PRG CHANGE LE MATRICE DE BASE


assert decoderMurs(exemple,9)=={"nord":True,"est":False,"sud":False,"ouest":True,"tresor":2,"pion":[1,2]}
assert decoderMurs(exemple2,0)=={"nord":False,"est":False,"sud":False,"ouest":False,"tresor":0,"pion":[]}

def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    print(c)
    valeur=coderMurs(c)
    print(valeur)
    return listeCartes[valeur]

exemple=Carte(False,False,False,False,2,[1,2])
assert toChar(carte)=='╔'
assert toChar(exemple)=='╬'

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    carte2 = sud = False
    carte1 = nord = False
    """
    res=False
    if not carte1['nord'] and not carte2['sud']:
        res=True
    return res

essaie=Carte(False,True,False,False,2,[1,2])
essaie2=Carte(True,False,False,False,2,[1,2])
assert passageNord(essaie,essaie2)==True
# attention ne pas oublier que False signifie qu'il n'y a pas de mur et True veut dire le contraire

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    res=False
    if not carte1['sud'] and not carte2['nord']:
        res=True
    return res

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    res=False
    if not carte1['ouest'] and not carte2['est']:
        res=True
    return res

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    res=False
    if not carte1['est'] and not carte2['ouest']:
        res=True
    return res
