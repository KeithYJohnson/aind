assignments = []

import re

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [['A1','B2','C3','D4','E5','F6','G7','H8', 'I9'],['A9','B8','C7','D6','E5','F4','G3','H2','I1']]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def shared_peers(a, b):
    """
      Args:
        The keys of two boxes
      Returns:
        The other peers of the peer group that they share: column, row or 3x3 square.
    """
    return set.intersection(peers[a], peers[b])

#credit https://stackoverflow.com/questions/4527942/comparing-two-dictionaries-in-python
def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same

    x = dict(a=1, b=2)
    y = dict(a=2, b=2)
    added, removed, modified, same = dict_compare(x, y)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(dict_grid):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

    #TODO Optimize optimize Optimize
    for key, value in dict_grid.items():
        if len(value) == 2:
            box_peers = peers[key]
            for peer in box_peers:
                if dict_grid[peer] == value:
                    other_peers = shared_peers(key, peer)
                    for other_peer in other_peers:
                        for num in value:
                            if num in dict_grid[other_peer]:
                                dict_grid[other_peer] = re.sub("[{}]".format(num), '', dict_grid[other_peer])

    return dict_grid

def cross(A, B):
    return [s+t for s in A for t in B]

def grid_values(grid_string, boxes):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    assert len(grid_string) == 81, "Input grid must be a string of length 81 (9x9)"
    grid_dict = {}
    for idx, char in enumerate(grid_string):
        if char == '.':
            grid_dict[boxes[idx]] = '123456789'
        else:
            grid_dict[boxes[idx]] = char


    return grid_dict

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


def eliminate(dict_grid):
    dict_grid = naked_twins(dict_grid)
    for key, value in dict_grid.items():
        if len(value) == 1:
            # Peers is built helpers.py and imported from there
            box_peers = peers[key]
            for peer in box_peers:
                prev_val = dict_grid[peer]
                new_val  = prev_val.replace(value, '')
                dict_grid[peer] = new_val

    return dict_grid

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit

    return values

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

def search(dict_grid):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    dict_grid = reduce_puzzle(dict_grid)

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

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    dict_grid = grid_values(grid, boxes)
    result    = search(dict_grid)
    if result:
        return result
    else:
        return False

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    result = solve(diag_sudoku_grid)
    display(result)


    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
