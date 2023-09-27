class Personnage:
    def __init__(self, Nom : str, Niveau : int = 1):
        self.__Nom = Nom
        self.__Niveau = Niveau
        self.__Initiative = Niveau
        self.__HealPoint = Niveau
    
    def Degats(self):
        return self.Niveau
        
    @property
    def Nom(self):
        return self.__Nom
        
    @property
    def Niveau(self):
        return self.__Niveau
    
    @property
    def HP(self):
        return self.__HealPoint
    
    @HP.setter
    def HP(self, Value : int):
        self.__HealPoint = Value
        
    @property
    def Initiative(self):
        return self.__Initiative
    
    @Initiative.setter
    def Initiative(self, Value : int):
        self.__Initiative = Value
    
    def HP_heal(self):
        self.__HealPoint = self.Niveau
    
    def attaque(self, Cible : str): 
        if isinstance(Cible, Personnage):
            if Cible.Initiative < self.Initiative:  # Remove parentheses after Initiative
                Cible.HP -= self.Degats()
                if Cible.HP <= 0:
                    pass
                else:
                    self.HP -= Cible.Degats()
            elif Cible.Initiative == self.Initiative:
                Cible.HP -= self.Degats()
                self.HP -= Cible.Degats()
            else:
                self.HP -= Cible.Degats()
                
    def combat(self, Cible : str):
        if isinstance(Cible, Personnage):
            print(f"{self.Nom} = {self.HP}\n{Cible.Nom} = {Cible.HP}", end="\n--\n")
            while self.HP > 0 or Cible.HP > 0:
                HP1, HP2 = self.HP, Cible.HP
                self.attaque(Cible)
                print(f"{self.Nom} = {self.HP} (- {HP1 - self.HP})\n{Cible.Nom} = {Cible.HP} (- {HP2 - Cible.HP})", end="\n--\n")
                if Cible.HP <= 0:
                    print(f"{Cible.Nom} est mort")
                    break
                elif self.HP <= 0:
                    print(f"{self.Nom} est mort")
                    break


class Guerrier(Personnage):
    def __init__(self, Nom : str, Niveau : int = 1):
        super().__init__(Nom, Niveau)
        self.Initiative = Niveau * 4 + 6
        self.HP = Niveau * 8 + 4
        
    def Degats(self):
        return self.Niveau * 2
              
class Mage(Personnage):
    def __init__(self, Nom : str, Niveau : int = 1):
        super().__init__(Nom, Niveau)
        self.Initiative = Niveau * 6 + 4
        self.HP = Niveau * 5 + 10
        self.__mana = Niveau * 5
        
    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, Value : int):
        self.__mana = Value
        
    def Degats(self):
        if self.mana > 0:
            self.mana -= 4 
            return self.Niveau + 3
        else:
            return self.Niveau


"""
class Joueur:
    def __init__(self, Nom : str, NbMaxPerso : int):
        self.__Nom = Nom
        self.__NbMaxPerso = NbMaxPerso
        self.__Perso = []
        
        
    @property
    def Perso(self):
        return [a for a in self.__Perso]
    
    @Perso.setter
    def Perso(self, Value : str):
        self.__Perso.append(Value)
        
    @property
    def NbMaxPerso(self):
        return self.__NbMaxPerso
    
    @NbMaxPerso.setter
    def NbMaxPerso(self, Value : int):
        self.__NbMaxPerso = Value
        
    def ajoutPerso(self, Perso : str):
        if len(self.Perso) < self.NbMaxPerso:
            self.Perso = Perso
        else:
            print("Nombre de personnage max atteint")
            
    def SelectCharOnIndex(self, Index : int):
        try:
            return self.Perso[Index].Nom
        except:
            return "Aucun personnage ne porte cet identifiant.."
    
    def SelectCharOnObject(self, Object : str):
        if isinstance(Object, Personnage) and Object in self.Perso:
            return Object.Nom
        else:
            "Cette instance de personnage est inexistante.."
        
    def SelectCharOnName(self, Name : str):
        for a in self.Perso:
            if a.Nom == Name:
                return a.Nom
        return "Aucun personnage ne porte ce nom.."
"""    
    
            
        
        

perso1 = Guerrier("perso1", 1)
perso2 = Mage("perso2", 1)

perso1.combat(perso2)

Player = Joueur("Player", 2)
Player.ajoutPerso(perso1)
Player.ajoutPerso(perso2)

#print(Player.SelectCharOnName("perso2"))

Player.DeleteCharOnIndex(1)
print(Player.SelectCharOnIndex(1))

#print(Player.Perso)


#print(perso2.__dict__)



# __dict__ is a dictionary containing the class's namespace.


