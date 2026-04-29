import math

class gravi:
    def __init__(self, M1: float, M2: float) -> None:
        self.G: float = 6.67430 * (10**-11)
        self.bodies: list[tuple[tuple[int,int],float]] = [] # holds position and mass
    
    def appendBody(self, BODY):
        self.bodies.append(BODY)
        
    def removeBody(self, BODY):
        self.bodies.remove(BODY)
    
    def acceleration(self):
        total_effect: float = 0.0

        for b in self.bodies:
            pass