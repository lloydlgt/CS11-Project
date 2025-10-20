from argparse import ArgumentParser
import os

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
