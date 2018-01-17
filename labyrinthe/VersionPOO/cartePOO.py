import random 

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


class Carte(object):

  def __init__(self, nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    self._nord=nord
    self._est=est
    self._sud=sud
    self._ouest=ouest
    self._tresor=tresor
    self._pions=pions
  

  # True=mur
  # False= pas de mur


  def estValide(self):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zero,un ou deux murs
    paramètre: c une carte
    """
    cpt=0
    res=True
    liste=[self._nord,self._est,self._sud,self._ouest]
    for elem in liste:
      if elem:
        cpt+=1
    if cpt>3:
      res=False
    return res

  
    
  def murNord(self):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    res=False
    if self._nord:
      res=True
    return res
  

  def murSud(self):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    res=False
    if self._sud:
        res=True
    return res


  def murEst(self):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    res=False
    if self._est:
        res=True
    return res


  def murOuest(self):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    res=False
    if self._ouest:
        res=True
    return res


  def getListePions(self):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return self._pions


  def setListePions(self,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    self._pions.append(listePions)

  def getNbPions(self):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(self._pions)


  def possedePion(self,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètre: c une carte
    """
    res=False
    if pion in self._pions:
        res=True
    return res


  def getTresor(self):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return self._tresor


  def prendreTresor(self):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    valeur_intermediaire=self._tresor
    self._tresor=0
    return valeur_intermediaire


  def mettreTresor(self,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    Cette fonction modifie la carte mais ne retourne rien
    """
    valeur_intermediaire=self._tresor
    self._tresor=tresor
    return valeur_intermediaire

  #assert mettreTresor(c,1)==2 # faire attention car ne fonctionne qu'une seule fois car
                            # après l'on change la valeur de tresor

  def prendrePion(self, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion in self._pions:
        self._pions.remove(pion)
    #else rien

  def poserPion(self, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in self._pions:
        self._pions.append(pion)
    #else rien

  def tournerHoraire(self):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    self._nord=self._ouest
    self._est=self._nord
    self._ouest=self._sud
    self._sud=self._est


  def tournerAntiHoraire(self):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    self._nord=self._est
    self._est=self._sud
    self._ouest=self._nord
    self._sud=self._ouest

  def tourneAleatoire(self):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    Nrandom=random.choice(range(5))
    liste=["Horaire","AntiHoraire"]
    dirRandom=random.choice(direction)
    for i in range(Nrandom):
        if dirRandom=="Horaire":
            self.tournerHoraire()
        else:
            self.tournerAntiHoraire()

  
  def coderMurs(self):
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
    res=""
    liste=[self._nord,self._est,self._sud,self._ouest]
    for elem in liste:
        if elem:
            res+="1"
        else:
            res+="0"
    return int(res,2) # pour convertir une chaine de caractère qui est dans une base spécifique


  def decoderMurs(self,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    valeur_binaire=bin(code)
    liste=list(valeur_binaire)
    mur=[self._nord,self._est,self._sud,self._ouest]
    i=2
    i1=0
    while i<len(liste):
        if liste[i]=='1':
            [mur[i1]]=True
        else:
            [mur[i1]]=False
        i+=1
        i1+=1
    return self

  #exemple=Carte(False,False,False,False,2,[1,2])

  def toChar(self):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    valeur=self.coderMurs()
    return listeCartes[valeur]


  def passageNord(self,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    carte2 = sud = False
    carte1 = nord = False
    """
    res=False
    if not self._nord and not carte2.murSud():
        res=True
    return res

  # attention ne pas oublier que False signifie qu'il n'y a pas de mur et True veut dire le contraire

  def passageSud(self,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    res=False
    if not self._sud and not carte2.murNord():
        res=True
    return res

  def passageOuest(self,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    res=False
    if not self._ouest and not carte2.murEst():
        res=True
    return res

  def passageEst(self,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    res=False
    if not self._est and not carte2murOuest():
        res=True
    return res

c=Carte(True,False,False,True,2,[1,2])
assert c.estValide()==True
assert c.murNord()==True
assert c.murSud()==False
assert c.murEst()==False
assert c.murOuest()==True
assert c.getListePions()==[1,2]
assert c.getNbPions()==2
assert c.possedePion(2)==True
assert c.getTresor()==2
assert c.prendreTresor()==2
assert c.coderMurs()==9
assert c.toChar()=='╔'
essaie=Carte(False,True,False,False,2,[1,2])
essaie2=Carte(True,False,False,False,2,[1,2])
assert essaie.passageNord(essaie2)==True
assert essaie.passageSud(essaie2)==False
assert essaie.passageOuest(essaie2)==True
assert essaie.passageEst(essaie2)==False