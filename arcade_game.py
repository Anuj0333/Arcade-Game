from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


s=Screen()
s.setup(width=800,height=600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0)


r_paddle=Paddle((380,0))
l_paddle=Paddle((-380,0))
ball=Ball()
scoreboard=Scoreboard( )


s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")    
s.onkey(l_paddle.go_up,"W")
s.onkey(l_paddle.go_down,"S")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update( )
    ball.move()

    #detect colision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce_y
        ball.bounce_y()

    #detect colision with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor(  )>360 or ball.distance(l_paddle)<50 and ball.xcor()<-360:
        ball.bounce_x(  )

    #DETECT when R_paddle misses
    if ball.xcor()>400:
        ball.reset_poaition()
        scoreboard.l_point()
        

    #DETECT when L_paddle misses
    if ball.xcor()<-400:
        ball.reset_poaition()
        scoreboard.r_point()
        















s.exitonclick()
