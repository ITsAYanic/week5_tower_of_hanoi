from classes.pillars import Pillars
from functions.move_plate import move_plate


game = Pillars(3)
autosolve_game = Pillars(3)
move_plate(game, "p1", "p3")
move_plate(game, "p1", "p2")
move_plate(game, "p3", "p2")
move_plate(game, "p1", "p3")
move_plate(game, "p2", "p1")
move_plate(game, "p2", "p3")
move_plate(game, "p1", "p3")

def solve_game(autosolve_game):
    yield

print(game)