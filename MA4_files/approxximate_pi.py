from math import pi
import random
import matplotlib.pyplot as plt

def random_coordinates(n):
    points = []
    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        points.append([x, y])
    return points

def in_circle(points):
    points_in_circle = []
    for point in points:
        if (point[0]**2 + point[1]**2) <= 1:
            points_in_circle.append(point)
    return points_in_circle 

def find_pi(points, points_in_circle):
    return 4*(len(points_in_circle))/len(points)

def get_x(points):
    x = []
    for point in points:
        x.append(point[0])
    return x

def get_y(points):
    y=[]
    for point in points:
        y.append(point[1])
    return y



def main(): 
    for n in [1000, 10000, 100000]:
        points = random_coordinates(n)
        points_in_circle = in_circle(points)
        points_outside_circle = [x for x in points if x not in points_in_circle]

        pi_approx = find_pi(points, points_in_circle)
        print(f"With {n} points, pi as estimated to be {pi_approx}")

        x_out = get_x(points_outside_circle)
        y_out = get_y(points_outside_circle)
        x_in = get_x(points_in_circle)
        y_in = get_y(points_in_circle)

        plt.scatter(x_out, y_out, c = 'blue')
        plt.scatter(x_in, y_in, c = 'red')
        plt.savefig(f'montecarlo_pi_{n}.png')
        #plt.show()



if __name__ == '__main__':
    main()