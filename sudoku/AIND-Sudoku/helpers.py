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
