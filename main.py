import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Burak Oyun")
screen.tracer(0)
car_manager = CarManager()

burak = Player()
screen.listen()
screen.onkey(key="Up", fun=burak.move_forward)
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(burak) < 20:
            game_is_on = False
            scoreboard.game_over()

    if burak.is_at_finish_line():
        burak.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()



