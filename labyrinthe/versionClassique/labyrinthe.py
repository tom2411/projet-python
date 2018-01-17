from listeJoueurs import *
from plateau import *

plat=([[{'nord': True, 'est': True, 'sud': False, 'ouest': False, 'tresor': 2, 'pion': [[1]]}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 4, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 2, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 1, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': False, 'ouest': True, 'tresor': 0, 'pion': []}], [{'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': True, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 2, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}], [{'nord': False, 'est': False, 'sud': True, 'ouest': True, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': False, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': []}, {'nord': False, 'est': True, 'sud': True, 'ouest': False, 'tresor': 0, 'pion': [[2]]}]],{'nord': True, 'est': True, 'sud': False, 'ouest': False, 'tresor': 0, 'pion': [[1]]} )

laby={"player":[("michel",[2,4,3],[1]),("louis",[5,8,7],[0])],"phase":0,"plateau":plat,"interdit":(1,'N')}
laby2={"player":[("michel",[1,2,3],[0]),("louis",[5,8,7],[1])],"phase":1,"plateau":plat,"interdit":(3,'O')}
def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    dico={}
    player=listeJoueurs(nomsJoueurs)
    distribuerTresors(player)
    initAleatoireJoueurCourant(player)
    dico["player"]=player
    dico["phase"]=0 #c'est la phase du jeu
    print(len(nomsJoueurs))
    dico["plateau"]=Plateau(len(nomsJoueurs),nbTresors)
    dico["interdit"]=None
    return dico 

#print(Labyrinthe(["michel","louis"],24,0))


def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return labyrinthe["plateau"]

#print(getPlateau(laby))
    
    

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return len(labyrinthe["player"])

assert(getNbParticipants({'player': [('michel', [15, 12, 10, 17, 8, 22], [0]), ('pierre', [4, 13, 3, 18, 0, 20], [1]), ('raoul', [23, 21, 2, 16, 19, 5], [2]), ('louis', [6, 11, 14, 1, 7, 9], [3])], 'phase': 0, 'plateau': None, 'interdit':None})==4)

    

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return labyrinthe["player"][0][0]

assert(getNomJoueurCourant({'player': [('michel', [15, 12, 10, 17, 8, 22], [0]), ('pierre', [4, 13, 3, 18, 0, 20], [1]), ('raoul', [23, 21, 2, 16, 19, 5], [2]), ('louis', [6, 11, 14, 1, 7, 9], [3])], 'phase': 0, 'plateau': None, 'interdit':None}))=="michel"

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return labyrinthe["player"][0][2][0]

assert(getNumJoueurCourant({'player': [('michel', [15, 12, 10, 17, 8, 22], [8]), ('pierre', [4, 13, 3, 18, 0, 20], [1]), ('raoul', [23, 21, 2, 16, 19, 5], [2]), ('louis', [6, 11, 14, 1, 7, 9], [3])], 'phase': 0, 'plateau': None, 'interdit':None}))==8

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """   
    return labyrinthe["phase"]

assert(getPhase({'player': [('michel', [15, 12, 10, 17, 8, 22], [0]), ('pierre', [4, 13, 3, 18, 0, 20], [1]), ('raoul', [23, 21, 2, 16, 19, 5], [2]), ('louis', [6, 11, 14, 1, 7, 9], [3])], 'phase': 0, 'plateau': None, 'interdit':None}))==0


def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """    
    if labyrinthe["phase"]==0:
        labyrinthe["phase"]=1
    
    elif labyrinthe["phase"]==1:
        labyrinthe["phase"]=0
        changerJoueurCourant(labyrinthe['player'])

#changerPhase(laby)
#print(laby)

def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """   
    cpt=0 
    for i in range(len(labyrinthe["player"])):
        cpt+=len(labyrinthe["player"][i][1])
    return cpt
assert(getNbTresors({'player': [('michel', [15, 12, 10, 17, 8, 22], [0]), ('pierre', [4, 13, 3, 18, 0, 20], [1]), ('raoul', [23, 21, 2, 16, 19, 5], [2]), ('louis', [6, 11, 14, 1, 7, 9], [3])], 'phase': 0, 'plateau': None, 'interdit':None}))==24

def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    return labyrinthe["player"]

assert(getListeJoueurs({'player': [('michel', [15, 12, 10, 17, 8, 22], [0]), ('pierre', [4, 13, 3, 18, 0, 20], [1]), ('raoul', [23, 21, 2, 16, 19, 5], [2]), ('louis', [6, 11, 14, 1, 7, 9], [3])], 'phase': 0, 'plateau': None, 'interdit':None}))==[('michel', [15, 12, 10, 17, 8, 22], [0]), ('pierre', [4, 13, 3, 18, 0, 20], [1]), ('raoul', [23, 21, 2, 16, 19, 5], [2]), ('louis', [6, 11, 14, 1, 7, 9], [3])]
        
def enleverTresor(labyrinthe,lig,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe. 
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    plateau=labyrinthe["plateau"][0]
    trouve=False
    if plateau[lig][col]["tresor"]==numTresor:
        plateau[lig][col]["tresor"]=0
        trouve=True
        for joueur in labyrinthe['player']:
            if joueur[1][0]==numTresor:
                del joueur[1][0]
                 
    return trouve

assert(enleverTresor(laby,1,1,2)==True)

def prendreJoueurCourant(labyrinthe,lig,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe    
    """
    joueur=labyrinthe["player"][0][2]
    if joueur in labyrinthe['plateau'][0][lig][col]['pion']:
        labyrinthe['plateau'][0][lig][col]['pion'].remove(joueur)

#prendreJoueurCourant(laby,0,0)
#print(laby)

def poserJoueurCourant(labyrinthe,lig,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe     
    """
    joueur=labyrinthe["player"][0][2]
    labyrinthe['plateau'][0][lig][col]['pion'].append(joueur)

#poserJoueurCourant(laby,0,1)
#print(laby)

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer    
    """    
    return labyrinthe['plateau'][1]

#print(getCarteAJouer(laby))


def coupInterdit(labyrinthe,direction,rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    res=False
    if direction=='N':
        if labyrinthe['interdit']==(rangee,'N'):
            res=True
    if direction=='S':
        if labyrinthe['interdit']==(rangee,'S'):
            res=True
    if direction=='E':
        if labyrinthe['interdit']==(rangee,'E'):
            res=True
    if direction=='O':
        if labyrinthe['interdit']==(rangee,'O'):
            res=True                
    return res

assert(coupInterdit(laby,'O',3))==False
assert(coupInterdit(laby2,'O',3))==True

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    
    if direction=="N" and not coupInterdit(labyrinthe,direction,rangee):
        labyrinthe['interdit']=(rangee,"S")
        labyrinthe['plateau']=(labyrinthe['plateau'][0],(decalageColonneEnHaut(labyrinthe['plateau'][0],rangee,labyrinthe['plateau'][1])))  
    if direction=="S" and not coupInterdit(labyrinthe,direction,rangee):
        labyrinthe['interdit']=(rangee,"N")
        labyrinthe['plateau']=(labyrinthe['plateau'][0],(decalageColonneEnBas(labyrinthe['plateau'][0],rangee,labyrinthe['plateau'][1])))
        
    if direction=="E" and not coupInterdit(labyrinthe,direction,rangee):
        labyrinthe['interdit']=(rangee,"O")
        labyrinthe['plateau']=(labyrinthe['plateau'][0],(decalageLigneADroite(labyrinthe['plateau'][0],rangee,labyrinthe['plateau'][1])))
        
    if direction=="O" and not coupInterdit(labyrinthe,direction,rangee):
        labyrinthe['interdit']=(rangee,"E")
        labyrinthe['plateau']=(labyrinthe['plateau'][0],(decalageLigneAGauche(labyrinthe['plateau'][0],rangee,labyrinthe['plateau'][1])))
    



def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe    
    """
    if sens=='H':
        tournerHoraire(labyrinthe['plateau'][1])
    if sens=='A':
        tournerAntiHoraire(labyrinthe['plateau'][1])

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return labyrinthe['player'][0][1][0]

assert(getTresorCourant(laby))==4 #ça rend 1 car un des assert precedent supprime le 2

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    plateau=labyrinthe["plateau"][0]
    tresor=getTresorCourant(labyrinthe)
    col=0
    lig=0
    for lign in plateau:
        for colo in lign:
            if colo['tresor']==tresor:
                return (col,lig)
            col+=1
        lig+=1

assert(getCoordonneesTresorCourant(laby))==(1,0)


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    joueur=getNumJoueurCourant(labyrinthe)
    plateau=labyrinthe["plateau"][0]
    col=0
    lig=0
    for lign in plateau:
        for colo in lign:
            if colo['pion'][0][0]==joueur:
                return (col,lig)
            col+=1
        lig+=1

assert(getCoordonneesJoueurCourant(laby))==(0,0)

def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    res=4
    if action=='T':
        sens=input("Dans quel sens voulez vous tournez la carte?")
        tournerCarte(labyrinthe,sens)
        res=0
    elif action=='N' or action=='E' or action=='S' or action=='O' and rangee in [1,3,5]:
        if (rangee,action)==labyrinthe["interdit"]:
            res=2
        elif (rangee,action)!=labyrinthe["interdit"]:
            res=1
            jouerCarte(labyrinthe,action,rangee)
    elif type(rangee)==int and type(action)==int:
        res=3
    return res

assert(executerActionPhase1(laby,'E',3))==1
assert(executerActionPhase1(laby2,'O',3))==2
assert(executerActionPhase1(laby,1,2))==3

def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    

def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    res=0
    if getCoordonneesJoueurCourant(labyrinthe)==getCoordonneesTresorCourant(labyrinthe):
        res=1
        joueurCourantTrouveTresor(getListeJoueurs)
        enleverTresor(labyrinthe,getCoordonneesJoueurCourant[1],getCoordonneesJoueurCourant[0],getTresor(carte))
        if joueurCourantAFini(labyrinthe['player']):
            res=2
    changerPhase(labyrinthe)
    return res
print(finirTour(laby))
