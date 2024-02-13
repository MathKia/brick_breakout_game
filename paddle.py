import turtle
from turtle import Turtle

x = [-40, 0, 40]

class Paddle:

    def __init__(self):
        self.paddle_body = []
        self.make_paddle()
        self.head = self.paddle_body[0]
        self.tail = self.paddle_body[2]

    def make_paddle(self):

        for square in x:

            new_square = turtle.Turtle()
            new_square.penup()
            new_square.color("white")
            new_square.shape("square")
            new_square.shapesize(stretch_len=2)
            new_square.goto(square, -200)
            self.paddle_body.append(new_square)



    def move_left(self):
        if -370 < self.head.xcor():
            for square in self.paddle_body:
                square.backward(30)


    def move_right(self):
        if 370 > self.tail.xcor():
            for square in self.paddle_body:
                square.forward(30)




























