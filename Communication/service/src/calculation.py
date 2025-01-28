import math
from datetime import datetime


SPEED = 340

def calculate_angle(distance, t1: datetime, t2: datetime):
    ta = distance / SPEED
    if t1 < t2:
        t = t2 - t1
    else:
        t = t1 - t2
    print(t)
    t = t.total_seconds()
    print(t)
    y = math.degrees(((t / ta) * math.pi) / 2)
    return y