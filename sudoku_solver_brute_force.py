import copy

grid = [[ 4,  2, -1, -1,  6, -1, -1, -1, -1],
        [ 5, -1, -1,  0,  8,  4, -1, -1, -1],
        [-1,  8,  7, -1, -1, -1, -1,  5, -1],
        [ 7, -1, -1, -1,  5, -1, -1, -1,  2],
        [ 3, -1, -1,  7, -1,  2, -1, -1,  0],
        [ 6, -1, -1, -1,  1, -1, -1, -1,  5],
        [-1,  5, -1, -1, -1, -1,  1,  7, -1],
        [-1, -1, -1,  3,  0,  8, -1, -1,  4],
        [-1, -1, -1, -1,  7, -1, -1,  6,  8]]


#returns cells and sections (rows,cols,segs)
def get_cells_from_raw(raw):
    #init empty cells
    cells = [[] for i in range(9)]
    
    #replace '.' in raw with '0'
    raw = raw.replace('.','0')
    #for each row and col in game, put in number from raw into relevant cell
    row = col = 0
    for char in raw:
        # -1 is empty, 0 through 8 are values
        contents = int(char)-1
        cells[row].append(contents)
        #increment cell row,col numbers
        col += 1
        if col == 9:
            col = 0
            row += 1
    return cells


def cells_to_string(cells):
    s = '---------------------\n'
    for i in range(9):
        for j in range(9):
            if cells[i][j] == -1:
                s += '_ '
            else:
                s += str(cells[i][j]) + " "
            if (j + 1) % 3 == 0:
                s += "  "
        s += '\n'
        if i == 2 or i == 5:
            s += '\n'
    s += '---------------------\n'
    return s


def is_not_in_row(grid, row,val):
    return val not in grid[row]


def is_not_in_col(grid,col,val):
    for i in range(9):
        if val == grid[i][col]:
            return False
    return True


def is_not_in_seg(grid,row,col,val):
    segRow = (row//3)*3
    segCol = (col//3)*3
    for i in range(3):
        for j in range(3):
            if grid[segRow + i][segCol + j] == val:
                return False
    return True


def solve_with_game(grid):
    global hmm_counter
    for row in range(9):
        for col in range(9):
            if grid[row][col] == -1:
                for val in range(9):
                    if is_not_in_row(grid,row,val) and is_not_in_col(grid,col,val) and is_not_in_seg(grid,row,col,val):
                        new_grid = copy.deepcopy(grid)
                        new_grid[row][col] = val
                        solved = solve_with_game(new_grid)
                        if solved != None:
                            return solved
                #if all the values are in all the sections the cell relates to (no possibilities left) return None
                hmm_counter += 1
                #print('m',end='')
                return None
    return grid

#TODO generate the games yourself (incl. difficulty settings) instead of using https://qqwing.com/generate.html
g1 = get_cells_from_raw('.8.....2...72....962.8.3...7.......3......4.6...3271....4...........9.3.....169.7')
g2 = get_cells_from_raw('4.9....8.3.68.59..5....1..3...7..15..68.3...7.......3........9..9....7.1..3....4.')
g3 = get_cells_from_raw('78.5..............912........735.9.8..827.16.56..9..2.....6....25.....3...38.....')
g4 = get_cells_from_raw('648..7.9.2.......3.9.......3....852.....457..87..3...9..6.......8.....4.....94.67')
g5 = get_cells_from_raw('.71.....45........4..68..3..3.......9.6.74...1....8463...7.......385..7..9......1')
g6 = get_cells_from_raw('.24........68..7.2..5..3...3..2...6.7..58.13.....4..2...1...5...6...1.4.......3..')
g7 = get_cells_from_raw('...193..........4..8...7....9.....2.1..9.8...84..2....9..3...14..487.23..38.5.9.7')

grids = [g1,g2,g3,g4,g5,g6,g7]

for grid in grids:
    print('unsolved')
    print(cells_to_string(grid))
    print('trying to solve...')

    hmm_counter = 0
    s = solve_with_game(grid)
    print('took '+str(hmm_counter)+' "hmms" to solve')
    print(cells_to_string(s))