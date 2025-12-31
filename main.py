BOARD_SIZE = 3

# format board as [rows][cols]
gameboard = [[None] * BOARD_SIZE for n in range(BOARD_SIZE)]


def log_board():
    print("Gameboard")
    print("┌───┬───┬───┐")
    for row_index, row in enumerate(gameboard):

        print("│", end="")
        for cell in row:
            if cell == None:
                cell = " "
            print(f" {cell} ", end="")
            print("│", end="")

        print()
        if row_index == len(gameboard) - 1:
            print("└───┴───┴───┘")
        else:
            print("├───┼───┼───┤")


def place_character(row, col, char):
    if len(char) > 1:
        char = char[0]

    if not valid_coords(row, col):
        return False

    if gameboard[row][col]:
        return False

    gameboard[row][col] = char
    return True


def valid_coords(row, col):
    if 0 < row > BOARD_SIZE - 1:
        return False
    if 0 < col > BOARD_SIZE - 1:
        return False
    return True


def play_move(char):
    while True:
        log_board()
        coords = input("Enter 'row, col' between 0-2 (e.g., '1, 2', '0, 0'):\n")

        try:
            row, col = coords.split(",")
            row = int(row)
            col = int(col)

            if place_character(row, col, char):
                return True
            else:
                raise Exception()

        except:
            print("Invalid input, please try again.")


def winner_exists(active_player):
    win_conditions_rows = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
    ]

    win_conditions_cols = [
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
    ]
    win_conditions_diagonals = [
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]],
    ]

    win_conditions = (
        win_conditions_rows + win_conditions_cols + win_conditions_diagonals
    )

    for condition in win_conditions:
        if all(gameboard[row][col] == active_player for row, col in condition):
            return True

    return False


def is_board_full():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if not gameboard[row][col]:
                return False
    return True
