import numpy as np

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




def main():
    game = init_game()
    print_game(game)
    
    
    

if __name__ == "__main__":
    main()