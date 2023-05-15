import matplotlib.pyplot as plt
import random
import time


def generate_sierpinski_triangle(level):
    vertices_x = [1, 3, 5]
    vertices_y = [2, 5, 2]

    x = []
    y = []

    # first point
    last_x = 3.5
    last_y = 2.5

    plt.plot(vertices_x, vertices_y, color='none', linestyle='dashed', linewidth=2, marker='o', markersize=6,
             markerfacecolor='blue', markeredgecolor='blue')



    for i in range(level):
        next_option = random.randint(0, 2)
        last_x = (last_x + vertices_x[next_option]) / 2
        last_y = (last_y + vertices_y[next_option]) / 2
        x.append(last_x)
        y.append(last_y)

    plt.plot(x, y, color='none', linestyle='dashed', linewidth=2, marker='o', markersize=2,
             markerfacecolor='red', markeredgecolor='red')

    plt.show()
    # plt.grid()
