import pygame
from checkers.contants import BLACK, RED, WHITE, COLS, ROWS, SQUARESIZE
from checkers.piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self_white_kings = 0
        self.create_board()

    def create_board(self):
        for row in ROWS:
            self.board.append([])
            for col in COLS:
                if col % 2 == (row + 1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARESIZE, col*SQUARESIZE, SQUARESIZE, SQUARESIZE))

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
