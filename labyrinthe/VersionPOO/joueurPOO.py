class Joueur(object):


    def __init__(self,nom):
        """
        creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
        paramètre: nom une chaine de caractères
        retourne le joueur ainsi créé
        """
        self.Player=(nom,[3,4],[0]) #à l'indice 1,on a la liste d'objet. A l'indice 2, on a le numéro du joueur


    def ajouterTresor(self,tresor):
        """
        ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
        paramètres:
            joueur le joueur à modifier
            tresor un entier strictement positif
            la fonction ne retourne rien mais modifie le joueur
        """
        self.Player[1].append(tresor)
    
    def prochainTresor(self):
        """
        retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
        paramètre:
            joueur le joueur
        résultat un entier représentant le trésor ou None
        """
        if self.Player[1]!=[]:
            return self.Player[1][0]
        else:
            return None
    
    def tresorTrouve(self):
        """ 
        enleve le premier trésor à trouver car le joueur l'a trouvé
        paramètre:
            joueur le joueur
        la fonction ne retourne rien mais modifie le joueur
        """
        del self.Player[1][0]


    def getNbTresorsRestants(self):
        """
        retourne le nombre de trésors qui reste à trouver
        paramètre: joueur le joueur
        résultat: le nombre de trésors attribués au joueur
        """
        return len(self.Player[1])
    

    def getNom(self):
        """
        retourne le nom du joueur
        paramètre: joueur le joueur
        résultat: le nom du joueur 
        """
        return self.Player[0]

Test=Joueur("michel")
assert(Test.prochainTresor())==3
assert(Test.getNbTresorsRestants())==2
assert(Test.getNom())=="michel"
