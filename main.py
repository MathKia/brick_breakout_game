from turtle import Screen
from ball import Ball
from paddle import Paddle
from wall import Wall
from lives_tracker import LivesTracker
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor('black')
screen.title("B R E A K  O U T")
screen.tracer(0)

ball = Ball()
paddle = Paddle()
wall = Wall()
lives = LivesTracker()

screen.listen()
screen.onkeypress(key="Left", fun=paddle.move_left)
screen.onkeypress(key="Right", fun=paddle.move_right)



while True:

    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounce_x()
    if ball.ycor() > 280 or ball.distance(paddle.paddle_body[0]) < 20 or ball.distance(paddle.paddle_body[1]) < 20 or ball.distance(paddle.paddle_body[2]) < 20:
        ball.bounce_y()
    if ball.ycor() < -310:
        lives.lives_decrease()
        if not lives.alive:
            break
        ball.reset_ball(paddle.paddle_body[1].xcor()+12, paddle.paddle_body[1].ycor()+12)
        ball.bounce_y()
    for brick in wall.wall:
        if ball.distance(brick) < 30:
            wall.destroy_brick(brick)
            if len(wall.bricks_gone) % 3 == 0:
                ball.ball_speed_up()
            if len(wall.bricks_gone) == 21:
                lives.game_over_win()
                break
            ball.bounce_y()



screen.exitonclick()



































