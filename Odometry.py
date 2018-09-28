from math import cos
import matplotlib

def advance():
    theta = theta + dtheta/dt
    dx = (l/2)*(Wr + Wl)*cos(theta)
    dy = (l/2)*(Wr + Wl)*sin(theta)
    x = x + dx/dt
    y = y + dy/dt
    t += dt

t = 0

while t < 10:
    dt = 1
    l = 10
    Wr = RightEncoderSpeed
    Wl = LeftEncoderSpeed
    dtheta = (l/1)*(Wr - Wl)
    theta = 0
    x = 0
    y = 0
