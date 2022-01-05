#!/usr/bin/env python3

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from time import sleep

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()

score = Score()
score.display_score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

if __name__ == '__main__':
    game_running = True

    while game_running:
        sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.new_location()
            snake.add_body_part()
            score.update_score()

        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            game_running = False
            score.game_over()

        snake_trail = snake.snake_body[1:]
        for part in snake_trail:
            if snake.head.distance(part) < 10:
                game_running = False
                score.game_over()

        screen.update()
    screen.exitonclick()

