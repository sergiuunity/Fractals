from turtle import *
from sierpinski_triangle import *


# generates a tree from the starting point with the given size, angle and going the given number of levels deep
def tree(size, angle, level):
    if level == 0:
        color("blue")
        dot(size)
        color("black")
        return
    forward(size)

    right(angle)
    tree(size * 0.6, angle, level - 1)

    left(angle * 2)
    tree(size * 0.6, angle, level - 1)

    right(angle)
    backward(size)


# reads the needed data and generates a tree with that information
def exec_one_tree():
    n = int(input("Enter the number of levels:\n"))
    left(90)
    tree(200, 30, n)


# reads the needed data and generates with that information multiple trees that form a flower pattern
def exec_multiple_trees_flower():
    n = int(input("Enter the number of levels:\n"))
    for i in range(8):
        left(45)
        tree(100, 30, n)


# generates a spiral going from the outside to the inside with the given amount of sides and the given number of levels
def spiral_inner(size, sides, level):
    if level == 0:
        return
    forward(size)
    right(360 / sides)
    spiral_inner(size * 0.99, sides, level - 1)


# reads the needed data and generates an inner spiral with that information
def exec_spiral_inner():
    sides = int(input("Enter the number of sides:\n"))
    n = int(input("Enter the number of levels:\n"))
    spiral_inner(30, sides, n)


# generates a spiral going from the outside to the inside with the given amount of sides and the given number of levels
def spiral_outer(size, sides, level):
    if level == 0 or size > 10000:
        return
    forward(size)
    right(360 / sides)
    spiral_outer(size * 1.01, sides, level - 1)


# reads the needed data and generates an outer spiral with that information
def exec_spiral_outer():
    sides = int(input("Enter the number of sides:\n"))
    n = int(input("Enter the number of levels:\n"))
    spiral_outer(1, sides, n)


# generates a koch snowflake with the given number of sides, the given size of a side and going the given number of
# levels deep
def koch_snowflake(size, sides, level):
    for i in range(sides):
        koch_snowflake_side(size, sides, level)
        right(360 / sides)


# generates a side of a koch snowflake
def koch_snowflake_side(size, sides, level):
    if level == 0:
        forward(size)
        return
    koch_snowflake_side(size / 3, sides, level - 1)
    left(180 / sides)
    koch_snowflake_side(size / 3, sides, level - 1)
    right(360 / sides)
    koch_snowflake_side(size / 3, sides, level - 1)
    left(180 / sides)
    koch_snowflake_side(size / 3, sides, level - 1)


# reads the needed data and generates a koch snowflake with that information
def exec_koch_snowflake():
    sides = int(input("Enter the number of sides:\n"))
    n = int(input("Enter the number of levels:\n"))
    # left(180 / sides)
    koch_snowflake(200, sides, n)


# shape("classic")
# speed(0)

# Uncomment one of the following lines to display different shapes

# exec_multiple_trees_flower()
# exec_one_tree()
# exec_spiral_inner()
# exec_spiral_outer()
# exec_koch_snowflake()

# turtle.reset()

# mainloop()

n = int(input("Give number:\n"))
generate_sierpinski_triangle(n)
