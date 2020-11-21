'''
NUMBERS ARE 0 -> 8 TO MAKE THINGS EASIER
EMPTY CELLS ARE -1
'''
#grid = [[ 1,  2,  3,  4,  5,  6,  7, -1, -1],
grid = [[ 4,  2, -1, -1,  6, -1, -1, -1, -1],
        [ 5, -1, -1,  0,  8,  4, -1, -1, -1],
        [-1,  8,  7, -1, -1, -1, -1,  5, -1],
        [ 7, -1, -1, -1,  5, -1, -1, -1,  2],
        [ 3, -1, -1,  7, -1,  2, -1, -1,  0],
        [ 6, -1, -1, -1,  1, -1, -1, -1,  5],
        [-1,  5, -1, -1, -1, -1,  1,  7, -1],
        [-1, -1, -1,  3,  0,  8, -1, -1,  4],
        [-1, -1, -1, -1,  7, -1, -1,  6,  8]]


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


def to_seg_num(row,col):
    return 3*(row//3) + col//3


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

        # if there is only 1 possiblity left, 
        if len(rows[row]) == 1:
            # pop from possibility set into last empty cell in row 
            for cell in grid[row]:
                if cell == -1:
                    grid[row][cell] = rows[row].pop()
    return rows


def update_col_possibilites(cols):
    global grid
    # for each column
    for col in range(9):
        # create a list for that column
        thisCol = [grid[i][col] for i in range(9)]
        # update the column possibilities
        cols[col] = check_set(thisCol, cols[col])

        #if there is only 1 possibility left,
        if len(cols[col]) == 1:
            # pop it from the possibility set into last empty cell in column
            for rowNum in range(9):
                if grid[rowNum][col] == -1:
                    grid[rowNum][col] = cols[col].pop()
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
            # update the segment possibilities
            segNum = 3*segRow + segCol
            segs[segNum] = check_set(thisSeg, segs[segNum])
    return segs


def update_all_possibilities(possibilities):
    global grid
    rows, cols, segs = possibilities
    rows = update_row_possibilites(rows)
    cols = update_col_possibilites(cols)
    segs = update_seg_possibilites(segs)

    possibilities = (rows, cols, segs)
    return possibilities


#returns the length of and index for the smallest set in the list
def smallest_in(list):
    min = 10
    index = None
    for i in range(9):#len(posses)
        if len(list[i]) < min:
            min = len(list[i])
            index = i
    return min, index


#get the section with fewest possibilities
def get_smallest_section(possibilities):
    rows, cols, segs = possibilities
    # get minumum from each section type
    rowMin, rowIndex = smallest_in(rows)
    colMin, colIndex = smallest_in(cols)
    segMin, segIndex = smallest_in(segs)
    # find which is minimum section (they may be equal)
    if rowMin <= colMin:
        if segMin <= rowMin:
            #seg is smallest
            sectionType = 'seg'
            sectionNum = segIndex
        else:
            #row is smallest
            sectionType = 'row'
            sectionNum = rowIndex
    else:
        if segMin <= colMin:
           #seg is smallest
           sectionType = 'seg'
           sectionNum = segIndex
        else:
            #col is smallest
            sectionType = 'col'
            sectionNum = colIndex
    return sectionType, sectionNum


def solve(possibilities):
    rows, cols, segs = possibilities

    solved = False
    while solved == False:
        # find section with fewest possibilities
        sectionType, sectionNum = get_smallest_section(possibilities)
        # for each empty cell in the section, cross reference with remaining two section possibilities
        if sectionType == 'row':
            row = sectionNum
            for col in range(9):
                if grid[row][col] == -1:
                    # 'cross-ref' means find difference between cell section possibilities and hope it leaves 1 option
                    cell_poss = rows[row] - (cols[col] | segs[to_seg_num(row,col)])
                    print(cell_poss)
                    # if there is one possibility for the empty cell, fill it and update possiblities for that cell's sections
                    if len(cell_poss) == 1:
                        grid[row][col] = cell_poss.pop()
                        rows, cols, segs = update_all_possibilities(possibilities)
                        # restart loop
                        continue
                    # if there is more than one possibility for the empty cell TODO 

def initialise_possibilities():
    global grid
    #get possibilities for each row,column,segment
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    segs = [set() for i in range(9)]
    possibilities = (rows, cols, segs)
    #update all the possibilities, filling in single possibility sections
    possibilities = update_all_possibilities(possibilities)
    rows, cols, segs = possibilities
    return possibilities


def main():
    '''
    update possibilities for each row, column, and segment, putting them into buckets of # of possibilities from 0 -> 9
    if you find any with 1 blank space, fill in the blank space
        and recalc the possibilities for that cells row, col, seg
    if you find any with 2 blank spaces, try to solve it for each of those, and exit the one that runs into an error
        and recalc the possibilities

    '''
    global grid
    print('Unsolved Game:')
    print_game()
    print('Getting initial section possibilities')
    # possibilities contains a list for rows, cols, segs, each of which contains possibilities for it's row,col,seg. 
    possibilities = initialise_possibilities()
    print('Solving...')
    solve(possibilities)
    print('Solved:')
    print_game()


if __name__ == '__main__':
    main()

