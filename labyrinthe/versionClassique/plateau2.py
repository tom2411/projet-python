from matrice import *
from carte import *

dicoCarteFixes={(0,0):'1001',(0,2):'0001',(0,4):'0001',(0,6):'0011'
                ,(2,0):'1000',(2,2):'1000',(2,4):'0001',(2,6):'0010'
                ,(4,0):'1000',(4,2):'0100',(4,4):'0010',(4,6):'0010'
                ,(6,0):'1100',(6,2):'0100',(6,4):'0100',(6,6):'0110'}

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
    dicoCarteFixes={(0,0):'1001',(0,2):'0001',(0,4):'0001',(0,6):'0011'
                    ,(2,0):'1000',(2,2):'1000',(2,4):'0001',(2,6):'0010'
                    ,(4,0):'1000',(4,2):'0100',(4,4):'0010',(4,6):'0010'
                    ,(6,0):'1100',(6,2):'0100',(6,4):'0100',(6,6):'0110'}
    carte=Carte(False,False,False,False,0,[])
    dicoAngle={(0,0):'1001',(0,6):'0011',(6,0):'1100',(6,6):'0110'}
    # for i in range(getNbLignes(matrice)):
    #     for j in range(getNbColonnes(matrice)):
    #         if (i,j) in dicoCarteFixes:
    #             carteAplacer=decoderMurs(carte,dicoCarteFixes[(i,j)])
    #             carte=toChar(carteAplacer)
    #             setVal(matrice,i,j,carteAplacer)
    #         else:
    #             nbRandom=random.choice(listeCartesUtilisable)
    #             if nbRandom==4:
    #                 jonction-=1
    #             elif nbRandom==5:
    #                 angle-=1
    #             else:
    #                 toutDroit-=1
    #             #carte=decoderMurs(carte,nbRandom)
    #             setVal(matrice,i,j,0)
    # return matrice
    for i in range(getNbLignes(matrice)):
        for j in range(getNbColonnes(matrice)):
            if (i,j) in dicoCarteFixes.keys(): # placer les cartes fixes
                carteAplacer=decoderMurs(carte,dicoCarteFixes[(i,j)])
                setVal(matrice,i,j,toChar(carteAplacer))
            else: # placer les cartes amovibles
                liste_Angles=['0100']*20
                liste_Jonctions=['0101']*18
                liste_tout_droits=['0110']*12
                liste_cartes_amovibles=liste_Angles+liste_Jonctions+liste_tout_droits
                random.shuffle(liste_cartes_amovibles)
                for numIndex in liste_cartes_amovibles:  # touner aleatoirement mes cartes amovibles
                    tourneAleatoire(decoderMurs(carte,numIndex))
                nbRandom=random.choice(liste_cartes_amovibles)
                carteAmovible=decoderMurs(carte,nbRandom)
                setVal(matrice,i,j,toChar(carteAmovible))
            print(matrice)

    if nbJoueurs==1:
        poserPion()
    if nbJoueurs==2:
        poserPion()
    if nbJoueurs==3:
        poserPion()
    if nbJoueurs==4:
        poserPion()









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
    # trouve=True
    # # coder la suite
    # return trouve
	# carte_position = getVal(plateau[0],lig,col) #On recupere une carte
    # tresor = getTresor(carte_position) #Le numero du tresor present sur la carte
    # if tresor==numTresor: #Si c'est bien le tresor rechercher
    #     res = True
    # else:
    #     res = False
    # return res

    trouve=False
    if plateau[lig][col]["tresor"]==numTresor:
        trouve=True
        plateau[lig][col]["tresor"]==0
    return trouve


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
    colonne=0
    ligne=0
    for lig in plateau:
        for col in plateau:
            if col["tresor"]==numTresor:
                trouve=True
            if trouve==True:
                return(colonne,ligne)
            colonne+=1
        ligne+=1
    return None



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

    colonne=0
    ligne=0
    for lig in plateau:
        for col in plateau:
            if col["pion"]==numJoueur:
                trouve=True
            if trouve==True:
                return(colonne,ligne)
            colonne+=1
        ligne+=1
    return None

def prendrePionPlateau(plateau,lig,col,numJoueur):
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
    trouve=False
    if plateau[lig][col]["pions"]==numJoueur:
        trouve=True
        del plateau[lig][col]["pions"]
    return trouve


def poserPionPlateau(plateau,lig,col,numJoueur):
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
    plateau[lig][col]["pions"].append(numJoueur)

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
            if j>0 and passageOuest(plateau[0][i][j],plateau[0][i][j-1]) or j<getNbColonnes(plateau[0])-1 and passageEst(plateau[0][i][j],plateau[0][i][j+1]) or i>0 and passageNord(plateau[0][i][j],plateau[0][i-1][j]) or i<getNbLignes(plateau[0])-1 and passageSud(plateau[0][i][j],plateau[0][i+1][j]):
                if i>0 and getVal(calque,i-1,j)==val and passageNord(plateau[0][i][j],plateau[0][i-1][j]) or j>0 and getVal(calque,i,j-1)==val and passageOuest(plateau[0][i][j],plateau[0][i][j-1]) or i<getNbLignes(plateau[0])-1 and getVal(calque,i+1,j)==val  and passageSud(plateau[0][i][j],plateau[0][i+1][j]) or j<getNbColonnes(plateau[0])-1 and getVal(calque,i,j+1)==val and passageEst(plateau[0][i][j],plateau[0][i][j+1]):
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

assert accessibleDist(([[{'nord':False,'est':False,'sud':True,'ouest':False},{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False}],[{'nord':True, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False},{'nord':True, 'est':False, 'sud':False, 'ouest':False}],[{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':True, 'est':False, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':False, 'ouest':False}]],{'inutile':True}),1,1,3,3)==[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
assert accessibleDist(([[{'nord':False,'est':False,'sud':True,'ouest':False},{'nord':False, 'est':True, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':False}],[{'nord':True, 'est':True, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':True, 'ouest':True},{'nord':True, 'est':False, 'sud':False, 'ouest':False}],[{'nord':False, 'est':False, 'sud':False, 'ouest':False},{'nord':True, 'est':True, 'sud':False, 'ouest':False},{'nord':False, 'est':False, 'sud':False, 'ouest':True}]],{'inutile':True}),1,1,3,3)==[(0,0),(0,1),(1,1),(1,2),(2,2)]
