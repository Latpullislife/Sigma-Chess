import pygame
import sys
from Const import *


class Game:
    def __init__(self):
        pass

    def show_background(self, surface):
        for row in range(Rows):
            for col in range(Cols):
                if (row + col) % 2 == 0:
                    color = (199, 186, 168)
                else:
                    color = (86, 80, 68)

                rect = (col * Square_size, row * Square_size, Square_size, Square_size)

                pygame.draw.rect(surface, color, rect)
