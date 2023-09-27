class Pokemon:

    def __init__(self, name: str, poids: int):
        self.__name = name
        self.__poids = poids

    @property
    def poids(self) -> int:
        return self.__poids
    @property
    def name(self) -> str:
        return self.__name

class Terre(Pokemon):

    def __init__(self, name: str, poids: int, nb_pattes: int, taille: float):
        super().__init__(name, poids)
        self.__nb_pattes = nb_pattes
        self.__taille = taille

    @property
    def nb_pattes(self) -> int:
        return self.__nb_pattes
    @nb_pattes.setter
    def nb_pattes(self, nb_pattes):
        self.__nb_pattes = nb_pattes

    @property
    def taille(self) -> float:
        return self.__taille
    @taille.setter
    def taille(self, taille):
        self.__taille = taille

    """ @property
    def poids(self) -> int:
        return self.__poids
    @property
    def name(self) -> str:
        return self.__name """

"""     def vitesse(self) -> float:
        return self.nb_pattes * self.taille * 3 """

    """ def __str__(self):
        return f"Je suis le pokémon {self.name} mon poids est {self.poids}kg, \ 
        ma vitesse est de {self.vitesse()}km/h j'ai {self.nb_pattes} pattes, ma taille est de {self.taille}m" """

class Eau(Pokemon):
    def __init__(self, name: str, poids: int, nb_nage: int):
        super().__init__(name, poids)
        self.__nb_nage = nb_nage

    @property
    def nb_nage(self) -> int:
        return self.__nb_nage
    @nb_nage.setter
    def nb_nage(self, nb_nage):
        self.__nb_nage = nb_nage
    


class Mer(Eau):
    def __init__(self, name: str, poids: int, nb_nage: int):
        super().__init__(name, poids, nb_nage)

    def vitesse(self) -> float:
        return (self.poids/25) * self.nb_nage


class Riviere(Eau):
    def __init__(self, name: str, poids: int, nb_nage: int):
        super().__init__(name, poids, nb_nage)

    def vitesse(self) -> float:
        return ((self.poids/25) * self.nb_nage)/2


class Sportif(Terre):