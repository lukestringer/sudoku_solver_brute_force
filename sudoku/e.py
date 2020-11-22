
for i in range(0,9):
    for j in range(0,9):
        print(i,"|", j, " ", end="", sep="")
        if (j+1) % 3 == 0:
            print("  ", end="")
    print()
    if (i+1) % 3 == 0:
        print()