from tkinter import *
from functools import partial

'''
While I didn't get a sudoku solver that works (whether or not it takes too long or doesn't work, I don't know and they are functionally
equivalent anyway), I did get a bare-bones sudoku player. I wanted to understand tkinter a bit better and I did come away with some knowledge, 
having never used it before that I can recall. Also, I think getting those two cells solved in the first row was an accomplishment and I 
am happy that I made that much progres, because each time I do this it will get easier. I made more progres on this that I did on snake
because on snake I was obsessing over how I was implementing it, not actually getting it done. So that was a positive.
"Moving the goal posts" is something I tried not to do tonight. I will watch two videos on solving sudoku, one that inspired me to do this
and the other from computerphile, then I will call it quits until after stats exam (though I may need a break and that is a whole nother story anyway)
'''



def main():
    #set up main window
    window = Tk()
    window.title('Simple Sudoku')
    window.configure(background="black")
    window.geometry("670x850")

    # sudoku game 
    raw = "196..5....8...32.4...8....1.15....8..4....................1.9..3.8..4.65.2.5...38"
    matrix = [[raw[i] for i in range(9*j,9*j+9)] for j in range(0,9)]
    #for i in range(0,9):
        #print(matrix[i])
    '''
    0,8     0
    9,17    1
    18,26   2
    '''

    '''
    # label for first number
    Label(window, text="1", background="grey", width=6,height=3,padx=0,pady=0,font="25").grid(row=0, column=0, sticky="ew")
    # button for empty space
    btn_text_var = [0]
    def update_btn_text():
        btn_text_var[0] %= 9
        btn_text_var[0] += 1
        btn_text.set(btn_text_var[0])
    btn_text = StringVar()
    Button(window, textvariable=btn_text, command=update_btn_text, width=6,height=3, font="25").grid(row=0,column=1, sticky="ew")
    btn_text.set("")
    '''
    '''
    string_vars = []#[[StringVar() for i in range(0,9)] for j in range(0,9)]
    for i in range(0,9):
        for j in range(0,9):
            var = StringVar()
            string_vars.append(var)
            https://stackoverflow.com/questions/21738149/make-tkinter-buttons-for-every-item-in-a-list
            functools 
            '''

    labels =  [[None for i in range(0,9)] for j in range(0,9)]
    buttons = [[None for i in range(0,9)] for j in range(0,9)]
    # update button 
    def clicked(i, j):
        print("clicked ", i, j)
        matrix[i][j] %= 9
        matrix[i][j] += 1
        buttons[i][j]['text'] = matrix[i][j]


    for i in range(0,9):
        for j in range(0,9):
            #convert to numbers (0 if empty)
            if matrix[i][j]  == ".":
                matrix[i][j] = 0
            else:
                matrix[i][j] = int(matrix[i][j])

    #make a copy for solving later (deal with guesses separately)
    original = matrix

    for i in range(0,9):
        for j in range(0,9):
            #make button if 0 and label otherwise
            if matrix[i][j] == 0:
                #b = Button(window, text=matrix[i][j], command=lambda a=i, b=j: clicked(i,j))
                b = Button(window, command=partial(clicked, i, j), width=6,height=3,padx=0,pady=0,font="25")
                b.grid(row=i,column=j)#,sticky="ew")
                buttons[i][j] = b
            else:
                l = Button(window, text=matrix[i][j], width=6, height=3,padx=0,pady=0,font="25",state="disabled", background="grey69", fg="black")
                l.grid(row=i, column=j)#, sticky="ew")
                labels[i].append(l)



    #solve
    '''
    there are different strategies, but i am going for cutting down candidates
    from top left to bottom right over and over until 1 candidate remains in
    each cell (solved)
    '''
    def solve():
        candidates = [[[x for x in range(1,10)] for i in range(0,9)] for j in range(0,9)]
        #make a copy of original to solve
        solving = original
        solved = False
        avg = 0########################################################################################################
        count = 0########################################################################################################
        loops = 0
        while solved == False:
            if loops > 500000:
                break
            loops += 1

            #try to solve
            for i in range(0,9):
                for j in range(0,9):
                    if solving[i][j] == 0:
                        for x in range(1,10):
                            #cut down candidates 
                            #print("cands before: ",candidates[i][j])
                            #print("x:",x)
                            #collect all relevant cells
                            collection = []
                            #based on row 
                            collection.extend(solving[i])
                            #based on column (excluding row)
                            collection.extend([solving[r][j] for r in range(1,9)])
                            #based on segment (excluding row and col)
                            # based on the number [1,3] row and col the celll is in the segment
                            # the four remaning cells will be:
                            # (1) both after ++
                            # (2) one before and one after -+
                            # (3) both before --
                            # for both the row and cell directions

                            #default case is third (for no particular reason)
                            rowDelta = [-2,-1]
                            if i % 3 == 0:
                                #1st
                                rowDelta = [1,2]
                            elif i % 3 == 1:
                                #2nd
                                rowDelta = [-1,1]

                            colDelta = [-2,-1]
                            if j % 3 == 0:
                                colDelta = [1,2]
                            elif j % 3 == 1:
                                colDelta = [-1,1]

                            for y in range(0,2):
                                collection.append(solving[i+rowDelta[0]][j+colDelta[y]])
                                collection.append(solving[i+rowDelta[1]][j+colDelta[y]])

                            #remove all 0's from collection
                            collection = [y for y in collection if y > 0]

                            if x in collection:
                                if x in candidates[i][j]: candidates[i][j].remove(x)
                                #if we have solved the cell, add it to the solving matrix
                                if len(candidates[i][j]) == 1:
                                    solving[i][j] = candidates[i][j][0]
                            #print("cands after: ", candidates[i][j])
                            #print("----------------------")
                        count += 1
                        avg += len(candidates[i][j])
            avg = avg / count
            print(avg)

            #check if solved
            solved = True #will be set to false if exception found
            for i in range(0,9):
                for j in range(0,9):
                    #if there is one cell with more than one candidate
                    # it is unsolved and must rerun
                    if len(candidates[i][j]) > 1:
                        solved = False
                        break
        #print
        print("=================================")
        print("=================================")
        print("original")
        for i in range(0,9):
            for j in range(0,9):
                print(original[i][j], end='')
            print()
        print("=================================")
        print("=================================")
        print("solved")
        for i in range(0,9):
            for j in range(0,9):
                print(solving[i][j], end='')
            print()


    sb = Button(window, command=solve, width=6, height=3, font="25", text="SOLVE")
    sb.grid(row=10, column=4)


    #run main window loop
    window.mainloop()

