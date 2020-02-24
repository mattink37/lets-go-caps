from random import randint
import pygame
from pygame import (Rect)
from sys import exit
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT)

class GameLogic:

    def __init__(self, windowSizeX=250, windowSizeY=250):
        self.window = pygame.display.set_mode([windowSizeX, windowSizeY])
        pygame.display.set_caption("Snake!")
        self.window.fill((0, 0, 0))
        self.gameUnitSize = 15
        self.snake = self.createSnake()
        self.food = self.createFood()
        self.speed = 15
        self._gameLoop()

    def createFood(self):
        foodX = randint(0, self.window.get_width() - self.gameUnitSize)
        foodY = randint(0, self.window.get_height() - self.gameUnitSize)
        foodRectangle = Rect((foodX, foodY), (self.gameUnitSize, self.gameUnitSize))
        return foodRectangle

    def createSnake(self):
        snakeNodeX = randint(0, self.window.get_width())
        snakeNodeY = randint(0, self.window.get_height())
        snakeNodeRectangle = Rect((snakeNodeX, snakeNodeY), (self.gameUnitSize, self.gameUnitSize))
        return snakeNodeRectangle
    def appendSnake(self):
        # add node to tail
        blah = 0
    def moveSnake(self, dx, dy):
        self.snake.x += dx * self.speed
        self.snake.y += dy * self.speed
        # self.snake.move(dx * self.speed, dy * self.speed)
    # def moveFood():
    def _update(self):
        self.window.fill((0,0,0))
        pygame.draw.rect(self.window, (255, 255, 255), self.snake)
        pygame.display.update()

    def _input(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
        keys = pygame.key.get_pressed()
        if (keys[K_LEFT]):
            self.moveSnake(-1, 0)
        elif (keys[K_RIGHT]):
            self.moveSnake(1, 0)
        elif (keys[K_UP]):
            self.moveSnake(0, -1)
        elif (keys[K_DOWN]):
            self.moveSnake(0, 1)

    def _gameLoop(self):
        while True:
            pygame.time.delay(100)
            self._input()
            self._update()

def main():
    game = GameLogic(500, 500)
main()
