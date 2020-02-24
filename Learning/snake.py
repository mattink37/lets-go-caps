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
        self.snake = [self.createSnake()]
        self.food = self.createFood()
        self.speed = 15
        self._gameLoop()

    def createFood(self):
        # TODO
        # Make food spawn where the snake isn't
        foodX = randint(0, self.window.get_width() - self.gameUnitSize)
        if (foodX % self.gameUnitSize != 0):
            foodX -= foodX % self.gameUnitSize
        foodY = randint(0, self.window.get_height() - self.gameUnitSize)
        if (foodY % self.gameUnitSize != 0):
            foodY -= foodY % self.gameUnitSize
        foodRectangle = Rect((foodX, foodY), (self.gameUnitSize, self.gameUnitSize))
        return foodRectangle

    def createSnake(self):
        snakeNodeX = randint(0, self.window.get_width())
        if (snakeNodeX % self.gameUnitSize != 0):
            snakeNodeX -= snakeNodeX % self.gameUnitSize
        snakeNodeY = randint(0, self.window.get_height())
        if (snakeNodeY % self.gameUnitSize != 0):
            snakeNodeY -= snakeNodeY % self.gameUnitSize
        snakeNodeRectangle = Rect((snakeNodeX, snakeNodeY), (self.gameUnitSize, self.gameUnitSize))
        return snakeNodeRectangle

    def appendSnake(self):
        # add node to tail
        newSnakeLink = Rect((self.snake[len(self.snake) - 1].x, self.snake[len(self.snake) - 1].y), (self.gameUnitSize, self.gameUnitSize))
        self.snake.append(newSnakeLink)

    def moveSnake(self, dx, dy):
        self.snake[len(self.snake) - 1].x = self.snake[0].x + dx * self.speed
        self.snake[len(self.snake) - 1].y = self.snake[0].y + dy * self.speed
        self.snake.insert(0, self.snake.pop())

    def intersect(self):
        if self.snake[0].x == self.food.x and self.snake[0].y == self.food.y:
            return True

    def _update(self):
        self.window.fill((0,0,0))
        
        if (self.intersect() == True):
            self.appendSnake()
            self.createFood()
        # elif snake hits wall || snake hits snake
            #killSnake

        for link in self.snake:
            pygame.draw.rect(self.window, (255, 255, 255), link)
        pygame.draw.rect(self.window, (102, 255, 51), self.food)
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
