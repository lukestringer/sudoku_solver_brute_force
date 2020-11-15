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
   
    # print options
    # def print_options(op, range=range(1,10)):
    #     for i in range:
    #         if i in op:
    #             print(str(i) + "  ", end="")
    #         else:
    #             print("_  ", end="")
    #     print()
    # for op in ro,co,so:
    #     print_options(op)
    # print()
    # print_options(options)
    return options



def get_all_options(game):
    options = [[] for i in range(0,9)]
    for row in range(0,9):
        for col in range(0,9):
            options[row].append(check_cell_options(row,col,game))
    return options

    



def main():
    game = init_game()
    print_game(game)
    options = get_all_options(game)
    #check_cell_options(1,4,game)
    
    

if __name__ == "__main__":
    main()
















# print all options
# flatten list
# pop = ""
# for row in range(0,9):
#     for col in range(0,9):
#         for i in range(1,10):
#             if i in options[row][col]:
#                 pop += str(i)
#             else:
#                 pop += "."
# for k in range(0,3):
#     for j in range(0,3):
#         for i in range(0,3):
#             print(pop[9*j+3*k+i],end="")
#         print(" ",end="")
#     print()

# rowSize = 9
# colSize = 9
# optRowSize = 3
# for rowNum in range(0,9):
#     for colNum in range(0,9):
#         for optRowNum in range(0,3):
#             for opColNum in range(0,3):
#                 print(pop[rowNum*rowSize  + colNum*colSize  +  optRowNum*optRowSize + opColNum],end="")
#             print(" ",end="")
#             if colNum == 3 and rowNum == 3:
#                 print()
#         print()
#     if rowNum % 3 == 0:
#         print()


'''
00  = 0 * 27  +  0 * 9  +  0 * 3  +  0 = rowNum*rowSize  +  colNum*colSize  +  optRowNum*optRowSize + opColNum
01  = 0 * 27  +  0 * 9  +  0 * 3  +  1 
02

09  = 0 * 27  +  1 * 9  +  0 * 3  +  0
10
11

18
19
20

NL

03
04
05

12
13
14

21
22
23

NL

06
07
08

15
16
17

24
25
26
'''

# print(pop[9*0+3*0+0],end="")#0
# print(pop[9*0+0*3+1],end="")#1
# print(pop[9*0+0*3+2],end="")#2
# print(" ",end="")
# print(pop[9*1+0*3+0],end="")#9
# print(pop[9*1+0*3+1],end="")#10
# print(pop[9*1+0*3+2],end="")#11
# print(" ",end="")
# print(pop[9*2+0*3+0],end="")#18
# print(pop[9*2+0*3+1],end="")#19
# print(pop[9*2+0*3+2],end="")#20
# print()

# print(pop[9*0+1*3+0],end="")#3
# print(pop[9*0+1*3+1],end="")#4
# print(pop[9*0+1*3+2],end="")#5
# print(" ",end="")
# print(pop[9*1+1*3+0],end="")#12
# print(pop[9*1+1*3+1],end="")#13
# print(pop[9*1+1*3+2],end="")#14
# print(" ",end="")
# print(pop[9*2+1*3+0],end="")#21
# print(pop[9*2+1*3+1],end="")#22
# print(pop[9*2+1*3+2],end="")#23
# print()

# print(pop[9*0+2*3+0],end="")#6
# print(pop[9*0+2*3+1],end="")#7
# print(pop[9*0+2*3+2],end="")#8
# print(" ",end="")
# print(pop[9*1+2*3+0],end="")#15
# print(pop[9*1+2*3+1],end="")#16
# print(pop[9*1+2*3+2],end="")#17
# print(" ",end="")
# print(pop[9*2+2*3+0],end="")#24
# print(pop[9*2+2*3+1],end="")#25
# print(pop[9*2+2*3+2],end="")#26
# print()

# print()


# print(pop[27*1  +  9*0  +  0*3  +0],end="")#0 + 27
# print(pop[27*1+9*0+0*3+1],end="")#1
# print(pop[27*1+9*0+0*3+2],end="")#2
# print(" ",end="")
# print(pop[27*1+9*1+0*3+0],end="")#9
# print(pop[27*1+9*1+0*3+1],end="")#10
# print(pop[27*1+9*1+0*3+2],end="")#11
# print(" ",end="")
# print(pop[27*1+9*2+0*3+0],end="")#18
# print(pop[27*1+9*2+0*3+1],end="")#19
# print(pop[27*1+9*2+0*3+2],end="")#20
# print()

# print(pop[27*1  +  9*0  +  1*3  +0],end="")#3
# print(pop[27*1+9*0+1*3+1],end="")#4
# print(pop[27*1+9*0+1*3+2],end="")#5
# print(" ",end="")
# print(pop[27*1+9*1+1*3+0],end="")#12
# print(pop[27*1+9*1+1*3+1],end="")#13
# print(pop[27*1+9*1+1*3+2],end="")#14
# print(" ",end="")
# print(pop[27*1+9*2+1*3+0],end="")#21
# print(pop[27*1+9*2+1*3+1],end="")#22
# print(pop[27*1+9*2+1*3+2],end="")#23
# print()

# print(pop[27*1+9*0+2*3+0],end="")#6
# print(pop[27*1+9*0+2*3+1],end="")#7
# print(pop[27*1+9*0+2*3+2],end="")#8
# print(" ",end="")
# print(pop[27*1+9*1+2*3+0],end="")#15
# print(pop[27*1+9*1+2*3+1],end="")#16
# print(pop[27*1+9*1+2*3+2],end="")#17
# print(" ",end="")
# print(pop[27*1+9*2+2*3+0],end="")#24
# print(pop[27*1+9*2+2*3+1],end="")#25
# print(pop[27*1+9*2+2*3+2],end="")#26
# print()