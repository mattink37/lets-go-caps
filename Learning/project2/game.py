import pygame
import sys
from pygame.locals import *

pygame.init()


# def createTile():


# def createTileMap():

class CaveGenerator:

    def __init__(self, unitSize, windowSizeX=500, windowSizeY=500):

        # game variables
        self.unitSize = unitSize
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        # window surface object setup
        x = 0
        y = 1

        if (self.windowSizeX % self.unitSize != 0):     # Ensure the window fits unit size exactly
            self.windowSizeX += self.unitSize - \
                self.windowSizeX % self.unitSize
        if (self.windowSizeY % self.unitSize != 0):
            self.windowSizeY += self.unitSize - \
                self.windowSizeY % self.unitSize
        self.window = pygame.display.set_mode(
            [self.windowSizeX, self.windowSizeY])
        pygame.display.set_caption("Cave Generator")
        self.backgroundColor = (36, 45, 54)
        self.window.fill(self.backgroundColor)

        self.tileMapDimensions = self.createTilemap()
        self.tileMap = []

        # game logic
        self._gameLoop()

    def createTilemap(self):
        return [self.window.get_width(
        ) / self.unitSize, self.window.get_height() / self.unitSize]

    def fillTileMap(self):
        stuff = 0

    def _update(self):
        self.window.fill(self.backgroundColor)
        pygame.display.update()

    def _gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
            pygame.time.delay(100)
            # self._input() if I add input it will be called here
            self._update()


def main():
    cave = CaveGenerator(15, 500, 500)


main()
