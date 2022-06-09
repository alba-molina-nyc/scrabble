def board():
    width = 15
    height = 15
    board = []
    row = []
    square = "| |"
    for i in range(width):
        row.append(square)
    for i in range(height):
        board.append(row)
    while True:
        for i in range(len(board)):
            print(board[i])
        break

board()


"""
15x15 grid for scrabble
"""







    