if __name__ == '__main__':
    main()

'''
https://www.google.com/search?q=what+is+pyw&oq=what+is+pyw&aqs=chrome..69i57j0i10i457j0i20i263j0j0i10j0l3.1636j0j7&sourceid=chrome&ie=UTF-8 | what is pyw - Google Search
https://www.google.com/search?q=uninstall+python+bash&oq=uninstall+python+bash&aqs=chrome..69i57j0i457j0l6.3945j0j7&sourceid=chrome&ie=UTF-8 | uninstall python bash - Google Search
https://www.google.com/search?q=add+python3+to+path+windows+10&oq=add+python3+to+&aqs=chrome.1.0i457j0l3j69i57j0i20i263j0l2.3923j0j4&sourceid=chrome&ie=UTF-8 | add python3 to path windows 10 - Google Search
https://phoenixnap.com/kb/how-to-install-python-3-windows | How To Install Python 3 on Windows {Quickstart}
https://phoenixnap.com/kb/install-pip-windows | How to Install PIP For Python on Windows | PhoenixNAP KB
https://stackoverflow.com/questions/32615440/python-3-tkinter-how-to-update-button-text | Python 3, Tkinter, How to update button text - Stack Overflow
http://effbot.org/tkinterbook/variable.htm | The Variable Classes (BooleanVar, DoubleVar, IntVar, StringVar)
https://www.howtogeek.com/197919/ | How to Easily Add and Remove Programs in Ubuntu 14.04
https://www.youtube.com/watch?v=EwezNTJ-Lj0 | How to Search, Install, and Uninstall Software on Ubuntu Using Terminal - YouTube
https://www.howtogeek.com/229699/how-to-uninstall-software-using-the-command-line-in-linux/ | How to Uninstall Software Using the Command Line in Linux
chrome://history/ | History
https://stackoverflow.com/questions/35844170/tkinter-error-unboundlocalerror-local-variable-flag-referenced-before-assignm | python - Tkinter error UnboundLocalError: local variable 'flag' referenced before assignment - Stack Overflow
https://mail.python.org/pipermail/tkinter-discuss/2008-April/001383.html | [Tkinter-discuss] How to make all the buttons the same size?
http://www.effbot.org/tkinterbook/grid.htm | The Tkinter Grid Geometry Manager
https://stackoverflow.com/questions/971678/iterating-through-a-multidimensional-array-in-python | Iterating through a multidimensional array in Python - Stack Overflow
https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter | python - How to pass arguments to a Button command in Tkinter? - Stack Overflow
https://stackoverflow.com/questions/37350971/tkinter-entry-not-showing-the-current-value-of-textvariable | python - Tkinter Entry not showing the current value of textvariable - Stack Overflow
https://stackoverflow.com/questions/32640219/creating-stringvar-variables-in-a-loop-for-tkinter-entry-widgets | python - Creating StringVar Variables in a Loop for Tkinter Entry Widgets - Stack Overflow
https://www.google.com/search?q=tkinter+change+button+text&oq=tkinter+change+button+text&aqs=chrome..69i57j0i457j0l6.3950j0j7&sourceid=chrome&ie=UTF-8 | tkinter change button text - Google Search
https://www.delftstack.com/howto/python-tkinter/how-to-change-the-tkinter-button-text/ | How to Update the Tkinter Button Text | Delft Stack
https://pythonexamples.org/python-tkinter-change-button-text-dynamically/ | How to change Button Text Dynamically in Tkinter? - Python Examples
https://www.google.com/search?q=python+make+new+function+of+same+name&oq=python+make+new+function+of+same+name&aqs=chrome..69i57j69i64.19151j0j4&sourceid=chrome&ie=UTF-8 | python make new function of same name - Google Search
https://www.google.com/search?q=python+tkinter+button+function+list&oq=python+tkinter+button+function+list&aqs=chrome..69i57j69i64.12115j0j4&sourceid=chrome&ie=UTF-8 | python tkinter button function list - Google Search
https://stackoverflow.com/questions/21738149/make-tkinter-buttons-for-every-item-in-a-list | python - Make tkinter buttons for every item in a list? - Stack Overflow
https://docs.python.org/2.7/library/functools.html#functools.partial | 9.8. functools — Higher-order functions and operations on callable objects — Python 2.7.18 documentation
http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png | File:TkInterColorCharts.png - dftwiki
https://www.tutorialspoint.com/python/tk_label.htm | Python - Tkinter Label - Tutorialspoint
http://effbot.org/tkinterbook/label.htm | The Tkinter Label Widget
''' 