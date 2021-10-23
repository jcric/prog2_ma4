import random
import math
import numpy as np


def approximate_volume(n,d):
    #points = np.random.uniform(low=-1, high=1, size=(n,d))
    points = [[random.uniform(-1,1) for _ in range(d)] for _ in range(n)] 
    points_squared_sum = [sum(list(map(lambda x : x**2, row))) for row in points]
    n_points_inside = 0

    for point in points_squared_sum:
        if point <= 1:
            n_points_inside += 1

    volume = (2**d) * (n_points_inside/n) 
    return volume


def calculate_volume(d):
    volume = ((math.pi) ** (d/2)) / (math.gamma(d/2 +1))
    return volume



n, d = 100000, 11
print(f"Actual volume: {calculate_volume(d)}. Approximated volume: {approximate_volume(n,d)}")
n, d = 100000, 2
print(f"Actual volume: {calculate_volume(d)}. Approximated volume: {approximate_volume(n,d)}")




