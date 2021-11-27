class Maillon :
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class ListeChainee :
    def __init__(self) :
        self.premier = None

    #methode qui permet d'inserer un nouveau maillon dans la liste chainee
    def insert(self, valeur):
        nouveauMaillon = Maillon(valeur)
        if (self.premier):
            courant = self.premier
            while (courant.suivant):
                courant = courant.suivant
            courant.suivant = nouveauMaillon
        else :
            self.premier = nouveauMaillon

    #methode qui permet d'afficher la liste chainee
    def printListe (self):
        courant = self.premier
        while (courant):
            print (courant.valeur)
            courant = courant.suivant
    
    #methode qui permet de compter le nombre de maillon qui existe
    #cela revient a dire qu'on donne la longueur de la liste chainee
    def longueurListe (self):
        courant = self.premier
        compteur = 0
        while (courant) :
            compteur += 1
            courant = courant.suivant
        return compteur

    #methode qui permet d'inverser la liste chainee
    def reverseListe (self):
        precedent = None
        courant = self.premier
        while (courant is not None):
            suivant = courant.suivant
            courant.suivant = precedent
            precedent = courant
            courant = suivant
        self.premier = precedent

'''
test creation d'un maillon

premier = Maillon(3)
print(premier.valeur)
'''

'''
test creation d'une liste chainee
on ajoute un maillon dans une liste

LC = ListeChainee()
LC.premier = Maillon(3)
print(LC.premier.valeur)
'''

#test insertion des nouveaux maillons 

LC = ListeChainee ()
LC.insert(1)
LC.insert(2)
LC.insert(3)
LC.insert(4)
LC.insert(5)

#test d'affichage de la liste chainee

print("Liste Chainee :")
LC.printListe()
print("Liste Chainee reversed :")
LC.reverseListe()
print "Cette liste chainee a de longueur", LC.longueurListe()
