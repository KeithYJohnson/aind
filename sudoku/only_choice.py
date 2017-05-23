from utils       import *
from grid_values import grid_values
from eliminate   import eliminate
from collections import defaultdict

def only_choice(dict_grid):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """

    for unit in unitlist:
        counts = defaultdict(lambda: 0)
        for box in unit:
            box_vals = dict_grid[box]
            for possible_digit in box_vals:
                counts[possible_digit] += 1

        for key, value in counts.items():
            if value == 1:
                for box in unit:
                    if key in dict_grid[box]:
                        dict_grid[box] = key

    return dict_grid





if __name__ == '__main__':
    string_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    dict_grid   = grid_values(string_grid, boxes)
    dict_grid = eliminate(dict_grid)
    only_choice(dict_grid)
