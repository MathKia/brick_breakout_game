from turtle import Turtle

FONT = ("Courier", 15, "normal")


class LivesTracker(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-380, 280)
        self.lives = 3
        self.lives_text()
        self.alive = True

    def lives_text(self):
        self.write(f"Lives = {self.lives}", align="left", font=FONT)

    def lives_decrease(self):
        self.clear()
        if self.lives > 1:
            self.lives -= 1
            self.lives_text()
        else:
            self.game_over_lose()

    def game_over_lose(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"YOU LOSE", align="center", font=FONT)
        self.goto(0, -50)
        self.alive = False

    def game_over_win(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"YOU WIN", align="center", font=FONT)
        self.goto(0, -50)
        self.alive = False
