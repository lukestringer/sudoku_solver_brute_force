from time import sleep
import os
i = 0
alpha = chr(172) + chr(28) + '-' + '_'#"abcdefghijklmnopqrstuvwxyz"
while True:
    print(i)
    i += 1
    for j in range(0, len(alpha)):
        print(alpha[(j + i)% len(alpha)], end='')
    i %= len(alpha)
    print()
    sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
'''while True:
    print(i)
    for j in range(0,26):
        print(chr(97 + (i + j)%26), end='')
    i += 1
    i %= 26
    print()
    sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')'''