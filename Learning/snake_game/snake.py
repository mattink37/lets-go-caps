from random import randint
import pygame
from pygame import (Rect)
from sys import exit
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT,
                           K_RIGHT, K_UP, KEYDOWN, QUIT)


class GameLogic:

    def __init__(self, windowSizeX=250, windowSizeY=250):
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        self.gameUnitSize = 15
        if (self.windowSizeX % self.gameUnitSize != 0):
            self.windowSizeX += self.gameUnitSize - self.windowSizeX % self.gameUnitSize
        if (self.windowSizeY % self.gameUnitSize != 0):
            self.windowSizeY += self.gameUnitSize - self.windowSizeY % self.gameUnitSize
        self.window = pygame.display.set_mode(
            [self.windowSizeX, self.windowSizeY])
        pygame.display.set_caption("Snake!")
        self.window.fill((0, 0, 0))
        pygame.font.init()
        self.font = pygame.font.SysFont("bahnschrift", 20)

        self.text = self.font.render(
            "Press any key to begin", True, (255, 255, 255))
        self.startTextRect = self.text.get_rect(
            center=(windowSizeX/2, windowSizeY/2))
        self.snake = [self.startSnake()]
        self.food = self.createFood()
        self.speed = 15
        self.score = 0
        self.scoreText = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255), None)
        self.snakeDirections = {
            'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}

        self.previousDirection = self.snakeDirections.get('left')
        self._readyScreen()
        self._gameLoop()

    def startSnake(self):
        snakeNodeX = self.window.get_width() / 2 - self.gameUnitSize
        if (snakeNodeX % self.gameUnitSize != 0):
            snakeNodeX -= snakeNodeX % self.gameUnitSize
        snakeNodeY = self.window.get_height() / 2 - self.gameUnitSize
        if (snakeNodeY % self.gameUnitSize != 0):
            snakeNodeY -= snakeNodeY % self.gameUnitSize
        snakeNodeRectangle = Rect(
            (snakeNodeX, snakeNodeY), (self.gameUnitSize, self.gameUnitSize))
        return snakeNodeRectangle

    def createFood(self):
        foodX = randint(0, self.window.get_width() - self.gameUnitSize)
        if (foodX % self.gameUnitSize != 0):
            foodX -= foodX % self.gameUnitSize
        foodY = randint(0, self.window.get_height() - self.gameUnitSize)
        if (foodY % self.gameUnitSize != 0):
            foodY -= foodY % self.gameUnitSize
        foodRectangle = Rect(
            (foodX, foodY), (self.gameUnitSize, self.gameUnitSize))
        return foodRectangle

    def moveFood(self):
        self.food.x = randint(0, self.window.get_width() - self.gameUnitSize)
        if (self.food.x % self.gameUnitSize != 0):
            self.food.x -= self.food.x % self.gameUnitSize
        self.food.y = randint(0, self.window.get_height() - self.gameUnitSize)
        if (self.food.y % self.gameUnitSize != 0):
            self.food.y -= self.food.y % self.gameUnitSize

    def createSnake(self):
        snakeNodeX = randint(0, self.window.get_width())
        if (snakeNodeX % self.gameUnitSize != 0):
            snakeNodeX -= snakeNodeX % self.gameUnitSize
        snakeNodeY = randint(0, self.window.get_height())
        if (snakeNodeY % self.gameUnitSize != 0):
            snakeNodeY -= snakeNodeY % self.gameUnitSize
        snakeNodeRectangle = Rect(
            (snakeNodeX, snakeNodeY), (self.gameUnitSize, self.gameUnitSize))
        return snakeNodeRectangle

    def appendSnake(self):
        # add node to tail
        newSnakeLink = Rect((self.snake[len(self.snake) - 1].x, self.snake[len(
            self.snake) - 1].y), (self.gameUnitSize, self.gameUnitSize))
        self.snake.append(newSnakeLink)

    def moveSnake(self, direction):
        x = 0
        y = 1
        self.snake[len(self.snake) - 1].x = self.snake[0].x + \
            direction[x] * self.speed
        self.snake[len(self.snake) - 1].y = self.snake[0].y + \
            direction[y] * self.speed
        self.snake.insert(0, self.snake.pop())
        self.previousDirection = direction

    def intersect(self):
        if self.snake[0].x == self.food.x and self.snake[0].y == self.food.y:
            return True

    def snakeCollidingWithWall(self):
        if self.snake[0].x >= self.windowSizeX or self.snake[0].x < 0 or self.snake[0].y >= self.windowSizeY or self.snake[0].y < 0:
            return True
        return False

    def snakeCollidingWithSelf(self):
        for link in self.snake:
            if (self.snake[0] is not link):
                if self.snake[0].x == link.x and self.snake[0].y == link.y:
                    return True
        return False

    def killSnake(self):
        self._gameOverScreen()

    def _update(self):
        self.window.fill((0, 0, 0))

        if (self.intersect() == True):
            self.appendSnake()
            self.moveFood()
            self.score += 1
        elif (self.snakeCollidingWithWall() == True or self.snakeCollidingWithSelf() == True):
            self.killSnake()

        for link in self.snake:
            pygame.draw.rect(self.window, (255, 255, 255), link)
        pygame.draw.rect(self.window, (102, 255, 51), self.food)

        self.scoreText = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        self.scoreTextRect = self.scoreText.get_rect(center=(40, 10))
        self.window.blit(self.scoreText, self.scoreTextRect)

        pygame.display.update()

    def _input(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
        keys = pygame.key.get_pressed()
        if (keys[K_LEFT] and self.previousDirection != self.snakeDirections.get('right')):
            self.moveSnake(self.snakeDirections.get('left'))
        elif (keys[K_RIGHT] and self.previousDirection != self.snakeDirections.get('left')):
            self.moveSnake(self.snakeDirections.get('right'))
        elif (keys[K_UP] and self.previousDirection != self.snakeDirections.get('down')):
            self.moveSnake(self.snakeDirections.get('up'))
        elif (keys[K_DOWN] and self.previousDirection != self.snakeDirections.get('up')):
            self.moveSnake(self.snakeDirections.get('down'))
        else:
            self.moveSnake(self.previousDirection)

    def _readyScreen(self):
        while True:
            self.window.blit(self.text, self.startTextRect)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
            keys = pygame.key.get_pressed()
            if (keys[K_LEFT]):
                self.previousDirection = self.snakeDirections.get('left')
                break
            if (keys[K_RIGHT]):
                self.previousDirection = self.snakeDirections.get('right')
                break
            if (keys[K_UP]):
                self.previousDirection = self.snakeDirections.get('up')
                break
            if (keys[K_DOWN]):
                self.previousDirection = self.snakeDirections.get('down')
                break
            pygame.display.update()

    def _gameOverScreen(self):
        while True:
            self.window.fill((0, 0, 0))
            self.text = self.font.render(
                f"Game Over, Score: {self.score}", True, (255, 255, 255))
            self.startTextRect = self.text.get_rect(
                center=(self.windowSizeX/2, self.windowSizeY/2))
            self.window.blit(self.text, self.startTextRect)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
            pygame.display.update()

    def _gameLoop(self):
        while True:
            pygame.time.delay(100)
            self._input()
            self._update()


class LeaderBoard:

    def __init__(self):
        # needs to be changed to relative path
        file = open("C:\git\hmt\Learning\leaderboard.txt", "r")
        self.leaderboard = []
        i = 0
        while i < 5:
            chunk = file.readline()
            if (chunk == ''):
                break
            LeaderBoard.insert(0, chunk.splitlines())
            i += 1
        file.close()
        self.leaderboard.reverse()

    @staticmethod
    def addToLeaderboard(self, name, newScore):
        i = 0
        for score in self.leaderboard:
            if newScore > score:
                self.leaderboard.remove(score)
                self.leaderboard.insert(i, newScore)
            i += 1
        file = open("C:\git\hmt\Learning\leaderboard.txt", "w")
        # add name and score
        file.close()


def main():
    #l = LeaderBoard()
    game = GameLogic(250, 250)


main()
