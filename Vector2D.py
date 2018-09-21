class Vector2D():
    """storage container for two dimensional vectors"""
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

    def add(self, vector):
        i = self.x + vector.x
        j = self.y + vector.y
        return Vector2D(i, j)

    def scaleVector(self, scalar):
        #U_vector * q
        i = self.x * scalar
        j = self.y * scalar
        return Vector2D(i, j)

    def unitVector(self):
        '''returns a vector of length one in the direction of this vector'''
        m = self.Magnitude()
        return self.scaleVector(1/m)

    def dot(self, vector):
        product = self.x * vector.x * math.cos(self.heading() - vector.heading())
        return product

    def cross(self, vector):
        k = self.x * vector.y - self.y * vector.x
        return k

    def lerp(self, vector, target):
        #linear interpolation between two vector endpoints. Solves at target.
        return (((self.y - vector.y)/(self.x-vector.x))*(target - self.x) + self.y)

    def heading(self):
        return math.atan(self.y/self.x)

    def Magnitude(self):
        return math.sqrt((self.x*self.x) + (self.y*self.y))
    
    def printAll(self):
        print(self.x,'i + (',self.y,')j')