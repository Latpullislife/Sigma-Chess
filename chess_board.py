import tkinter as tk
import math
from Const import*
from files import*

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

# Dictionary to store the current position of each piece
piece_positions = {}

# Function to get the chess piece at a given board position
def get_piece(row, col):
    return board[row][col];

# Function to update the board position for a piece
def update_position(row, col, piece):
    board[row][col] = piece
    piece_positions[piece] = (row, col)


# Function to handle mouse click event
def on_click(event):
    global selected_piece, selected_piece_image, selected_piece_position, selected_piece_image_id
    x, y = event.x, event.y
    col = x // square_size
    row = y // square_size
    piece = get_piece(row, col)

    if piece != '  ':
        selected_piece = piece
        selected_piece_image = images[selected_piece]
        selected_piece_position = (row, col)
        # canvas.delete(selected_piece_image_id)


# Function to handle mouse drag event
def on_drag(event):
    if selected_piece is not None:
        x, y = event.x, event.y
        canvas.coords(selected_piece_image_id, x, y)


# Function to handle mouse release event
def on_release(event):
    global selected_piece, selected_piece_image, selected_piece_position, selected_piece_image_id
    if selected_piece is not None:
        x, y = event.x, event.y
        col = x // square_size
        row = y // square_size
        new_position = (row, col)
        update_position(*selected_piece_position, '  ')  # Clear the old position
        update_position(*new_position, selected_piece)  # Update the new position
        canvas.coords(selected_piece_image_id, col * square_size, row * square_size)
        selected_piece_image_id = None  # Delete the old piece image ID
        selected_piece = None


# Bind mouse events to functions
canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)

# Place the pieces on the chessboard initially
for row in range(board_size):
    for col in range(board_size):
        piece = board[row][col]
        if piece != '  ':
            x = col * square_size
            y = row * square_size
            piece_image_id = canvas.create_image(x + square_size // 2, y + square_size // 2, image=images[piece])
            piece_positions[piece] = (row, col)
            images[piece] = piece_image_id

# Variables to keep track of the selected piece and its image
selected_piece = None
selected_piece_image = None
selected_piece_position = None
selected_piece_image_id = None

root.mainloop()
