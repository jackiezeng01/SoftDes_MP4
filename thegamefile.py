"""
Micro Project 4
"""

import pygame
import opencv as cv2
#this is the main file for the project with all of the classes and functions that will be called

class Obstacles:
#creates a class that for the obstacles
    def __init__(self, x_position, y_position):
    #initilizes each obstical with an x & y position
pass


class Runner:
#creates a class for the character in the game
    def __init__(self, x_position=middle):
    #initilizes the character with a starting x position (no y position because the background moves not the character)
pass


class Timer:
#creates a timer that serves
    def __init__(self, minute=0, second=0, millisecond=0):
pass


class Best_Time:
#class to save the high score/best time
pass


def init_game():
pass


def read_card():
    "if open cv reads left arrow"
        return "left"
    "if open cv reads right arrow"
        return "right"
    "if open cv does not read anything"
        return "stay"
pass


def move_left():
    "if read_card returns left shift the runner to the lane dirrectly to the left of thier current position"
    "if the runner is in the furthest left lane do not allow the runner to move further"
pass


def move_right():
    "if read_card returns right shift the runner to the lane dirrectly to the right"
    "if the runner is in the furthest right lane do not allow the runner to move further"
pass


def generate_obstacles():
    "randomly generates obsticals for the runner to dodge"
    "as time passes it creates more obsticals"
pass


def crash():
    "when runner hits an obstical with 0 lives the game ends and the end screen shows"
pass
