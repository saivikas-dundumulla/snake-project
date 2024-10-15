import time
from turtle import Screen

from Food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to SnakeLand")
screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    # repaint the screen
    screen.update()
    time.sleep(0.1)
    # Move Snake
    snake.move()
    #Detect the collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        board.increase_score()
        snake.extend()
    # Detect the collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        board.reset()
        snake.reset()
    # Detect the collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset()



screen.exitonclick()