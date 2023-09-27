def affiche(string : str) -> str:
    return print("texte à afficher: ",string)

class Velo:
    vitesse_courante : int = 1
    def __init__(self, marque: str, taille : int, couleur : str, nbrdevitesses: int) -> None:
        self.marque = marque
        self.taille = taille
        self.couleur = couleur
        self.nbrdevitesses = nbrdevitesses
        
        
    def gear_up(self, up: int) -> None:
        self.vitesse_courante += up if (self.vitesse_courante < self.nbrdevitesses and self.vitesse_courante != 0) else self.vitesse_courante
        return print(f" la vitesse actuelle est de {self.vitesse_courante}")
    
    def gear_down(self, down: int) -> None:
        self.vitesse_courante -= down if (self.vitesse_courante > 1 and self.vitesse_courante != 0) else self.vitesse_courante
        return print(f" la vitesse actuelle est de {self.vitesse_courante}")
    
    

def run():
    str1: str = input("entrez une chaine : ")
    affiche(str1)
    v1 = Velo("BMW", 16, "rouge", 10)
    v1.gear_up(2)
    v1.gear_down(1)

if __name__ == '__main__':
    run()