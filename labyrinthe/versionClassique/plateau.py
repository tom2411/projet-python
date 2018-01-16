from matrice import *
from carte import *


def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    parametres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
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

    carte=Carte(False,False,False,False,0,[])

    # Cartes fixes
    c=Carte(True,True,False,False,0,[])
    setVal(matrice,0,0,c)

    c=Carte(True,False,False,False,0,[])
    setVal(matrice,0,2,c)

    c=Carte(True,False,False,False,0,[])
    setVal(matrice,0,4,c)

    c=Carte(True,False,False,True,0,[])
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



    num=1
    liste_Angles=['0100']*20
    liste_Jonctions=['0101']*18
    liste_tout_droits=['0110']*12
    liste_cartes_amovibles=liste_Angles+liste_Jonctions+liste_tout_droits
    # for i in range(getNbLignes(matrice)):
    #     for j in range(getNbColonnes(matrice)):
    #         if (i,j) in dicoCarteFixes: # placer les cartes fixes
    #             carteAplacer=decoderMurs(carte,dicoCarteFixes[(i,j)])
    #             setVal(matrice,i,j,carteAplacer)
    #         else:
    #             random.shuffle(liste_cartes_amovibles)
    #             for numIndex in liste_cartes_amovibles:  # touner aleatoirement mes cartes amovibles
    #                 tourneAleatoire(decoderMurs(carte,numIndex))
    #             nbRandom=random.choice(liste_cartes_amovibles)
    #             carteAmovible=decoderMurs(carte,nbRandom)
    #             setVal(matrice,i,j,carteAmovible)
            # if matrice[0][0]['pion']==[] and nbJoueurs>=1:
            #     matrice[0][0]['pion'].append(1)

    for i in range(getNbLignes(matrice)):
        for j in range(getNbColonnes(matrice)): # placement des cartes amovibles
            if matrice[i][j]==0:
                random.shuffle(liste_cartes_amovibles)
                for numIndex in liste_cartes_amovibles:  # touner aleatoirement mes cartes amovibles
                    tourneAleatoire(decoderMurs(carte,numIndex))
                nbRandom=random.choice(liste_cartes_amovibles)
                carteAmovible=decoderMurs(carte,nbRandom)
                setVal(matrice,i,j,carteAmovible)

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

    liste=list(range(nbTresors))
    liste.insert(len(liste),len(liste))
    while len(liste) < 45:
        liste.append(0)

    random.shuffle(liste)
    print(liste)
    # place les différents trésors

    for i in range(getNbLignes(matrice)):
        for j in range(getNbColonnes(matrice)):
            if (i,j)!=(0,0) or (i,j)!=(0,6) or (i,j)!=(6,0) or (i,j)!=(6,6):
                mettreTresor(matrice[i][j],liste[0])
                liste.remove(liste[0])




    return (matrice,0)






def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    # liste=[]
    # #coder le prg
    # return liste

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
	coordonneesCarte=getVal(plateau[0],lig,col) #On recupere une carte
    tresor = getTresor(carte_position) #Le numero du tresor present sur la carte
    if tresor==numTresor: #Si c'est bien le tresor rechercher
        res = True
    else:
        res = False
    return res

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    # coder la fonction
    #return (lig,col)
	# nbLignes = getNbLignes(plateau[0])
    # nbColonnes = getNbColonnes(plateau[0])
    # iLig = 0
    # iCol = 0
    # res = None
    #
    # while (res==None) and (iLig<nbLignes) and (iCol<nbColonnes): #Tant que l'on as pas trouver le tresor et que l'on peut parcourir la matrice
    #     tresor_sur_carte_actuel = prendreTresorPlateau(plateau,iLig,iCol,numTresor) #Verifie si le tresor se trouve sur la carte sur laquelle on est
    #     if tresor_sur_carte_actuel: #Si le tresor est sur la carte sur laquelle on est
    #         res = (iLig,iCol) #On enregistre les coordonnées du trésor
    #     else: #Sinon
    #         iCol = (iCol+1)%nbColonnes #On passe à la colonne suivante (ou l'on revient au debut des colonnes)
    #         if iCol == 0: #Si on est revenus au debut de la colonne
    #             iLig += 1 #On passe à la ligne suivante
    #
    # return res
    for i in range(getNbLignes(plateau[0])):
        for j in range(getNbColonnes(plateau[0])):
            if plateau[0][i][j]['tresor']==numTresor:
                return (i,j)

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    #coder la fonction
    # return (lig,col)
    # nbLignes = getNbLignes(plateau[0])
    # nbColonnes = getNbColonnes(plateau[0])
    # iLig = 0
    # iCol = 0
    # res = None
    #
    # while (res==None) and (iLig<nbLignes) and (iCol<nbColonnes): #Tant que l'on as pas trouver le joueur et que l'on peut parcourir la matrice
    #     carte_position = getVal(plateau[0],iLig,iCol) #On recupere la carte sur laquelle on est
    #     if possedePion(carte_position,numJoueur): #Si le joueur est sur la carte sur laquelle on est
    #         res = (iLig,iCol) #On enregistre les coordonnées du joueur
    #     else: #Sinon
    #         iCol = (iCol+1)%nbColonnes #On passe à la colonne suivante (ou l'on revient au debut des colonnes)
    #         if iCol == 0: #Si on est revenus au debut de la colonne
    #             iLig += 1 #On passe à la ligne suivante
    #
    # return res
    res=None
    for i in range(getNbLignes(plateau[0])):
        for j in range(getNbColonnes(plateau[0])):
            if plateau[0][i][j]['pion']==numJoueur:
                res=(i,j)
    return res


def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
	# carte_position = getVal(plateau[0],lin,col) #On recupere la carte selectionnee
    # prendrePion(carte_position,numJoueur) #Enleve le pion de la carte


def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    # carte_position = getVal(plateau[0],lin,col) #On recupere la carte selectionnee
    # poserPion(carte_position,numJoueur) #Enleve le pion de la carte


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
    chemin_sortie=True
    # coder la fonction
    return chemin_sortie

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
    liste=[]
    # coder la suite du prg
    return liste
