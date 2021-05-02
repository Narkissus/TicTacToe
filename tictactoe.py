from os import system
from string import ascii_uppercase


class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [["_" for x in range(size)] for y in range(size)]
        self.actor = None

    @staticmethod
    def clear():
        system("cls")

    def draw_board(self):
        print(" ", end=" ")
        for x in range(1, self.size+1):
            print(x, end=" ")
        print()
        for i, row in enumerate(self.board):
            print(ascii_uppercase[i], end=" ")
            for element in row:
                print(element, end=" ")
            print()

    def update_board(self):
        if self.actor is not None:
            self.board[self.actor[0]][self.actor[1]] = self.actor[2]
        self.clear()
        self.draw_board()

    def player_turn(self, player):
        while True:
            try:
                coor = input("Player '{}' ... Please enter the coordinates (e.g. D4): ".format(player))
                if int(coor[1]) != 0:
                    row = ascii_uppercase.index(coor[0].upper())
                    col = int(coor[1:])-1
                    if self.board[row][col] == "_":
                        self.actor = row, col, player
                        break
                    else:
                        print("You cannot rewrite an assigned position")
                else:
                    print("Coordinates are out of range")
            except ValueError:
                print("Incorrect coordinates format")
            except IndexError:
                print("Coordinates are out of range")

    def check_winning_conditions(self, player):
        for lines in self.board, list(zip(*self.board)), self.get_for_dia(), self.get_bck_dia():
            for line in lines:
                if self.check_for_four(line, player):
                    print("Player {} won!".format(player))
                    return True
        # Checking for stalemates
        if [x for sub in self.board for x in sub].count("_") == 0:
            print("Stalemate!")
            return True

    def get_bck_dia(self):
        b = [None] * (len(self.board) - 1)
        grid = [b[i:] + r + b[:i] for i, r in enumerate([[c for c in r] for r in self.board])]
        return [[c for c in r if c is not None] for r in list(zip(*grid))]

    def get_for_dia(self):
        b = [None] * (len(self.board) - 1)
        grid = [b[:i] + r + b[i:] for i, r in enumerate([[c for c in r] for r in self.board])]
        return [[c for c in r if c is not None] for r in list(zip(*grid))]

    @staticmethod
    def check_for_four(array, player):
        if array.count(player) == 4:
            for i, symbol in enumerate(array):
                if symbol == player == array[i+1] == array[i+2] == array[i+3]:
                    return True
