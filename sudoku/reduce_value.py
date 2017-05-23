from utils       import *
from eliminate   import eliminate
from only_choice import only_choice
from grid_values import grid_values

def reduce_puzzle(dict_grid):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in dict_grid.keys() if len(dict_grid[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        dict_grid = eliminate(dict_grid)

        # Your code here: Use the Only Choice Strategy
        dict_grid = only_choice(dict_grid)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in dict_grid.keys() if len(dict_grid[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in dict_grid.keys() if len(dict_grid[box]) == 0]):
            return False

    return dict_grid

if __name__ == '__main__':
    string_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    dict_grid   = grid_values(string_grid, boxes)
    print(reduce_puzzle(dict_grid))
