#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    player_1 = Player("Alice")
    player_2 = Player("Bob")

    game = Game("Chess")
    result_1 = Result(player_1, game, 1000)
    result_2 = Result(player_2, game, 500)

    highest_scored_player = Player.highest_scored(game)

    print(highest_scored_player)

    ipdb.set_trace()
