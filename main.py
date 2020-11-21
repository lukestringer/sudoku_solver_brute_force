'''
NUMBERS ARE 0 -> 8 TO MAKE THINGS EASIER
EMPTY CELLS ARE -1
'''

grid = [[4, 2, -1, -1, 6, -1, -1, -1, -1],
        [5, -1, -1, 0, 8, 4, -1, -1, -1],
        [-1, 8, 7, -1, -1, -1, -1, 5, -1],
        [7, -1, -1, -1, 5, -1, -1, -1, 2],
        [3, -1, -1, 7, -1, 2, -1, -1, 0],
        [6, -1, -1, -1, 1, -1, -1, -1, 5],
        [-1, 5, -1, -1, -1, -1, 1, 7, -1],
        [-1, -1, -1, 3, 0, 8, -1, -1, 4],
        [-1, -1, -1, -1, 7, -1, -1, 6, 8]]


def print_game():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == -1:
                print('_', " ", end="", sep="")
            else:
                print(str(grid[i][j]), " ", end="", sep="")
            if (j + 1) % 3 == 0:
                print("  ", end="")
        print()
        if (i + 1) % 3 == 0:
            print()


# checks if if range(9) in set, updating possibilities accordingly
def check_set(set, set_possibilities):
    global grid
    # for each possible number
    for num in range(9):
        # the number is only an option if it is not in the set
        if num not in set:
            set_possibilities.add(num)
        else:
            set_possibilities.discard(num)
    return set_possibilities
        

def update_row_possibilites(rows):
    global grid
    # for each row
    for row in range(9):
        # update the row possibilties 
        rows[row] = check_set(grid[row], rows[row])
        # # for each possible number
        # for num in range(9):
        #     # the number is only an option if it is not in the row
        #     if num not in grid[row]:
        #         rows[row].add(num)
        #     else:
        #         rows[row].discard(num)
    print(rows)
    return rows


def update_col_possibilites(cols):
    global grid
    # for each column
    for col in range(9):
        # create a list for that column
        thisCol = [grid[i][col] for i in range(9)]
        # for each possible number
        for num in range(9):
            # the number is only an option if it is not in the column
            if num not in thisCol:
                cols[col].add(num)
            else:
                cols[col].discard(num)
    return cols


def update_seg_possibilites(segs):
    global grid
    # for each segment 
    for segRow in range(3):
        for segCol in range(3):
            ''' 
            e.g. segment 1,1
                rows 3,4,5  == 3*1 + i for i in range(3)
                cols 3,4,5  == 3*1 + i for i in range(3)
            '''
            # create a list for that segment from relevant cells
            thisSeg = []
            for cellRow in range(3):
                gridRow = 3*segRow + cellRow
                for cellCol in range(3):
                    gridCol = 3*segCol + cellCol
                    thisSeg.append(grid[gridRow][gridCol])
            # for each possible number
            for num in range(9):
                pass


def update_all_possibilities(possibilities):
    global grid
    rows, cols, segs = possibilities
    rows = update_row_possibilites(rows)
    cols = update_col_possibilites(cols)
    segs = update_seg_possibilites(segs)

    possibilities = (rows, cols, segs)
    return possibilities


def main():
    '''
    update possibilities for each row, column, and segment, putting them into buckets of # of possibilities from 0 -> 9
    if you find any with 1 blank space, fill in the blank space
        and recalc the possibilities for that cells row, col, seg
    if you find any with 2 blank spaces, try to solve it for each of those, and exit the one that runs into an error
        and recalc the possibilites

    '''
    global grid
    #initial list of possibilities is empty for each row/col/seg
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    segs = [set() for i in range(9)]
    possibilities = (rows, cols, segs)
    #update all the possibilities
    print_game()
    print('solving')
    possibilities = update_all_possibilities(possibilities)
    print_game()



if __name__ == '__main__':
    main()

