from turtle import Screen,Turtle
from ball import Ball
from paddle import Paddle
import time
from score import Score
sc=Screen()
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("PONG")
sc.tracer(0)

paddle=Turtle()
ball=Ball()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))



score=Score()
sc.listen()
sc.onkey(r_paddle.go_up, "Up")
sc.onkey(r_paddle.go_down, "Down")
sc.onkey(l_paddle.go_up, "w")
sc.onkey(l_paddle.go_down, "s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    #detect collision with wall
    if ball.ycor()>280or ball.ycor()<-280:
        ball.bounce_y()

    #collison with paddle both
    if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #detect when r_paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score.l_board()

    #detect when l_paddle misses

    if ball.xcor()<-380:
        ball.reset_position()
        score.r_board()





sc.exitonclick()