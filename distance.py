# import re

# def CSVtoList(CSVstring):
#     m = re.match(r"(\d+)+", CSVstring)
#     myList = m.groups()
#     return(myList)

# csv = str(input())
# print(CSVtoList(csv))

print("A:")
ax = int(input("x: "))
ay = int(input("y: "))
az = int(input("z: "))

print("B:")
bx = int(input("x: "))
by = int(input("y: "))
bz = int(input("z: "))

distance = ((ax - bx)**2 + (ay-by)**2 + (az - bz)**2)**.5

print(distance)