#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant
    valeurParDefaut dans chacune des cases
    paramètres:
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    matrice=[]
    for i in range(nbLignes):
        matrice.append([valeurParDefaut]*nbColonnes)
    return matrice

assert Matrice(3,3,0)==[[0,0,0],[0,0,0],[0,0,0]]


def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice)

assert getNbLignes([[0,0,0],[0,0,0],[0,0,0]])==3

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice[0])

assert getNbColonnes([[0,0,0],[0,0,0],[0,0,0]])==3

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice[ligne][colonne]

assert getVal([[0,0,0],[0,0,0],[0,0,9]],2,2)==9

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice[ligne][colonne]=valeur
    res=matrice
    return res

assert setVal([[0,0,0],[0,0,0],[0,0,9]],2,2,5)==[[0,0,0],[0,0,0],[0,0,5]]


#------------------------------------------
# decalages
#------------------------------------------

def decalageLigneAGauche(matrice, numLig, nouvelleValeur):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    if numLig<=getNbLignes(matrice):
        for i in range(len(matrice)):
            if i+1==numLig:
                ligne=matrice[i]
                ligne.insert(len(ligne),nouvelleValeur)
                valeur_rejettee=ligne[0]
                ligne.remove(ligne[0])
            #else rien
    #else rien
    return valeur_rejettee

assert decalageLigneAGauche([[1,2,3],[4,5,6],[7,8,9]],1,5)==1

def decalageLigneADroite(matrice, numLig, nouvelleValeur):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    if numLig<=getNbLignes(matrice):
        for i in range(len(matrice)):
            if i+1==numLig:
                ligne=matrice[i]
                ligne.insert(0,nouvelleValeur)
                valeur_rejettee=ligne[len(ligne)-1]
                ligne.pop()
            #else rien
    #else rien
    return valeur_rejettee

assert decalageLigneADroite([[1,2,3],[4,5,6],[7,8,9]],1,5)==3

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    if numCol<=getNbColonnes(matrice):
        for i in range(len(matrice)):
            if i+1==numCol:
                for i in range(getNbColonnes(matrice)):
                    valeur_intermediaire=matrice[len(matrice)-i-1][numCol-1]
                    matrice[len(matrice)-i-1][numCol-1]=nouvelleValeur
                    nouvelleValeur=valeur_intermediaire
                valeur_rejettee=valeur_intermediaire
            #else rien
    #else rien
    return valeur_rejettee

#assert decalageColonneEnHaut([[1,2,3],[4,5,6],[7,8,9]],1,5)==[[4,2,3],[7,5,6],[5,8,9]]
assert decalageColonneEnHaut([[1,2,3],[4,5,6],[7,8,9]],1,5)==1


def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    if numCol<=getNbColonnes(matrice):
        for i in range(len(matrice)):
            if i+1==numCol:
                for i in range(getNbColonnes(matrice)):
                    valeur_intermediaire=matrice[i][numCol-1]
                    matrice[i][numCol-1]=nouvelleValeur
                    nouvelleValeur=valeur_intermediaire
                valeur_rejettee=valeur_intermediaire
            #else rien
    #else rien
    return valeur_rejettee

#assert decalageColonneEnBas([[1,2,3],[4,5,6],[7,8,9]],1,5)==[[5,2,3],[1,5,6],[4,8,9]]
assert decalageColonneEnBas([[1,2,3],[4,5,6],[7,8,9]],1,5)==7
