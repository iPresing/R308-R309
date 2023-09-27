import math

"""
+------------------+
|      Point       |
+------------------+
| - x: float      |
| - y: float      |
+------------------+
| + __init__(x: float = 0, y: float = 0) |
| + __add__(p: Point) -> Point           |
| + __str__() -> str                     |
| + distance(*args) -> float            |
+------------------+


   |
   |
   |   +------------------+
   |   |      Cercle      |
   |   +------------------+
   |   | - r: float      |
   |   +------------------+
   |   | + __init__(x: float = 0, y: float = 0, r: float = 0) |
   |   | + diametre(*args) -> float      |
   |   | + surface(*args) -> float       |
   |   | + perimeter(*args) -> float     |
   |   | + intersection(*args) -> bool   |
   |   | + appartient(*args) -> bool     |
   |   +------------------+
"""
class Point:
    def __init__(self, x: float =0, y:float =0):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, *args):
        if len(args) == 2:
            x, y = args[0], args[1]
        elif len(args) == 1 and isinstance(args[0], Point):
            x, y = args[0].x, args[0].y
        else:
            return "Problèmes d'arguments"
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
    

class Cercle(Point):
    
    def __init__(self, x: float =0, y:float =0, r:float =0):
        super().__init__(x, y) # appel du constructeur de la classe mère
        self.r = r
        
        
    def diametre(self, *args):
        return args[0].r * 2 \
            if len(args) == 1 and isinstance(args[0], Cercle) \
                else self.r * 2
                
    def surface(self, *args):
        return math.pi * (args[0].r ** 2) \
            if len(args) == 1 and isinstance(args[0], Cercle) \
                else math.pi * (self.r ** 2)
    
    def perimeter(self, *args):
        return 2 * math.pi * args[0].r \
            if len(args) == 1 and isinstance(args[0], Cercle) \
                else 2 * math.pi * self.r
    
    #) une méthode permettant de dire si un autre cercle est en intersection avec celui ci.
    def intersection(self, *args) -> bool:
        if len(args) == 1 and isinstance(args[0], Cercle):
            return self.distance(args[0]) < self.r + args[0].r
        else:
            return "Problèmes d'arguments"
        
    #une méthode permettant de dire si un Point A fait parti du cercle
    def appartient(self, *args) -> bool:
        if len(args) == 1 and isinstance(args[0], Point):
            return self.distance(args[0]) < self.r
        else:
            return "Problèmes d'arguments"


A = Cercle(1, 1, 1)
B = Cercle(2, 2, 5)

class Rectangle(Point):
        
        def __init__(self, x: float =0, y:float =0, longueur:float =1, hauteur:float =1):
            super().__init__(x, y) # appel du constructeur de la classe mère
            self.longueur = longueur
            self.hauteur = hauteur
            
        def __str__(self):
            return f"({self.x}, {self.y}, {self.longueur}, {self.hauteur})"
        
        def surface(self):
            return self.longueur * self.hauteur
        
        def perimeter(self):
            return 2 * (self.longueur + self.hauteur)
        
        def point_bas_gauche(self):
            return Point(self.x, self.y)
        
        def point_bas_droit(self):
            return Point(self.x + self.longueur, self.y)
        
        def point_haut_gauche(self):
            return Point(self.x, self.y + self.hauteur)
        
        def point_haut_droit(self):
            return Point(self.x + self.longueur, self.y + self.hauteur)
        
        def appartient(self, *args):
            if len(args) == 1 and isinstance(args[0], Point):
                return self.x <= args[0].x <= self.x + self.longueur and self.y <= args[0].y <= self.y + self.hauteur
            else:
                return "Problèmes d'arguments"
    