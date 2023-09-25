import tkinter as tk
import math
from Const import*
from files import*
root =  tk.Tk()
canvas = tk.Canvas(root, width=Width, height=Height)
root.minsize(800, 800)
canvas.pack()

# Draw the squares of the chessboard
for row in range(board_size):
    for col in range(board_size):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        if (row + col) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, outline=border_color, width=border_width, fill=tile_1_color)
        else:
            canvas.create_rectangle(x1, y1, x2, y2, outline=border_color, width=border_width, fill=tile_2_color)

# Add images for chess pieces and scale them

images = {
    'wp': tk.PhotoImage(file=pawn_white),
    'wr': tk.PhotoImage(file=rook_white),
    'wn': tk.PhotoImage(file=knight_white),
    'wb': tk.PhotoImage(file=bishop_white),
    'wq': tk.PhotoImage(file=queen_white),
    'wk': tk.PhotoImage(file=king_white),
    'bp': tk.PhotoImage(file=pawn_black),
    'br': tk.PhotoImage(file=rook_black),
    'bn': tk.PhotoImage(file=knight_black),
    'bb': tk.PhotoImage(file=bishop_black),
    'bq': tk.PhotoImage(file=queen_black),
    'bk': tk.PhotoImage(file=king_black),
}

#Enlarge pieces to fit board:
for key in images:
    images[key] = images[key].zoom(3)
for key1 in images:
    images[key1] = images[key1].subsample(2)
# Place the pieces on the chessboard
board = [
    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr'],
]
points = [[0] * board_size] * board_size
for row in range(board_size):
    for col in range(board_size):
        piece = board[row][col]
        x = col * square_size
        y = row * square_size
        if piece != '  ':
            canvas.create_image(x + square_size // 2, y + square_size // 2, image=images[piece])
        '''
        points[col][row] = x + square_size // 2
        points[col] = y + square_size // 2
        '''

root.mainloop()
