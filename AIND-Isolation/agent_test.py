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
        self.small_g = Board(self.p1, self.p2, 4, 4)

    def test_minimax_no_plies(self):
        actual = self.p1.minimax(self.small_g, 1)
        expected = (1,1)
        self.assertEqual(actual, expected)

    def test_minimax_one_ply(self):
        self.small_g.apply_move((1,1))
        actual   = self.p2.minimax(self.small_g, 1)

        # There are other moves that will result in the same
        # heuristic score like (1,2) but this is the first
        # move of that max score that minimax() evaluates
        expected = (2, 1) # There are mul

        self.assertEqual(actual, expected)

    def test_minimax_two_plies(self):
        self.small_g.apply_move((1,1))
        self.small_g.apply_move((2,1))

        expected = (3,2)
        actual   = self.p1.minimax(self.small_g, 1)

        self.assertEqual(expected, actual)

    def test_minimax_more_than_one_ply(self):
        actual = self.p1.minimax(self.small_g, 1)
        expected = (1,1)
        self.assertEqual(actual, expected)

    def test_custom_score_one_ply(self):
        self.small_g.apply_move((1,1))
        print(self.small_g.print_board())

        actual   = game_agent.custom_score(self.small_g, self.p1)
        #P1 has 4 possible moves from a middle square
        #P2 having not yet moved, can occupy any of the remaing 15 square
        expected = -11

        self.assertEqual(actual, expected)

    def custom_score_no_plies(self):
        # In the initial state, each player has the same amount of possible moves
        actual   = game_agent.custom_score(self.small_g, self.p1)
        expected = 0 #16 - 16
        self.assertEqual(actual, expected)

    def custom_score_two_plies(self):
        self.small_g.apply_move((1,1))
        self.small_g.apply_move((0,0))
        actual   = game_agent.custom_score(self.small_g, self.p1)
        expected = 2 #4 - 2
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
