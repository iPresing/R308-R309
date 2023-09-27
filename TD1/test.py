def superior(a : int, b : int) -> int:
    """
    Cette fonction retourne le plus grand des deux nombres passés en paramètre."""
    return a if a > b else b


def test_seuil(a: int, seuil : int = 10) -> str:
    """
    Cette fonction retourne True si a est supérieur au seuil passé en paramètre, False sinon."""
    return "Valeur supérieur au seuil {}".format(seuil) if a > seuil else "Valeur inférieur ou égale au seuil {}".format(seuil)

def max_of_list(liste : list) -> int:
    """
    Cette fonction retourne le plus grand nombre d'une liste de nombres."""
    return max(liste)

def liste_sup_seuil(liste : list, seuil : int = 3) -> list:
    """
    Cette fonction retourne le nomvre de valeurs supérieures au seuil passé en paramètre."""
    return len([x for x in liste if x > seuil]) # compréhension de liste

def ensemble_donnée(chaine: str, dictionnaire : dict) -> str:
    
    return print(chaine , dictionnaire)

a : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b : dict = {"a": 1, "b": 2, "c": 3, "d": 4}

#print(ensemble_donnée("test", b))

class Tasse:
    matiere : str = "céramique"
    
    def __init__(self, couleur : str, contenance : float, marque : str) -> None:
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
        
    # méthode qui permet de définir le contenu comme un nouvel attribut d'instance
    def remplir(self, contenu : str) -> None:
        self.contenu = contenu
        
    def __del__(self) -> None:
        if hasattr(self, 'contenu'):
            del self.contenu
    
    
    def __str__(self) -> str:
        return "la tasse de matière {}, de couleur {} et de la marque {} a une contenance de {} ml".format(self.matiere, self.couleur, self.marque, self.contenance)
    
    
plot = Tasse("Bleur", 50, "duralex")
print(plot)



