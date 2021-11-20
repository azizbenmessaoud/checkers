import pygame
from checkers.board import Board
from checkers.contants import RED

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valide_moves = {}

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()
        