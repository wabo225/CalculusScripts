from vector import Vector3D
# from shapes import plane, line

Zero = Vector3D(0, 0, 0)
i = Vector3D(1, 0, 0)
j = Vector3D(0, 1, 0)
k = Vector3D(0, 0, 1)
if k.toList() == i.cross(j).toList():
    print(k.toList())
