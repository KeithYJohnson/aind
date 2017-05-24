from utils         import *
from reduce_value import reduce_value
from ipdb import set_trace as st

from utils import *

def search(dict_grid):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    dict_grid = reduce_value(dict_grid)

    if not dict_grid:
        return False
    elif all(len(dict_grid[s]) == 1 for s in boxes):
        return dict_grid


    boxes_asc  = sorted(dict_grid, key=lambda k: len(dict_grid[k]))
    min_digits_box = None

    for idx, box in enumerate(boxes_asc):
        if len(dict_grid[box]) > 1:
            min_digits_box = boxes_asc[idx]


    for possible_digit in dict_grid[min_digits_box]:
        copy                 = dict_grid.copy()
        copy[min_digits_box] = possible_digit
        result               = search(copy)
        if result:
            return result
