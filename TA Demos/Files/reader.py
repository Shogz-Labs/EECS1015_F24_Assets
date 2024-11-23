import time
with open('TA Demos\Files\why_do_i.txt', 'r') as file:
    for line in file.readlines():
        for word in line.strip():
            print(word, end='')
            time.sleep(0.01)
        print()