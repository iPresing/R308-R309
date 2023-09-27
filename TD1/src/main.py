def affiche(string: str) -> str:
    """
    Affiche le texte passé en argument.

    :param string: Le texte à afficher.
    :type string: str
    :return: Le texte affiché.
    :rtype: str
    """
    return print("texte à afficher: ", string)

class Velo:
    """
    Classe représentant un vélo.
    """

    vitesse_courante: int = 1

    def __init__(self, marque: str, taille: int, couleur: str, nbrdevitesses: int) -> None:
        """
        Initialise une instance de la classe Velo.

        :param marque: La marque du vélo.
        :type marque: str
        :param taille: La taille du vélo.
        :type taille: int
        :param couleur: La couleur du vélo.
        :type couleur: str
        :param nbrdevitesses: Le nombre de vitesses du vélo.
        :type nbrdevitesses: int
        """
        self.marque = marque
        self.taille = taille
        self.couleur = couleur
        self.nbrdevitesses = nbrdevitesses

    def gear_up(self, up: int) -> str:
        """
        Augmente la vitesse du vélo.

        :param up: Le nombre de vitesses à augmenter.
        :type up: int
        :return: None
        :rtype: None
        """
        self.vitesse_courante += up \
            if (self.vitesse_courante <= self.nbrdevitesses and self.vitesse_courante <= 1) \
                else self.vitesse_courante
        return print(f" la vitesse actuelle est de {self.vitesse_courante}")

    def gear_down(self, down: int) -> str:
        """
        Diminue la vitesse du vélo.

        :param down: Le nombre de vitesses à diminuer.
        :type down: int
        :return: None
        :rtype: None
        """
        self.vitesse_courante -= down \
            if (self.vitesse_courante >= 1 and self.vitesse_courante <= 1)\
                else self.vitesse_courante
        return print(f" la vitesse actuelle est de {self.vitesse_courante}")


def run():
    """
    Fonction principale du programme.
    """
    str1: str = input("entrez une chaine : ")
    affiche(str1)
    v1 = Velo("BMW", 16, "rouge", 10)
    v1.gear_up(2)
    v1.gear_down(1)


if __name__ == '__main__':
    run()