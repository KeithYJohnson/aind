"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import game_agent
from isolation  import Board
from game_agent import MinimaxPlayer

from pdb import set_trace as st
from importlib import reload


class MinimaxPlayerTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.p1 = MinimaxPlayer()
        self.p2 = MinimaxPlayer()
        self.g  = Board(self.p1, self.p2)

    def test_minimax(self):
        pass

    def test_custom_score(self):
        p1 = self.p1
        p2 = self.p2
        g  = self.g

        # Initial positions
        g.apply_move((0,0))
        g.apply_move((1,1))

        #2 moves for p1, 4 for p2
        actual   = game_agent.custom_score(g, p1)
        expected = -2

        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()
