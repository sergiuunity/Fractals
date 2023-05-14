from turtle import *


def exec_trees():
    n = int(input("Enter the number of levels:\n"))
    for i in range(8):
        left(45)
        tree(100, 30, n)


def tree(size, angle, level):
    if level == 0:
        color("blue")
        dot(size)
        color("black")
        return
    forward(size)

    left(angle)
    tree(size * 0.6, angle, level - 1)

    right(angle * 2)
    tree(size * 0.6, angle, level - 1)

    left(angle)
    backward(size)


shape("classic")
speed(1)

exec_trees()

# exec_koch_snowflake()


mainloop()
