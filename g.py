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

def possible(game,row,col,candidate):
    #check row
    for i in range(0,9):
        if game[row][i] == candidate:
            return False
    #check column
    for i in range(0,9):
        if game[i][col] == candidate:
            return False
    #check segment
    seg_row = (row//3)%3
    seg_col = (col//3)%3
    for i in range(0,3):
        for j in range(0,3):
            if game[seg_row+i][seg_col+j] == candidate:
                return False
    #if not in row col or seg, it's possible
    return True
        
def solve(game):
    for row in range(0,9):
        for column in range(0,9):
            if game[row][column] == 0:
                for candidate in range(1,10):
                    if possible(game,row,column,candidate):
                        game[row][column] = candidate
                        solve(game)
                        game[row][column] = 0
                return
    print_game(game)
    input("Enter for more")
    


def main():
    game = init_game()
    print_game(game)
    solve(game)
    
    
    

if __name__ == "__main__":
    main()
