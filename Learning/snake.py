from graphics import *
from time import time
from random import randint
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

class GameLogic:

    def __init__(self, window, windowSizeX=250, windowSizeY=250):
        self.window = window
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        self.snake = self.createSnake()
        self.food = self.createFood()
        self.speed = 5
        self._gameLoop()

    def createFood(self):
        foodOriginX = randint(0, self.windowSizeX)
        foodOriginY = randint(0, self.windowSizeY)
        foodSize = 15
        foodOrigin = Point(foodOriginX, foodOriginY)
        foodEnd = Point(foodOriginX + foodSize, foodOriginY + foodSize)
        foodRectangle = Rectangle(foodOrigin, foodEnd)
        foodRectangle.setFill('white')
        foodRectangle.draw(self.window)
        return foodRectangle

    def createSnake(self):
        snakeOriginX = randint(0, self.windowSizeX)
        snakeOriginY = randint(0, self.windowSizeY)
        snakeSize = 15
        snakeOrigin = Point(snakeOriginX, snakeOriginY)
        snakeEnd = Point(snakeOriginX + snakeSize, snakeOriginY + snakeSize)
        snakeRectangle = Rectangle(snakeOrigin, snakeEnd)
        snakeRectangle.setFill('white')
        snakeRectangle.draw(self.window)
        return snakeRectangle
    # def appendSnake():
    def moveSnake(self, dx, dy):
        self.snake.move(dx * self.speed, dy * self.speed)
    # def moveFood():
    # def _update(self):
        
    # def _draw():
    def _input(self):
        running = True
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    self.moveSnake(-1, 0)
                if event.key == K_RIGHT:
                    self.moveSnake(1, 0)
                if event.key == K_UP:
                    self.moveSnake(0, -1)
                if event.key == K_DOWN:
                    self.moveSnake(0, 1)
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
        return running

    def _gameLoop(self):
        while True:
            if (self._input() == False):
                break
            # self._update()
            # _draw()

def main():
    window = GraphWin("Snake!", 500, 500)

    window.setBackground(color_rgb(0, 107, 169))

    game = GameLogic(window)

    window.getMouse()
    window.close()

main()