BOARD_SIZE = 3

# format board as [rows][cols]
gameboard = [[None] * BOARD_SIZE for n in range(BOARD_SIZE)]

def log_board():
    print('Gameboard')
    print('┌───┬───┬───┐')
    for row_index, row in enumerate(gameboard):

        print('│', end='')
        for cell in row:
            if cell == None:
                cell = ' '
            print(f' {cell} ', end='')
            print('│', end='')



        print()
        if row_index == len(gameboard) - 1:
            print('└───┴───┴───┘')
        else:
            print('├───┼───┼───┤')


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
