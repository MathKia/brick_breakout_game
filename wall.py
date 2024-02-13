import turtle
from turtle import Turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
x_positions = [-340, -220, -100, 20, 140, 260, 380]
y_positions = [250, 170, 90]

class Wall(Turtle):

    def __init__(self):
        self.wall = []
        self.bricks_gone = []
        self.bricks()

    def bricks(self):

        for y_spot in y_positions:
            for x_spot in x_positions:
                new_brick = turtle.Turtle()
                new_brick.penup()
                new_brick.shape("square")
                new_brick.shapesize(stretch_len=4, stretch_wid=2)
                new_brick.color(random.choice(colors))
                new_brick.goto(x_spot, y_spot)
                self.wall.append(new_brick)

    def destroy_brick(self, brick):
        brick.hideturtle()
        brick.goto(-500, -500)
        self.bricks_gone.append(brick)





































