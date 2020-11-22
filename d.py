def print_game(game):
    for i in range(0,9):
        for j in range(0,9):
            print(str(game[i][j])," ", end="", sep="")
            if (j+1) % 3 == 0:
                print("  ", end="")
        print()
        if (i+1) % 3 == 0:
            print()




def init_game():
    game_str = "196005000080003204000800001015000080040000000000000000000010900308004065020500038"
    #game_str = "196245873587163294432897651215439786743682519869751342654318927378924165921576438"
    #                                                        V
    #game_str = "196245873587163294432897651215439786743682519069751342654318927378924165921576438"
    game_ls = [[] for i in range(0,9)]
    for row in range(0,9):
        for col in range(0,9):
            try:
                game_ls[row].append(int(game_str[9 * row + col]))
            except ValueError:
                game_ls[row].append(0)
    return game_ls




def row_options(row, col, game):
    options = []
    # check row
    for i in range(1,10):
        if i not in game[row]:
            options.append(i)
    return options



def col_options(row,col,game):
    options = []
    # check col
    column = [game[i][col] for i in range(0,9) if game[i][col] != 0]
    for i in range(1,10):
        if i not in column:
            options.append(i)
    return options




def get_segment_coord(row,col,game):
    return (row//3, col//3)



def seg_options(row,col,game):
    # get segment as list
    seg_row = row - (row % 3)
    seg_col = col - (col % 3)
    segment = []
    for row in range(seg_row, seg_row + 3):
        for col in range(seg_col, seg_col + 3):
            if game[row][col] != 0:
                segment.append(game[row][col])
    # calclulate options
    options = []
    for i in range(1,10):
        if i not in segment:
            options.append(i)
    return options



def check_cell_options(row,col,game):
    # only check options for empty cells
    if game[row][col] != 0:
        return []#[game[row][col]]

    # options as sets
    ro = set(row_options(row,col,game))
    co = set(col_options(row,col,game))
    so = set(seg_options(row,col,game))
    # & is intersection
    options = list(ro & co & so)
    return options



def get_all_options(game):
    options = [[] for i in range(0,9)]
    for row in range(0,9):
        for col in range(0,9):
            cell_opts = check_cell_options(row,col,game)
            options[row].append(cell_opts)
    return options

#returns all the options and the (row,col) of the first cell with the fewwest options greater than 0
def get_all_options_and_fewest_coords(game):
    options = [[] for i in range(0,9)]
    min = 9
    coords = (99,99)#garbage
    for row in range(0,9):
        for col in range(0,9):
            cell_opts = check_cell_options(row,col,game)
            options[row].append(cell_opts)
            #check if smaller than min
            if len(cell_opts) < min and len(cell_opts) > 0:
                min = len(cell_opts)
                coords = (row,col)
    return (options, coords)




def main():
    game = init_game()
    print_game(game)
    options, (row,col) = get_all_options_and_fewest_coords(game)
    print(row,col," ",options[row][col])
    max = 9
    
    #check_cell_options(1,4,game)
    
    

if __name__ == "__main__":
    main()
