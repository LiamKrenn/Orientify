import math
from datetime import datetime


SPEED = 340000000


def calculate_timestamps(microphone1: list, microphone2: list):
    max1 = max(microphone1)
    max2 = max(microphone2)

    t1 = microphone1.index(max1) * 22.1
    t2 = microphone2.index(max2) * 22.1

    return t1, t2

def calculate_angle(distance, t1, t2):
    ta = distance / SPEED
    if t1 < t2:
        t = t2 - t1
    else:
        t = t1 - t2
    y = math.degrees(((t / ta) * math.pi) / 2)
    return y


if __name__ == "__main__":
    print(calculate_angle(0.3, datetime(2024, 12, 17, 10, 0, 0, 0), datetime(2024, 12, 17, 10, 0, 0, 500)))