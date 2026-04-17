import math

class gravi:
    def __init__(self, M1, M2) -> None:
        self.G: float = 6.67430 * (10**-11)
        self.m1: int = M1 # solar mass
        self.m2: int = M2 # planatry mass
    
    def acceleration(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        dist = math.sqrt(dx**2 + dy**2)

        if dist == 0:
            return (0, 0)

        Rn = (dx / dist, dy / dist)

        a = (self.G * self.m1) / (dist ** 2)

        movement = (Rn[0] * a, Rn[1] * a)

        return movement