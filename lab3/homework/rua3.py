from turtle import *

def draw_square(length,colorr):
    color(colorr)

    for _ in range(4):
        forward(length)
        left(90)