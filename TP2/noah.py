class Personnage:
    def __init__(self, pseudo: str, niveau: int=1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau


    @property
    def pseudo(self):
        return self.__pseudo
    

    @property
    def niveau(self):
        return self.__niveau
    

    
    @property
    def pv(self):
        return self.__pv
    @pv.setter
    def pv(self, valeur:int):
        self.__pv  = valeur
        
    def soin_pv(self):
        self.__pv = self.niveau
        
    @property
    def initiative(self):
        return self.__initiative
    
    @initiative.setter
    def initiative(self, valeur:int):
        self.__initiative= valeur
    

    
            
    def attaque(self, cible:str):
        if isinstance(cible, Personnage):
            if self.initiative > cible.initiative:
                cible.pv-=self.niveau
                if cible.pv > 0:
                    self.pv-=cible.niveau
            elif self.initiative == cible.initiative:
                self.pv-=cible.niveau
                cible.pv-=self.niveau
            else:
                self.pv-=cible.niveau
                if self.pv > 0:
                    cible.pv-=self.niveau
            
                
    def combat(self, cible: str):
        if isinstance(cible, Personnage):
            while self.pv > 0 or cible.pv > 0:
                self.attaque(cible)

            if cible.pv <= 0:
                print(f'{cible.pseudo} est mort')
            elif self.pv <= 0:
                print(f'{self.pseudo} est mort')



            
class Guerrier(Personnage):
    def __init__(self, pseudo : str , niveau : int=1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 8 + 4
        self.initiative = niveau * 4 + 6
        
        
                        
class Mage(Personnage):
    def __init__(self, pseudo : str , niveau : int=1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        self.__mana = niveau * 5
            
            
            
joueur1 = Guerrier('Guerrier')
joueur2 = Mage('Mage')

joueur2.combat(joueur1)
print(joueur2.pv)
joueur2.soin_pv()
print(joueur2.pv)