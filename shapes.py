from vector import Vector3D
from matrix import matrix
# class point():
#     def __init__(self, x: float, y: float, z: float):
#         self.x, self.y, self.z = x, y, z
    
#     def printall(self):
#         print("(", self.x, " , ", self.y, " , ", self.z, ')', sep='')
    
#     def toList(self):
#         return (self.x, self.y, self.z)

#     def constructLine(self, vectorObject: type(Vector3D)):
#         return line(Vector3D(self.x, self.y, self.z), vectorObject)

Point = {x: 0, y: 0, z: 0}

class line():
    def __init__(self, R0: dict, Ve: Vector3D):
        self.R0, self.Ve = R0, Ve
        self.eq = lambda time : return (Ve.x + + Ve.y Ve.z, Ve.dot(R0))
    
    def printall(self):
        print("R = R0 + V(t)")
        print()
        print(str(self.R0.toList()), ' + ', self.Ve.toList(), '(t)', sep='')
        pass

    def evaluate(self, t: float):
        R = self.R0.add(self.Ve.scaleVector(t))
        return R

    def intersect(self, line2: line, line3: line):
        return matrix([self.eq, line2.eq, line3.eq]).gauss()

class plane():
    def __init__(self, N: Vector3D, P: Vector3D) -> None:
        self.N, self.P = N, P
        pass

    def intersectLine(self, line: function):

