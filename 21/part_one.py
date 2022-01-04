# Advent of Code 2021
# https://adventofcode.com/2021
# Day 21: Dirac Dice

from typing import Any
from itertools import cycle

class DiracDice:
    WINNING_SCORE = 1000
    
    class DeterministicDice:
        value = 0
        total_rolls = 0
        def roll(self) -> int:
            self.total_rolls += 1
            self.value += 1
            # if self.value > 100:
                # self.value = 1
            return self.value
    
    class Player:
        def __init__(self, number: int, start_position: int) -> None:
            self.name = number
            self.position = start_position
            self.score = 0
        
        def move(self, dice) -> int:
            result = 0
            # print(f"Player {self.name} rolls ", end="")
            for _ in range(3):
                d = dice.roll()
                # print(f"{d} ", end="")
                result += d
            self.position = (self.position + result) % 10
            if self.position == 0:
                self.position = 10
            self.score += self.position
            # print(f"and moves to space {self.position} for a total score of {self.score}.")
            return self.score
            
    def __init__(self, filename: str):
        self.players = []
        with open(filename) as file:
            num = 0
            for line in file:
                num += 1
                start_pos = int(line[line.find(":") + 2:])
                self.players.append(self.Player(num, start_pos))
        self.dice = self.DeterministicDice()
    
    def play(self) -> int:
        score = 0
        players = cycle(self.players)
        while score < self.WINNING_SCORE:
            player = next(players)
            score = player.move(self.dice)
        # print(f"Player {player.name} wins with total score {player.score}!")
        return next(players).score * self.dice.total_rolls

game = DiracDice("input.txt")
print(game.play())