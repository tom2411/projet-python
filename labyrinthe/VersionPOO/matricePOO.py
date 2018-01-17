#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------
class Matrice(object):

  def __init__(self,nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant
    valeurParDefaut dans chacune des cases
    paramètres:
     nbLignes un entier strictement positif qui indique le nombre de lignes
     nbColonnes un entier strictement positif qui indique le nombre de colonnes
     valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    self._matrice=[]
    self._lignes=nbLignes
    self._colonnes=nbColonnes
    for i in range(nbLignes):
        self._matrice.append([valeurParDefaut]*nbColonnes)
      
  def getNbLignes(self):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return self._lignes


  def getNbColonnes(self):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return self._colonnes


  def getVal(self,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return self._matrice[ligne][colonne]


  def setVal(self,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    self._matrice[ligne][colonne]=valeur
    res=self._matrice
    return res


  #------------------------------------------
  # decalages
  #------------------------------------------

  def decalageLigneAGauche(self, numLig, nouvelleValeur):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    if numLig<=self._lignes:
        for i in range(self._lignes):
            if i+1==numLig:
                ligne=self._matrice[i]
                ligne.insert(len(ligne),nouvelleValeur)
                valeur_rejettee=ligne[0]
                ligne.remove(ligne[0])
            #else rien
    #else rien
    return valeur_rejettee


  def decalageLigneADroite(self, numLig, nouvelleValeur):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valeur_rejettee=self._matrice[numLig][1]
    if numLig<=self._lignes:
        i=numLig-1
        ligne=self._matrice[i]
        ligne.insert(0,nouvelleValeur)
        valeur_rejettee=ligne[len(ligne)-1]
        ligne.remove(ligne[-1])
    return valeur_rejettee


  def decalageColonneEnHaut(self, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valeur_rejettee=self._matrice[0][numCol-1]
    if numCol<=self._colonnes:
        for i in range(self._lignes):
            if i+1==numCol:
                for j in range(self._colonnes):
                    valeur_intermediaire=self._matrice[self._lignes-i-1][numCol-1]
                    self._matrice[self._lignes-i-1][numCol-1]=nouvelleValeur
                    nouvelleValeur=valeur_intermediaire
            #else rien
    #else rien
    return valeur_rejettee

  #assert decalageColonneEnHaut([[1,2,3],[4,5,6],[7,8,9]],1,5)==[[4,2,3],[7,5,6],[5,8,9]]


  def decalageColonneEnBas(self, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valeur_rejettee=self._matrice[self._lignes-1][numCol-1]
    if numCol<=self._colonnes:
        for i in range(self._lignes):
            if i+1==numCol:
                for j in range(self._colonnes):
                    valeur_intermediaire=self._matrice[i][numCol-1]
                    self._matrice[i][numCol-1]=nouvelleValeur
                    nouvelleValeur=valeur_intermediaire
            #else rien
    #else rien
    return valeur_rejettee

  #assert decalageColonneEnBas([[1,2,3],[4,5,6],[7,8,9]],1,5)==[[5,2,3],[1,5,6],[4,8,9]]

c=Matrice(3,3,0)
d=Matrice(3,3,0)
d.setVal(2,2,9)
e=Matrice(3,3,0)
e.setVal(0,0,1)
e.setVal(0,1,2)
e.setVal(0,2,3)
e.setVal(1,0,4)
e.setVal(1,1,5)
e.setVal(1,2,6)
e.setVal(2,0,7)
e.setVal(2,1,8)
e.setVal(2,2,9)
assert c.getNbLignes()==3
assert c.getNbColonnes()==3
assert d.getVal(2,2)==9
assert d.setVal(2,2,5)==[[0,0,0],[0,0,0],[0,0,5]]
assert e.decalageLigneAGauche(1,5)==1 
assert e.decalageLigneADroite(1,5)==3 
assert e.decalageColonneEnHaut(1,5)==1