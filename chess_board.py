import tkinter as tk
import math
import Const

root = tk.Tk()
canvas = tk.Canvas(root, width=Const.Width, height=Const.Height)
canvas.pack()

# Define the size of the chessboard and the size of each square
board_size = 8
square_size = Const.Width / board_size

# define colors of tiles and border
tile_1_color = (Const.Primary_Colour)
tile_2_color = (Const.Secondary_Colour)
border_color = 'black'
border_width = 5

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
    'wp': tk.PhotoImage(file='resources/pieces_basic/white/pawn.png'),
    'wr': tk.PhotoImage(file='resources/pieces_basic/white/rook.png'),
    'wn': tk.PhotoImage(file='resources/pieces_basic/white/knight.png'),
    'wb': tk.PhotoImage(file='resources/pieces_basic/white/bishop.png'),
    'wq': tk.PhotoImage(file='resources/pieces_basic/white/queen.png'),
    'wk': tk.PhotoImage(file='resources/pieces_basic/white/king.png'),
    'bp': tk.PhotoImage(file='resources/pieces_basic/black/pawn.png'),
    'br': tk.PhotoImage(file='resources/pieces_basic/black/rook.png'),
    'bn': tk.PhotoImage(file='resources/pieces_basic/black/knight.png'),
    'bb': tk.PhotoImage(file='resources/pieces_basic/black/bishop.png'),
    'bq': tk.PhotoImage(file='resources/pieces_basic/black/queen.png'),
    'bk': tk.PhotoImage(file='resources/pieces_basic/black/king.png'),
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
