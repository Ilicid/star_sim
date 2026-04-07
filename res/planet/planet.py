class Planet():
    def __init__(self) -> None:
        self.radius: int
        self.density: int # or mass idk
        self.angle: int # the offset from the star that the velocity is aplied, 0 and 360 would be into the star
        self.velocity: int # the start speed of the planet

        self.position: tuple[int,int]
        self.color: int

    def setPrams(self, radius, density, angle, velocity, position, color) -> None:
        self.radius = radius
        self.density = density
        self.angle = angle
        self.velocity = velocity

        self.position = position
        self.color = color
