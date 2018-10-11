from vector import Vector3D as vector
import matplotlib.pyplot as pt
import numpy as np


class mass():
	def __init__(self, Position: vector, Velocity: vector, Acceleration: vector):
		self.Position =  Position
		self.Velocity = Velocity
		self.Acceleration = Acceleration

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

x_0 = vector(0,1,0)
v_0 = vector(0,0,0)
a = vector(1, 0, 0)

o = mass(x_0,v_0, a)

pvtx = []
pvty = []
t = 0
while t < 2:
	pvtx.append(o.Position.x)
	pvty.append(o.Position.y)
	o.progress(0.1)
	t += 0.1 

pt.plot(pvtx, pvty)
pt.show()
