import math

class Vector3D():
    """useful storage container for three dimensional vectors"""
    def __init__ (self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        pass
    def toList(self) -> tuple:
        return (self.x, self.y, self.z)
    
    def negate(self):
        return self.scaleVector(-1)

    def heading(self) -> float:
        return math.atan(self.y/self.x)

    def Magnitude(self) -> float:
        return math.sqrt((self.x*self.x) + (self.y*self.y)+ (self.z*self.z))

    def unitVector(self):
        '''returns a vector of length one in the direction of this vector'''
        m = self.Magnitude()
        return self.scaleVector(1/m)

    def angleBetween(self, vector) -> float:
        '''returns a radian measure of the angle between two variables measured from this to the given'''
        return(math.acos(self.dot(vector)/(self.Magnitude() * vector.Magnitude())))
    
    def interpolate(self, r):
        v = self.subtract(r)
        return lambda time : self.add(v.scaleVector(time))

    def projectToPlane(self, camera, plane) -> tuple: 
        lerp = camera.interpolate(self)
        v = camera.subtract(self)
        t = -camera.x/v.x
        lerp(t)
        return lerp(t)

    def proj(self, vector):
        '''the projection of vector onto self'''
        projection = self.dot(vector)
        projection = projection/(self.Magnitude()**2)
        projection = self.scaleVector(projection)
        return projection

    def orth(self, vector):
        '''the othagonal projection of b onto a'''
        return self.add(vector.proj(self).scaleVector(-1))
    def add(self, vector):
        #add two 3D Vectors
        #returns a Vector
        i = self.x + vector.x
        j = self.y + vector.y
        k = self.z + vector.z
        return Vector3D(i, j, k)

    def subtract(self, vector):
        return self.add(vector.negate())

    def scaleVector(self, scalar):
        #U_vector * q
        i = self.x * scalar
        j = self.y * scalar
        k = self.z * scalar
        return Vector3D(i, j, k)

    def dot(self, vector):
        '''returns the dot product of two vectors'''
        return self.x*vector.x + self.y*vector.y + self.z*vector.z

    def tripleScalarProduct(self, vector1, vector2):
        return self.cross(vector1).dot(vector2)

    def cross(self, vector):
        i = self.y * vector.z - self.z * vector.y
        j = self.z * vector.x - self.x * vector.z
        k = self.x * vector.y - self.y * vector.x
        return Vector3D(i, j, k)
    def printAll(self) -> None:
        print(round(self.x, 3),'i + (',round(self.y, 3),')j + (',round(self.z, 3),')k', sep='')
        pass