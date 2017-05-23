from utils import *
from grid_values import grid_values

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    for key, value in dict_grid.items():
        if len(value) == 1:
            # Peers is built utils.py and imported from there
            box_peers = peers[key]
            for peer in box_peers:
                prev_val = dict_grid[peer]
                new_val  = prev_val.replace(value, '')
                dict_grid[peer] = new_val

                return dict_grid

    return dict_grid

if __name__ == '__main__':
    string_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    dict_grid   = grid_values(string_grid, boxes)
    print(eliminate(dict_grid))
