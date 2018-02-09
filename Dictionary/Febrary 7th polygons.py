from turtle import Turtle

def square( t: Turtle, length: int)  -> None:
    """
    Draw a square with a given length
    :param t: an instance of a Turtle used to render my square
    :param length: the length of the side
    :return: None
    """
    for count in range(4)
        t.forward(length)
        t.left(90)

def hexagon( t: Turtle, length: int) -> None:
    """Draw a hexagon with a given length
    :param t: an instance of a Turtle used to render my hexagon
    :param length: the length of the side
    :return: None"""

    for count in range(6)
        t.forward(length)
        t.left(60)

def triangle( t: Turtle, length: int) -> None:
    """Draw a triangle with a given length
        :param t: an instance of a Turtle used to render my triangle
        :param length: the length of the side
        :return: None"""
    for count in range(3):
        t.forward(length)
        t.left(120)


def octagon( t: Turtle, length: int) -> None:
    """Draw a octagon with a given length
        :param t: an instance of a Turtle used to render my octagon
        :param length: the length of the side
        :return: None"""
    for count in range(8):
        t.forward(length)
        t.left(40)

def radial_pattern( t: Turtle, n: int, length: int, shape) -> None:
    """
    Draw the radial pattern of n shapes with given length
    :param t: a Turlte instant
    :param n: number of shapes
    :param length: length of side shape
    :param shape: a function of drawing some shape
    :return: None
    """
    for count in range(n):
        shape(t, length)
        t.left(360/n)
