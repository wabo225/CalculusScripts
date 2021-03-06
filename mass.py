from vector import Vector3D as vector

class massiveObject():
    '''object with position velocity and mass'''
    def __init__(self, Position: vector, Velocity: vector, Acceleration: vector, mass: float):
        self.Position =  Position
        self.Velocity = Velocity
        self.Acceleration = Acceleration
        self.mass = mass

    def move(self, newX: float, newY: float, newZ: float):
        self.Position = vector(newX, newY, newZ)

    def changeSpeed(self, newX: float, newY: float, newZ: float):
        self.Velocity = vector(newX, newY, newZ)

    def changeAcceleration(self, newX: float, newY: float, newZ: float):
        self.Acceleration = vector(newX, newY, newZ)

    def progress(self, dt: float):
        a = self.Acceleration
        v = self.Velocity
        x = self.Position
        self.Position = x.add(v.scaleVector(dt))
        self.Velocity = v.add(a.scaleVector(dt))