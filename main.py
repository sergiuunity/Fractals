from turtle import *


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


def exec_one_tree():
    n = int(input("Enter the number of levels:\n"))
    left(90)
    tree(100, 30, n)


def exec_multiple_trees():
    n = int(input("Enter the number of levels:\n"))
    for i in range(8):
        left(45)
        tree(100, 30, n)


def koch_snowflake_side():
    return


def koch_snowflake(size, level, total):
    if level == 0:
        right(60)
        forward(size)
        return

    forward(size / (3 ** (total - level)))
    left(60)
    koch_snowflake(size, level - 1, total)
    forward(size / (3 ** (total - level)))

    right(120)
    forward(size / (3 ** (total - level)))
    left(60)
    koch_snowflake(size, level - 1, total)
    forward(size / (3 ** (total - level)))

    # if level == total:
    #    right(120)
#     forward(size * 3)
#      left(60)
#       koch_snowflake(size / 3, level - 1, False)
#        forward(size * 3)


def exec_koch_snowflake():
    # n = int(input("Enter the number of levels:\n"))
    n = 2
    left(60)
    koch_snowflake(30, n, n)


def spiral_inner(size, sides, level):
    if level == 0:
        return
    forward(size)
    right(360 / sides)
    spiral_inner(size * 0.99, sides, level - 1)


def exec_spiral_inner():
    sides = int(input("Enter the number of sides:\n"))
    n = int(input("Enter the number of levels:\n"))
    spiral_inner(300, sides, n)


def spiral_outer(size, sides, level):
    if level == 0 or size > 10000:
        return
    forward(size)
    right(360 / sides)
    spiral_outer(size * 1.01, sides, level - 1)


def exec_spiral_outer():
    sides = int(input("Enter the number of sides:\n"))
    n = int(input("Enter the number of levels:\n"))
    spiral_outer(1, sides, n)


shape("classic")
speed(0)

# exec_trees()
# exec_koch_snowflake()
# exec_one_tree()
# exec_spiral_inner()
exec_spiral_outer()

mainloop()
