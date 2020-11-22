'''
find section with fewest possibilities
for each empty cell in that section, cross-reference possibilities for its sections to find cell options
if cell options == len 1:
    fill in cell, update possibilities for that cell's sections
if cell options == len >1:
    (e.g. len == 2)
    
'''

#mapping of cells to their seg number to make things easy
seg_num = [[] for i in range(9)]
for row in range(9):
    for i in range(3):
        for potato in range(3):
            seg_num[row].append(3*(row//3) + i)


def cells_to_string(cells):
    s = '---------------------\n'
    for i in range(9):
        for j in range(9):
            if cells[i][j].contents == -1:
                s += '_ '
            else:
                s += str(cells[i][j].contents) + " "
            if (j + 1) % 3 == 0:
                s += "  "
        s += '\n'
        if i == 2 or i == 5:
            s += '\n'
    s += '---------------------\n\n'
    return s

#get a cell's segment number [0,8] from the cell row and column number
def seg_num(row,col):
    return 3*(row//3) + col//3


def row_col_from_seg(seg_num):
    row = (seg_num//3) * 3
    col = (seg_num%3) * 3
    return row, col


'''------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------------------------------'''

class Section:
    'any section (row, column, segment) on the grid'

    def __init__(self,num,possibilities=None):
        self.num = num
        self.possibilities = possibilities if possibilities is not None else set()
    

    def __repr__(self):
        return str(self.num) + ': ' + str(self.possibilities)


class Row(Section):
    'a row on the grid'

    def __init__(self,num,possibilities=None):
        super().__init__(num,possibilities)


class Column(Section):
    'a column on the grid'

    def __init__(self,num,possibilities=None):
        super().__init__(num,possibilities)


class Segment(Section):
    'a segment on the grid'

    def __init__(self,num,possibilities=None):
        super().__init__(num,possibilities)


class Cell:
    'cell has a number each for which row,column,segment it\'s in. can be solved or just temporarily filled'

    def __init__(self, contents, row, col, seg, solved=False):
        self.contents = contents
        self.row = row
        self.col = col
        self.seg = seg
        self.solved = solved

    def __repr__(self):
       return 'c' + str(self.contents)

class Game:
    'game has 81 cells and related 9 each of rows,cols,segs'

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
            cells[row].append(Cell(contents=contents, row=row,col=col,seg=seg_num(row,col)))
            #increment cell row,col numbers
            col += 1
            if col == 9:
                col = 0
                row += 1
        return cells
    
    def get_row_possibilities(cells):
        rows = [Row(num=rowNum) for rowNum in range(9)]
        #for each row of cells
        rowNum = 0
        for rowOfCells in cells:
            #for each cell in the row
            possibilities = set(range(9))
            for cell in range(9):
                #remove the cell number from the possibilities
                possibilities.discard(rowOfCells[cell].contents)
            #update the row sections possibilities
            rows[rowNum].possibilities = possibilities
            #increment current row number
            rowNum += 1
        return rows

    def get_col_possibilities(cells):
        cols = [Column(num=colNum) for colNum in range(9)]
        possibilities = set(range(9))
        #for each column of cells
        for colNum in range(9):
            columnContents = {cells[rowNum][colNum].contents for rowNum in range(9)}
            cols[colNum].possibilities = possibilities - columnContents
        return cols


    def get_seg_possibilities(cells):
        segs = [Segment(num=segNum) for segNum in range(9)]
        #for each segment
        for seg in range(9):
            possibilities = set(range(9))
            segment = set()
            #get the segment cells
            row, col = row_col_from_seg(seg)
            for r in range(3):
                for c in range(3):
                    segment.add(cells[row+r][col+c].contents)
            segs[seg].possibilities = possibilities - segment
        return segs


    def __init__(self,raw):
        #empty cells and sections (rows,cols,segs)
        self.cells = Game.get_cells_from_raw(raw)
        self.rows = Game.get_row_possibilities(self.cells)
        self.cols = Game.get_col_possibilities(self.cells)
        self.segs = Game.get_seg_possibilities(self.cells)

    def __repr__(self):
        s = cells_to_string(self.cells) + 'rows: ' + str(self.rows) + '\n'
        s += 'cols: '+ str(self.cols) + '\n' + 'segs: '+ str(self.segs)
        return s
          

'''------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------------------------------'''

def game_is_solved(game):
    # try to find an unsolved cell
    foundUnsolvedCell = False
    #break when finding an unsolved cell
    for cellRow in game.cells:
        if foundUnsolvedCell == True:
            break
        for cell in cellRow:
            if cell.solved == False:
                foundUnsolvedCell = True
                break
    #if we have not found any unsolved cells, we have solved the game
    solved = not foundUnsolvedCell
    return solved


def sect_with_fewest(game):
    min = 99
    minType = ''
    mindex = 99
    for i in range(9):
        minRow = len(game.rows[i].possibilities)
        if minRow < min and minRow > 0:
            min = minRow
            minType = 'row'
            mindex = i
        minCol = len(game.cols[i].possibilities)
        if minCol < min and minCol > 0:
            min = minCol
            minType = 'col'
            mindex = i
        minSeg = len(game.cols[i].possibilities)
        if minSeg < min and minSeg > 0:
            min = minSeg
            minType = 'seg'
            mindex = i
    return min, minType, mindex

def solve(game):
    solved = False
    while solved == False:
        #test if the game is solved
        if game_is_solved(game):
            break
        #find section with fewest possibilities
        min, minType, mindex = sect_with_fewest(game)
        #for each cell in that section
        # find cell with fewest possibilities 
        # if cell has 1 possibility, fill it in, check for duplicates in sections (raise error if yes)
        #                                    and update section possibilities by removing that number
        #                                       ALSO set cell to solved
        # if cell has more than one possibility
        # for each possibility try the first one
            

def main():
    #hard coded games for now TODO
    raw_unsolved = '4.9....8.3.68.59..5....1..3...7..15..68.3...7.......3........9..9....7.1..3....4.'
    raw_solved = '419376285376825914582491673934782156168539427257164839741658392895243761623917548'
    raw_one_match_to_make = '4193762853768259145824916739347821561685394272571.4839741658392895243761623917548'
    game = Game(raw=raw_one_match_to_make)
    print(cells_to_string(game.cells))
    print(game)
    print('solving')
    solve(game)
    

    
if __name__ == "__main__":
    main()