from vector import Vector3D

def interpolate(r0: Vector3D, t1: float, r: Vector3D, t2: float):
    deltaT = t2 - t1
    v = r.subtract(r0).scaleVector(1/deltaT)
    r0 = Vector3D(r0.x - v.x*t1, r0.y - v.y*t1, r0.z - v.z*t1)
    return lambda time : r0.add(v.scaleVector(time))

a = interpolate( Vector3D(0, 0, 0), 1, Vector3D(1, 1, 1), 3)

a(2).printAll()