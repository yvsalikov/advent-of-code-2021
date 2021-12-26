# Advent of Code 2021
# https://adventofcode.com/2021
# Day 18: Snailfish

from typing import Any
from math import floor, ceil
from itertools import permutations

class Number:
    LEFT = -1
    RIGHT = +1
    def __init__(self):
        self.left_val = None
        self.right_val = None
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__(self) -> str:
        str_buff = []
        str_buff.append("[")
        if self.left:
            str_buff.append(self.left.__str__())
        if self.left_val != None:
            str_buff.append(str(self.left_val))
        str_buff.append(",")
        if self.right:
            str_buff.append(self.right.__str__())
        if self.right_val != None:
            str_buff.append(str(self.right_val))
        str_buff.append("]")
        return "".join(str_buff)
        
    def reduce(self) -> None:
        is_reduced = False
        while not is_reduced:
            # print(f":{self}")
            path = []
            is_reduced = self._traverse_and_explode(path, 0)
            if not is_reduced:
                continue
            is_reduced = self._traverse_and_split(path, 0)
    
    def add(self, number: Any) -> Any:
        result = Number()
        result.left = self
        self.parent = result
        result.right = number
        number.parent = result # mutate argument
        result.reduce()
        return result
    
    def magnitude(self) -> int:
        mag = 0
        if self.left_val != None:
            mag += 3*self.left_val
        else:
            mag += 3*self.left.magnitude()
        if self.right_val != None:
            mag += 2*self.right_val
        else:
            mag += 2*self.right.magnitude()
        return mag
    
    def _traverse_and_explode(self, path: list, level: int) -> bool:
        if level == 4:
            self._explode(path)
            return False
        
        if self.left:
            path.append(self.LEFT)
            if not self.left._traverse_and_explode(path, level+1):
                return False
            path.pop()
        if self.right:
            path.append(self.RIGHT)
            if not self.right._traverse_and_explode(path, level+1):
                return False
            path.pop()
        return True
        
    def _traverse_and_split(self, path: list, level: int) -> bool:
        if self.left_val != None:
            if self.left_val >= 10:
                number = Number()
                number.left_val = floor(self.left_val / 2)
                number.right_val = ceil(self.left_val / 2)
                number.parent = self
                self.left = number
                self.left_val = None
                return False
        if self.left:
            path.append(self.LEFT)
            if not self.left._traverse_and_split(path, level+1):
                return False
            path.pop()
            
        if self.right_val != None:
            if self.right_val >= 10:
                number = Number()
                number.left_val = floor(self.right_val / 2)
                number.right_val = ceil(self.right_val / 2)
                number.parent = self
                self.right = number
                self.right_val = None
                return False
        if self.right:
            path.append(self.RIGHT)
            if not self.right._traverse_and_split(path, level+1):
                return False
            path.pop()
        return True
    
    def _explode(self, path: list) -> None:
        # print(self)
        # first to the left
        left = None
        parent = self.parent
        for i in range(-1, -(len(path) + 1), -1):
            # go "upward" on path
            if path[i] == self.RIGHT:
                if parent.left_val != None:
                    parent.left_val += self.left_val
                else:
                    # go "downward" on neighbour branch
                    child = parent.left
                    while child.right:
                        child = child.right
                    child.right_val += self.left_val
                break
            parent = parent.parent
        # first to the right
        right = None
        parent = self.parent
        for i in range(-1, -(len(path) + 1), -1):
            if path[i] == self.LEFT:
                if parent.right_val != None:
                    parent.right_val += self.right_val
                else:
                    child = parent.right
                    while child.left:
                        child = child.left
                    child.left_val += self.right_val
                break
            parent = parent.parent
        
        # remove referenses to exploded pair
        parent = self.parent
        if path[-1] == self.LEFT:
            parent.left_val = 0
            parent.left = None
        else:
            parent.right_val = 0
            parent.right = None
        self.parent = None
    

def read(line: str) -> Number:
    stack = []
    LEFT = -1
    RIGHT = +1
    part = []
    for char in line:
        if char == "[":
            stack.append(Number())
            part.append(LEFT)
        elif char == ",":
            # part.pop()
            part.append(RIGHT)
        elif char == "]":
            number = stack.pop()
            if part:
                is_left_element = part.pop()
            if stack:
                number.parent = stack[-1]
                if is_left_element == LEFT:
                    stack[-1].left = number
                else:
                    stack[-1].right = number
        else: # values
            is_left_element = part.pop()
            if is_left_element == LEFT:
                stack[-1].left_val = int(char)
            else:
                stack[-1].right_val = int(char)
    return number

def add(num1: Number, num2: Number) -> Number:
    result = Number()
    result.left = num1
    num1.parent = result
    result.right = num2
    num2.parent = result
    result.reduce()
    return result


largest_magnitude = 0
with open("input.txt") as file:
    numbers = file.read().splitlines()
    for x, y in permutations(range(len(numbers)), 2):
        num1 = read(numbers[x])
        num2 = read(numbers[y])
        s = add(num1, num2)
        magnitude = s.magnitude()
        if magnitude > largest_magnitude:
            largest_magnitude = magnitude

print(largest_magnitude)

