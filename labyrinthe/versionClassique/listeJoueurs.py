import random
from joueur import *


def listeJoueurs(joueur):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    listeJoueur=[]
    for joueur in joueur:
        player=Joueur(joueur)
        listeJoueur.append(player)
    return listeJoueur
assert(listeJoueurs(["michel","pierre","louis"])==[("michel",[],[0]),("pierre",[],[0]),("louis",[],[0])])

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs.append(joueur)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    random.shuffle(joueurs)
    e=1
    for i in range(len(joueurs)):
        joueurs[i][2][0]=e
        e=e+1
    
initAleatoireJoueurCourant([("michel",[],[0]),("pierre",[],[0]),("louis",[],[0])])


def distribuerTresors(joueurs,nbTresors=24,nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    listeTresor=[x for x in range(nbTresors)]
    random.shuffle(listeTresor)
    nbDist=len(listeTresor)//len(joueurs)
    e=0
    for i in range(0,len(listeTresor),len(joueurs)):
        for joueur in joueurs:
            joueur[1].append(listeTresor[e])
            e=e+1
distribuerTresors([("michel",[],[0]),("pierre",[],[0]),("louis",[],[0])])


def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """   
    for i in range(len(joueurs)):
        if i==0:
            listAv0=joueurs[len(joueurs)-1]
            joueurs[len(joueurs)-1]=joueurs[0]
        if i>0 and i<(len(joueurs)-1):
            joueurs[i-1]=joueurs[i]
    joueurs[len(joueurs)-2]=listAv0
changerJoueurCourant([("michel",[],[1]),("pierre",[],[2]),("louis",[],[3]),("raoul",[],[4])])

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)
assert(getNbJoueurs([("michel",[],[1]),("pierre",[],[2]),("louis",[],[3]),("raoul",[],[4])])==4)

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    return joueurs[0]
assert(getJoueurCourant([("michel",[],[1]),("pierre",[],[2]),("louis",[],[3]),("raoul",[],[4])])==("michel",[],[1]))

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    del joueurs[0][1][0]

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésor restant pour le joueur dont le numero 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    for joueur in joueurs:
        if joueur[2][0]==numJoueur:
            return len(joueur[1])
assert (nbTresorsRestantsJoueur([("michel",[1,2,3],[1]),("pierre",[4,5,6],[2]),("louis",[7,8,9],[3]),("raoul",[10,11,12],[4])],2)==3)


def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs[0][2][0]
assert(numJoueurCourant([("michel",[1,2,3],[1]),("pierre",[4,5,6],[2]),("louis",[7,8,9],[3]),("raoul",[10,11,12],[4])])==1)

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return joueurs[0][0]
assert(nomJoueurCourant([("michel",[1,2,3],[1]),("pierre",[4,5,6],[2]),("louis",[7,8,9],[3]),("raoul",[10,11,12],[4])])=="michel")

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    for joueur in joueurs:
        if joueur[2][0]==numJoueur:
            return joueur[0]
assert(nomJoueur([("michel",[1,2,3],[1]),("pierre",[4,5,6],[2]),("louis",[7,8,9],[3]),("raoul",[10,11,12],[4])],2)=="pierre")
    

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    for joueur in joueurs:
        if joueur[2][0]==numJoueur:
            return joueur[1][0]
assert(prochainTresorJoueur([("michel",[1,2,3],[1]),("pierre",[4,5,6],[2]),("louis",[7,8,9],[3]),("raoul",[10,11,12],[4])],2)==4)

    

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return joueurs[0][1][0]
assert(tresorCourant([("michel",[1,2,3],[1]),("pierre",[4,5,6],[2]),("louis",[7,8,9],[3]),("raoul",[10,11,12],[4])])==1)

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    res=False
    if joueurs[0][1] == []:
        res=True
    return res
assert(joueurCourantAFini([("michel",[1,2,3],[1]),("pierre",[4,5,6],[2]),("louis",[7,8,9],[3]),("raoul",[10,11,12],[4])])==False)
assert(joueurCourantAFini([("michel",[],[1]),("pierre",[4,5,6],[2]),("louis",[7,8,9],[3]),("raoul",[10,11,12],[4])])==True)