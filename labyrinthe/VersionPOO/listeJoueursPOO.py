import random
from joueur import *

class listeJoueur(object):
    
    def __init__(self,joueur):
        self.listePlayer=[]
        for player in joueur:
            self.listePlayer.append(Joueur(player))
    
    def ajouterJoueur(self, joueur):
        """
        ajoute un nouveau joueur à la fin de la liste
        paramètres: self.listePlayer un liste de self.listePlayer
                    joueur le joueur à ajouter
        cette fonction ne retourne rien mais modifie la liste des self.listePlayer
        """
        self.listePlayer.append(joueur)

    def initAleatoireJoueurCourant(self):
        """
        tire au sort le joueur courant
        paramètre: self.listePlayer un liste de self.listePlayer
        cette fonction ne retourne rien mais modifie la liste des self.listePlayer
        """
        random.shuffle(self.listePlayer)
        e=0
        for i in range(len(self.listePlayer)):
            self.listePlayer[i][2][0]=e
            e=e+1
        
    def distribuerTresors(self,nbTresors=24,nbTresorMax=0):
        """
        distribue de manière aléatoire des trésors entre les self.listePlayer.
        paramètres: self.listePlayer la liste des self.listePlayer
                    nbTresors le nombre total de trésors à distribuer (on rappelle 
                            que les trésors sont des entiers de 1 à nbTresors)
                    nbTresorsMax un entier fixant le nombre maximum de trésor 
                                qu'un joueur aura après la distribution
                                si ce paramètre vaut 0 on distribue le maximum
                                de trésor possible  
        cette fonction ne retourne rien mais modifie la liste des self.listePlayer
        """
        listeTresor=[x for x in range(nbTresors)]
        random.shuffle(listeTresor)
        nbDist=len(listeTresor)//len(self.listePlayer)
        e=0
        for i in range(0,len(listeTresor),len(self.listePlayer)):
            for joueur in self.listePlayer:
                joueur[1].append(listeTresor[e])
                e=e+1
        
    def changerJoueurCourant(self):
        """
        passe au joueur suivant (change le joueur courant donc)
        paramètres: self.listePlayer la liste des self.listePlayer
        cette fonction ne retourne rien mais modifie la liste des self.listePlayer
        """   
        for i in range(len(self.listePlayer)):
            if i==0:
                listAv0=self.listePlayer[len(self.listePlayer)-1]
                self.listePlayer[len(self.listePlayer)-1]=self.listePlayer[0]
            if i>0 and i<(len(self.listePlayer)-1):
                self.listePlayer[i-1]=self.listePlayer[i]
        self.listePlayer[len(self.listePlayer)-2]=listAv0
        

    def getNbJoueur(self):
        """
        retourne le nombre de self.listePlayer participant à la partie
        paramètre: self.listePlayer la liste des self.listePlayer
        résultat: le nombre de self.listePlayer de la partie
        """
        return len(self.listePlayer)

    def getJoueurCourant(self):
        """
        retourne le joueur courant
        paramètre: self.listePlayer la liste des self.listePlayer
        cette fonction ne retourne rien mais modifie la liste des self.listePlayer
        """
        return self.listePlayer[0]

    def joueurCourantTrouveTresor(self):
        """
        Met à jour le joueur courant lorsqu'il a trouvé un trésor
        c-à-d enlève le trésor de sa liste de trésors à trouver
        paramètre: self.listePlayer la liste des self.listePlayer
        cette fonction ne retourne rien mais modifie la liste des self.listePlayer
        """
        del self.listePlayer[0][1][0]

    def nbTresorsRestantsJoueur(self,numJoueur):
        """
        retourne le nombre de trésor restant pour le joueur dont le numero 
        est donné en paramètre
        paramètres: self.listePlayer la liste des self.listePlayer
                    numJoueur le numéro du joueur
        résultat: le nombre de trésors que joueur numJoueur doit encore trouver
        """
        for joueur in self.listePlayer:
            if joueur[2][0]==numJoueur:
                return len(joueur[1])


    def numJoueurCourant(self):
        """
        retourne le numéro du joueur courant
        paramètre: self.listePlayer la liste des self.listePlayer
        résultat: le numéro du joueur courant
        """
        return self.listePlayer[0][2][0]

    def nomJoueurCourant(self):
        """
        retourne le nom du joueur courant
        paramètre: self.listePlayer la liste des self.listePlayer
        résultat: le nom du joueur courant
        """
        return self.listePlayer[0][0]
    
    def nomJoueur(self,numJoueur):
        """
        retourne le nom du joueur dont le numero est donné en paramètre
        paramètres: self.listePlayer la liste des self.listePlayer
                    numJoueur le numéro du joueur    
        résultat: le nom du joueur numJoueur
        """
        for joueur in self.listePlayer:
            if joueur[2][0]==numJoueur:
                return joueur[0]
        

    def prochainTresorJoueur(self,numJoueur):
        """
        retourne le trésor courant du joueur dont le numero est donné en paramètre
        paramètres: self.listePlayer la liste des self.listePlayer
                    numJoueur le numéro du joueur    
        résultat: le prochain trésor du joueur numJoueur (un entier)
        """
        for joueur in self.listePlayer:
            if joueur[2][0]==numJoueur:
                return joueur[1][0]
   

        

    def tresorCourant(self):
        """
        retourne le trésor courant du joueur courant
        paramètre: self.listePlayer la liste des self.listePlayer 
        résultat: le prochain trésor du joueur courant (un entier)
        """
        return self.listePlayer[0][1][0]
    
    def joueurCourantAFini(self):
        """
        indique si le joueur courant a gagné
        paramètre: self.listePlayer la liste des self.listePlayer 
        résultat: un booleen indiquant si le joueur courant a fini
        """
        res=False
        if self.listePlayer[0][1] == []:
            res=True
        return res

Test=listeJoueur(["michel","jacques","paul"])

assert(Test.getNbJoueur())==3


    