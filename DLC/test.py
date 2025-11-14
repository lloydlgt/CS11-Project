def pgrid(grid):
    for row in grid:
        print(''.join(row))
def movement(move, position):
    i, j = position[0], position[1]
    move = move.lower()
    if move == 'w':
        i -= 1
    elif move == 'a':
        j -= 1
    elif move == 's':
        i += 1
    elif move == 'd':
        j += 1
    else:
        return None
    return i, j

R = 30
C = 30

from random import randint
forest = []

for i in range(R):
    row = []
    for j in range(C):
        row.append('\N{White Large Square}')
    forest.append(row)



import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def is_in_bounds(r, c, i, j):
    return 0 <= i < r and 0 <= j < c


zombies = []
for _ in range(4):
    i, j = randint(0, R - 1), randint(0, C - 1)
    zombies.append([i, j])
    forest[i][j] = '\N{zombie}'

print(zombies)
i, j = randint(0, R - 1), randint(0, C - 1)
forest[i][j] = '\N{adult}'

directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
def heuristic(zombie: tuple[int, int], person: tuple[int, int], maxx: tuple[int, int]):
    h = []
    
    for direction in directions:
        print(person, zombie)
        di, dj = zombie[0] + direction[0], zombie[1] + direction[1]
        if is_in_bounds(maxx[0], maxx[1], di, dj):
            distance = abs(di - person[0]) + abs(dj - person[1])
            h.append((distance, (dj, di)))
    h.sort()
    print(h)
    return h[0][1]

tick = 0
while True:
    # clear()
    pgrid(forest)
    moves = input("Enter your move: ")
    for move in moves:
        # clear()
        # pgrid(forest)
        # sleep(0.5)
        next_i, next_j = movement(move, (i, j))
        if is_in_bounds(R, C, next_i, next_j) and forest[next_i][next_j] == '\N{White Large Square}':
            print('itworked', (next_i, next_j))
            forest[i][j] = '\N{White Large Square}'
            forest[next_i][next_j] = '\N{adult}'
            test = list((next_i, next_j))
            test1 = test.copy()
            orig_i, orig_j = i, j
            i, j = test1[0], test1[1]
        print('current position:', (i, j))
        tick %= 2
        if tick == 0:
            for z in range(len(zombies)): # i is already used
                zi, zj = zombies[z]
                hj, hi = heuristic((zi, zj), (i,j), (R, C))
                next_zi, next_zj = hi, hj
                if is_in_bounds(R, C, next_zi, next_zj) and forest[next_zi][next_zj] == '\N{White Large Square}':
                    forest[zi][zj] = '\N{White Large Square}'
                    forest[next_zi][next_zj] = '\N{zombie}'
                    zombies[z][0], zombies[z][1] = next_zi, next_zj
        tick += 1
        
