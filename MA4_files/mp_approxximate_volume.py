import random
import concurrent.futures as future
from time import perf_counter as pc

def approximate_volume(n,d):
    points = [[random.uniform(-1,1) for _ in range(d)] for _ in range(n)] 
    points_squared_sum = [sum(list(map(lambda x : x**2, row))) for row in points]
    n_points_inside = 0

    for point in points_squared_sum:
        if point <= 1:
            n_points_inside += 1

    volume = (2**d) * (n_points_inside/n) 
    return volume




if __name__ == "__main__":

    start = pc()
    with future.ProcessPoolExecutor() as ex:
        n = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]
        d = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
        results = ex.map(approximate_volume, n, d)

        #print(sum(results))
    
    end = pc()
    print(f"Using multiprocessing took {round(end-start, 2)} seconds")

    start2 = pc()
    approximate_volume(10000000, 11)
    end2 = pc()
    print(f"Not using multiprocessing took {round(end2-start2, 2)} seconds")


"""Using multiprocessing took 69.25 seconds
Not using multiprocessing took 209.27 seconds"""


 