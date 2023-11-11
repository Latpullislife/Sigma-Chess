import tkinter as tk

root = tk.Tk()
width = 800
height = 800
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Define the size of the chessboard and the size of each square
board_size = 8
square_size = width / board_size

# Define colors of tiles and border
tile_1_color = ('#c7baa8')
tile_2_color = ('#565044')
border_color = 'black'
border_width = 5

# Add images for chess pieces and scale them
images = {
    'wp': tk.PhotoImage(file='white_pawn.png'),
    'wr': tk.PhotoImage(file='white_rook.png'),
    'wn': tk.PhotoImage(file='white_knight.png'),
    'wb': tk.PhotoImage(file='white_bishop.png'),
    'wq': tk.PhotoImage(file='white_queen.png'),
    'wk': tk.PhotoImage(file='white_king.png'),
    'bp': tk.PhotoImage(file='black_pawn.png'),
    'br': tk.PhotoImage(file='black_rook.png'),
    'bn': tk.PhotoImage(file='black_knight.png'),
    'bb': tk.PhotoImage(file='black_bishop.png'),
    'bq': tk.PhotoImage(file='black_queen.png'),
    'bk': tk.PhotoImage(file='black_king.png'),
}

# Enlarge pieces to fit board:
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
    return board[row][col]


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
