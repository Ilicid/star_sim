import math

class gravi:
    def __init__(self) -> None:
        self.G: float =  1 #6.67430 * (10**(-11))
        self.bodies: list = []
        self.QUEUE: list = []
        self.dt: float = 0.02

    def configure(self, SETTING, VALUE):
        match SETTING:
            case "dt":
                self.dt = VALUE
            case "G":
                self.G = VALUE
    
    def appenedBody(self, BODY):
        for b in BODY:
            self.bodies.append(b)

    def scenario(self):
        pass

    def compute(self):
        for body1 in self.bodies:
            POS1 = body1.position
            VELOCITY = body1.velocity

            ax = 0
            ay = 0

            for body2 in self.bodies:
                if body2 is body1:
                    continue

                POS2 = body2.position
                MASS = body2.mass

                dx = POS2[0] - POS1[0]
                dy = POS2[1] - POS1[1]

                dist = math.sqrt(dx**2 + dy**2)

                if dist < 1:
                    continue

                ax += self.G * MASS * dx / dist**3
                ay += self.G * MASS * dy / dist**3

            # update velocity ONCE
            VELOCITY[0] += ax * self.dt
            VELOCITY[1] += ay * self.dt

            #print(VELOCITY[0], VELOCITY[1])
            # update position ONCE
            body1.updatePos(
                VELOCITY[0] * self.dt,
                VELOCITY[1] * self.dt
            )
