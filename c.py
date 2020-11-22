'''
    111 111 111
    111 111 111
    111 111 111

    111 111 111
    111 111 111
    111 111 111

    111 111 111
    111 111 111
    111 111 111


196 005 000
080 003 204
000 800 001

015 000 080
040 000 000
000 000 000

000 010 900
308 004 065
020 500 038

'''


'''
get the segment number from the list number
(each cell listed from left to right, top to bottom)
'''
def get_segment_number(cell_number):
    # get sgement row and col of cell
    column = (cell_number//3)%3
    row = cell_number//27
    # calculate segment number (init at 0)
    segments_per_row = 3
    seg_number = row * segments_per_row + column - 1
    return seg_number

def get_row_number(cell_number):
    return cell_number //9

def get_column_number(cell_number):
    return cell_number % 9

def print_game(game):
    for i in range(0,81):
        #print(f"{i//9:02d} ", end="")
        print(str(game[i]) + " ", end="")
        i += 1
        if i % 3 == 0:
            print(" ", end="")
        if i % 9 == 0:
                print()
        if i % (9 * 3) == 0:
                print()

def get_game_string():
    # currently default game, could ask for user input, use website or generate one
    return "196005000080003204000800001015000080040000000000000000000010900308004065020500038"

def process_game_string(game):
    processed_game = []
    for c in range(0,len(game)):
        try:
            i = int(game[c])
            processed_game.append(i)
        except ValueError:
            processed_game.append(0)
    return processed_game


def initialise_game():
    game = get_game_string()
    game = process_game_string(game)
    return game

def solve_game(game):
    for i in range(0,9*9):
        pass

def main():
    game = initialise_game()
    print_game(game)
    input("Press enter to solve")
    game = solve_game(game)
    print_game(game)



if __name__ == "__main__":
    main()



'''

init game:
    get game string: 
        get the game from user, internet, or generate it
    process game string:
        turn string into flat list
    return processed game
solve game:
    for each cell, print out binary 


'''