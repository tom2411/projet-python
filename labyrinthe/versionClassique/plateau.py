from matrice import *
from carte import *

a = ([[{'nord': True, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': [[1]]}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 2, 'pion': []}, {'nord': False, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 1, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}], [{'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': True, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': False, 'sud': True, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': [[2]]}]], {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []})

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    parametres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 12 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    matrice=Matrice(7,7,0)
    # carte fixe
    # dicoCarteFixes={(0,0):'1001',(0,2):'0001',(0,4):'0001',(0,6):'0011'
    #                 ,(2,0):'1000',(2,2):'1000',(2,4):'0001',(2,6):'0010'
    #                 ,(4,0):'1000',(4,2):'0100',(4,4):'0010',(4,6):'0010'
    #                 ,(6,0):'1100',(6,2):'0100',(6,4):'0100',(6,6):'0110'}

    # carte=Carte(False,False,False,False,0,[])

    # Cartes fixes
    c=Carte(True,False,False,True,0,[])
    setVal(matrice,0,0,c)

    c=Carte(True,False,False,False,0,[])
    setVal(matrice,0,2,c)

    c=Carte(True,False,False,False,0,[])
    setVal(matrice,0,4,c)

    c=Carte(True,True,False,False,0,[])
    setVal(matrice,0,6,c)

    c=Carte(False,False,False,True,0,[])
    setVal(matrice,2,0,c)

    c=Carte(False,False,False,True,0,[])
    setVal(matrice,2,2,c)

    c=Carte(True,False,False,False,0,[])
    setVal(matrice,2,4,c)

    c=Carte(False,True,False,False,0,[])
    setVal(matrice,2,6,c)

    c=Carte(False,False,False,True,0,[])
    setVal(matrice,4,0,c)

    c=Carte(False,False,True,False,0,[])
    setVal(matrice,4,2,c)

    c=Carte(False,False,False,True,0,[])
    setVal(matrice,4,4,c)

    c=Carte(False,False,False,True,0,[])
    setVal(matrice,4,6,c)

    c=Carte(False,False,True,True,0,[])
    setVal(matrice,6,0,c)

    c=Carte(False,False,True,False,0,[])
    setVal(matrice,6,2,c)

    c=Carte(False,False,True,False,0,[])
    setVal(matrice,6,4,c)

    c=Carte(False,True,True,False,0,[])
    setVal(matrice,6,6,c)




    liste_Angles=['0100']*16
    liste_Jonctions=['0101']*6
    liste_tout_droits=['0110']*12
    liste_cartes_amovibles=liste_Angles+liste_Jonctions+liste_tout_droits

    random.shuffle(liste_cartes_amovibles)
    cartesPlacees=0
    for i in range(getNbLignes(matrice)):
        for j in range(getNbColonnes(matrice)): # placement des cartes amovibles
            if matrice[i][j]==0:

                carte=Carte(False,False,False,False,0,[])
                carte=decoderMurs(carte,liste_cartes_amovibles[cartesPlacees])
                tourneAleatoire(carte)
                print(cartesPlacees,carte,toChar(carte))
                cartesPlacees+=1
                # tourneAleatoire(carteAmovible)
                setVal(matrice,i,j,carte)
    carteAJouer = Carte(False,False,False,False)
    decoderMurs(carteAJouer,liste_cartes_amovibles[-1])

    # place les joueurs selon leur nombre
    if nbJoueurs>=1:
        c = getVal(matrice,0,0)
        setListePions(c,[1])
    if nbJoueurs>=2:
        c = getVal(matrice,6,6)
        setListePions(c,[2])
    if nbJoueurs>=3:
        c = getVal(matrice,6,0)
        setListePions(c,[3])
    if nbJoueurs==4:
        c = getVal(matrice,0,6)
        setListePions(c,[4])


    liste=list(range(1,nbTresors+1)) # liste qui contient les tresors
    print(liste)
    random.shuffle(liste)
    liste_carte_fixes=[]
    for i in [0,2,4,6]: # creation de la liste de carte fixes sans les angles
        for j in [0,2,4,6]:
            if (i,j)==(0,0) or (i,j)==(0,6) or (i,j)==(6,0) or (i,j)==(6,6):
                continue
            else:
                liste_carte_fixes.append((i,j))
    random.shuffle(liste_carte_fixes)
    #print(liste_carte_fixes)

    # creation d'une liste qui contient les coordonnées des cartes amovibles
    liste_carte_Amovibles=[]
    for i in [1,3,5]:
        for j in [0,1,2,3,4,5,6]:
            liste_carte_Amovibles.append((i,j))
    random.shuffle(liste_carte_Amovibles)
    print(liste_carte_Amovibles)

    # placement des tresors sur les cartes
    i=0
    j=0
    while i<getNbLignes(matrice) and j<getNbColonnes(matrice) and len(liste)>0:
        if (i,j) in liste_carte_fixes:
            mettreTresor(matrice[i][j],liste[0])
            liste_carte_fixes.remove((i,j))
            liste.remove(liste[0])
            print(liste)
            j+=1
            if j==getNbColonnes(matrice):
                j=0
                i+=1
        elif (i,j) in liste_carte_Amovibles:
            mettreTresor(matrice[i][j],liste[0])
            #liste_carte_Amovibles.remove((i,j))
            del liste_carte_Amovibles[liste_carte_Amovibles.index((i,j))]
            liste.remove(liste[0])
        j+=1
        if j==getNbColonnes(matrice):
            j=0
            i+=1
        else:
            pass
    print(len(liste))
    res=(matrice,carteAJouer)
    return res

def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """


def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """

    coordonneesCarte=getVal(plateau[0],lig,col)
    tresor=getTresor(coordonneesCarte)
    if tresor==numTresor:
        res=True
    else:
        res=False
    return res

assert prendreTresorPlateau(a,3,3,1)==False

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """

    res=None
    for i in range(getNbLignes(plateau[0])):
        for j in range(getNbColonnes(plateau[0])):
            if plateau[0][i][j]['tresor']==numTresor:
                res=(i,j)
    return res

assert getCoordonneesTresor(a,1)==(0,4)

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """

    res=None
    for i in range(getNbLignes(plateau[0])):
        for j in range(getNbColonnes(plateau[0])):
            if len(plateau[0][i][j]['pion'])!=0:
                if numJoueur in plateau[0][i][j]['pion'][0]:
                    res=(i,j)
    return res

assert getCoordonneesJoueur(a,1)==(0,0)


def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """

    joueur=getVal(plateau[0],lin,col)
    prendrePion(joueur,numJoueur)



def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """

    joueur=getVal(plateau[0],lin,col)
    poserPion(joueur,numJoueur)

def marquageDirect(calque,plateau,val=1,marque=1):
    '''
    marque avec la valeur 'marque' les éléments du calque tel que la valeur
    correspondante n'est pas un mur (de valeur differente de 1) et
    qu'un de ses voisins dans le calque à pour valeur val
    la fonction doit retourner True si au moins une case du calque a été marquée
    calque= [0,0,0,0,0,0,0,     calque est la matrcie que l'on marque quand l'on peut passer quand il y a un couloir dans
             0,0,0,0,0,0,0,     la matrice de base du labyrinthe (plateau)
             0,0,0,0,0,0,0,     plateau est le labyrinthe de base
             0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,
             0,0,0,0,0,0,0]
    '''

    res=False
    for i in range(getNbLignes(calque)):
        for j in range(getNbColonnes(calque)):
            if (j>0 and passageOuest(plateau[0][i][j],plateau[0][i][j-1]) or j<getNbColonnes(plateau[0])-1
            and passageEst(plateau[0][i][j],plateau[0][i][j+1]) or i>0 and passageNord(plateau[0][i][j],plateau[0][i-1][j]) or i<getNbLignes(plateau[0])-1
            and passageSud(plateau[0][i][j],plateau[0][i+1][j])):
                if (i>0 and getVal(calque,i-1,j)==val and passageNord(plateau[0][i][j],plateau[0][i-1][j]) or j>0 and getVal(calque,i,j-1)==val
                and passageOuest(plateau[0][i][j],plateau[0][i][j-1]) or i<getNbLignes(plateau[0])-1 and getVal(calque,i+1,j)==val
                and passageSud(plateau[0][i][j],plateau[0][i+1][j]) or j<getNbColonnes(plateau[0])-1 and getVal(calque,i,j+1)==val and passageEst(plateau[0][i][j],plateau[0][i][j+1])):
                    if getVal(calque,i,j)!=marque:
                        setVal(calque,i,j,marque)
                        res=True

    return (res,marque)

def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    print(plateau[0][1][1])
    calque=Matrice(getNbLignes(plateau[0]),getNbColonnes(plateau[0]),0)
    setVal(calque,ligD-1,colD-1,1)
    res=False
    marquage=marquageDirect(calque,plateau,1,1)[0]
    if marquage:
        if getVal(calque,ligA-1,colA-1)==1:
            res=True
    return res

assert accessible(([[{'nord':False,'est':False,'sud':True,'ouest':False},{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False}],[{'nord':True, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False},{'nord':True, 'est':False, 'sud':False, 'ouest':False}],[{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':True, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':False, 'ouest':False}]],{'inutile':True}),1,1,3,3)==True
assert accessible(([[{'nord':False,'est':False,'sud':True,'ouest':False},{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False}],[{'nord':True, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False},{'nord':True, 'est':False, 'sud':False, 'ouest':False}],[{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':True, 'est':False, 'sud':False, 'ouest':False},{'nord':True, 'est':True, 'sud':True, 'ouest':True}]],{'inutile':True}),1,1,3,3)==False


def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin,
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    if not accessible(plateau, ligD, colD, ligA, colA):
        return None
    else:
        calque=Matrice(getNbLignes(plateau[0]),getNbColonnes(plateau[0]),0)
        setVal(calque,ligD-1,colD-1,1)
        res=[]
        marquage=marquageDirect(calque,plateau,1,1)
        for i in range(getNbLignes(calque)):
            for j in range(getNbColonnes(calque)):
                if getVal(calque,i,j)==1:
                    res.append((i,j))
        return res

assert accessibleDist(([[{'nord':False,'est':False,'sud':True,'ouest':False},{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False}],[{'nord':True, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False},{'nord':True, 'est':False, 'sud':False, 'ouest':False}],[{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':True, 'est':False, 'sud':False, 'ouest':False},{'nord':False,'est':False, 'sud':False, 'ouest':False}]],{'inutile':True}),1,1,3,3)== [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
assert accessibleDist(([[{'nord':False,'est':False,'sud':True,'ouest':False},{'nord':False, 'est':True, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False}],[{'nord':True, 'est':True, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':True},{'nord':True, 'est':False, 'sud':False, 'ouest':False}],[{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':True, 'est':True, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':False, 'ouest':True}]],{'inutile':True}),1,1,3,3)==[(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]


def affichePlateau(plateau):
    """
    affichage redimentaire d'un plateau
    """

    for i in range(getNbLignes(plateau[0])):
        res=' '
        for j in range(getNbLignes(plateau[0][i])) :
            res+=toChar(plateau[0][i][j])
        print(res)
