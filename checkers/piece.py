from checkers.contants import RED, WHITE, GREY, CROWN, SQUARESIZE
import pygame

class Piece:
    PADDING = 5

    def  __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQUARESIZE + SQUARESIZE // 2
        self.y = self.row * SQUARESIZE + SQUARESIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARESIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
        