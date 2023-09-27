# classe personnage

class Personnage():
    
    def __init__(self, Pseudo : str, Niveau : int = 1):
             
        self.__Pseudo = Pseudo
        self.__Niveau = Niveau
        
    
    def HP(self, HealLevel : int):
        self.__HealLevel = HealLevel
        
        
    @property
    def Niveau(self):
        return self.__Niveau
    def GetHP(self):
        return self.__HealLevel
    
    
    @GetHP.setter
        
    def attaque(self, Cible : str):
        hp_cible, init_cible = Cible.Niveau
        hp_self, init_self = self.Niveau
        if isinstance(Cible, Personnage):
            if Cible.Niveau == self.Niveau 
        


        