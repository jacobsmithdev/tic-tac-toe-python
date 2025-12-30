# format board as [rows][cols]
gameboard = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

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
