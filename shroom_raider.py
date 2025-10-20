from argparse import ArgumentParser
import os

class Func:
    def pgrid(grid):
        for row in grid:
            print(''.join(row))

class Boot:
    def launch():
        parser = ArgumentParser()
        parser.add_argument('stage_file')
        args = parser.parse_args()

        try:
            with open(args.stage_file, 'r', encoding='utf-8') as f:
                file = (line.strip('\n') for line in f.readlines())

                forest_dimension = next(file)
                forest_grid = [list(tuple(line)) for line in file]

                if any((int(forest_dimension[:2]) != len(forest_grid), int(forest_dimension[2:]) != len(forest_grid[0]))):
                    print(f"Error: Forest dimension '{int(forest_dimension[:2]), int(forest_dimension[2:])}' does not match forest grid '{len(forest_grid), len(forest_grid[0])}'.")
                    quit()

                return forest_grid
        except FileNotFoundError:
            print(f"Error: Stage file {args.stage_file} not found.")
            quit()

class Terminal:
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

class Graphics: 
    def ascii_to_ui_and_loc(grid):
        tile = {
        # 'L': 'L',
        # 'T': 'T',
        # '+': '+',
        # 'R': 'R',
        # '~': '~',
        # '_': '_',
        # '.': '.',
        # 'x': 'x',
        # '*': '*'
        'L': '\N{Adult}',
        'T': '\N{evergreen tree}',
        '+': '\N{mushroom}',
        'R': '\N{rock}',
        '~': '\N{large blue square}',
        '_': '\N{white medium square}',
        '.': '　',
        'x': '\N{axe}',
        '*': '\N{fire}'
        }

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'L':
                    loc = (i, j)
                grid[i][j] = tile[grid[i][j]]
        return grid, loc

class Movement:
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

    def is_validtile(grid, tile):
        i, j = tile[0], tile[1]
        if grid[i] in {0, len(grid) - 1} or grid[j] in {0, len(grid[0]) - 1}:
            return False
        return True


forest_main, player_location = Graphics.ascii_to_ui_and_loc(Boot.launch())
print(player_location)
Func.pgrid(forest_main)