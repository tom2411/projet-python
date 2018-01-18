def Joueur(nom):
    """
    creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
    paramètre: nom une chaine de caractères
    retourne le joueur ainsi créé
    """
    objets=[]
    Joueur=(nom,objets,[0])
    return Joueur
assert(Joueur("michel"))==("michel",[],[0])

def ajouterTresor(joueur,tresor):
    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
        joueur le joueur à modifier
        tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """
    joueur[1].append(tresor)

def prochainTresor(joueur):
    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
        joueur le joueur
    résultat un entier représentant le trésor ou None
    """
    if joueur[1]!=[]:
        return joueur[1][0]
    else:
        return None
assert(prochainTresor(("michel",[2,3,4,5],[0])))==2
assert(prochainTresor(("michel",[],[0])))==None

def tresorTrouve(joueur):
    """
    enleve le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """
    del joueur[1][0]
    #print(joueur)
tresorTrouve(("michel",[1,2,3],[0]))

def getNbTresorsRestants(joueur):
    """
    retourne le nombre de trésors qui reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """
    return len(joueur[1])
assert(getNbTresorsRestants(("michel",[1,2,3,4],[0])))==4

def getNom(joueur):
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur
    """
    return joueur[0]
assert(getNom(("michel",[1,2,3],[0])))=="michel"
