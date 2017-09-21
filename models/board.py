"""
Represent game board state
"""

import random

class BoardError(Exception):
    """Exception for Board logic"""
   
def index_to_coord(pos, num_rows, num_columns):
    """Convert index as counted left to right, top to bottom to a coordinate in a 2d array"""
    if pos > num_rows*num_columns - 1:
        raise BoardError("Linear position out of bounds")
    return (pos//num_rows, pos%num_columns)


def get_adjactent(r,c, num_rows, num_columns):
    """Get (<=)8 coordinates around one coordinate. Won't return out of bounds coords""" 
    return [(adj_row, adj_col)
            for adj_row in [r+x for x in range(-1,2) if r+x >= 0 and r+x < num_rows]
            for adj_col in [c+x for x in range(-1,2) if c+x >= 0 and c+x < num_columns]
            if (adj_row, adj_col) != (r,c)]


class Tile:
    def __init__(self):
        self.bomb = False
        self.score = 0
        self.hidden = True
        self.marked = False

    def __str__(self):
        if self.marked:
            return "X"
        elif self.hidden:
            return "-"
        elif self.bomb:
            return "B"
        else:
            return str(self.score)

    def reveal(self):
        self.hidden = False

    def is_bomb(self):
        return self.bomb

    def toggle_mark(self):
        self.marked = not self.marked 


def make_board(rows,columns,bombs):
    board = [[Tile() for _ in range(columns)] for _ in range(rows)]
    bomb_coords = [index_to_coord(x,rows,columns) for x in random.sample(range(rows*columns), bombs)]
    for x,y in bomb_coords:
        board[x][y].bomb=True
        for x_a,y_a in get_adjactent(x,y, rows, columns):
            board[x_a][y_a].score += 1
    return board


class Board:

    def __init__(self, rows=20, columns=20, bombs=4):
        if bombs > rows*columns-1:
            raise BoardError("Too Many Bombs")

        self.rows = rows
        self.columns = columns
        self.bombs = bombs
        self.board = make_board(rows,columns,bombs)

        self.hidden_tiles = rows*columns - bombs


    def __str__(self):
        out = ""
        for r in self.board:
            for e in r:
                out+= " " + str(e) + " "
            out+="\n"
        return out

    def reveal_all(self):
        for row in self.board:
            for tile in row:
                tile.reveal()

    def at(self, index):
        row, column = index 
        return self.board[row][column]

    def reveal_tile(self, row, column):
        tile = self.board[row][column]
        if not tile.hidden:
            return 
        tile.reveal()
        if not tile.is_bomb():
            self.hidden_tiles-=1
    


    def toggle_tile_mark(self, row, column):
        self.board[row][column].toggle_mark()




