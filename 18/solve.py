import numpy as np

size = 100
grid = np.zeros((size+2,size+2), dtype=int)

with open("input.txt") as textFile:
    for i,line in enumerate(textFile):
        for j,char in enumerate(line):
            if char == '#':
                grid[i+1][j+1] = 1

def loop(gr, corner):
    if corner:
        gr[1][1] = 1
        gr[1][size] = 1
        gr[size][1] = 1
        gr[size][size] = 1
    newgrid = np.zeros((size+2,size+2), dtype=int)
    for i in range(1,size+1):
        for j in range(1,size+1):
            current = gr[i][j]
            sum = gr[i-1:i+2, j-1:j+2].sum() - current
            if current:
                if sum != 2 and sum != 3:
                    newgrid[i][j] = 0
                else:
                    newgrid[i][j] = 1
            else:
                if sum != 3:
                    newgrid[i][j] = 0
                else:
                    newgrid[i][j] = 1

    if corner:
        newgrid[1][1] = 1
        newgrid[1][size] = 1
        newgrid[size][1] = 1
        newgrid[size][size] = 1
    return newgrid

nn = grid.copy()
for i in range(100):
    nn = loop(nn, False).copy()

nn2 = grid.copy()
for i in range(100):
    nn2 = loop(nn2, True).copy()

print "The number of lights is: ", nn.sum()
print "The number of lights with corner alway on is: ", nn2.sum()
