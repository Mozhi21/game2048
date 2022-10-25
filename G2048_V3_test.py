"""
CS5001/3 Final Project Part1
Mozhi Shen
5-2-2022

This is the Test code for third version of 2048 game.
Everything except GUI and User input was tested here.
Constants are stored in G2048_v3_constant.py
"""
from G2048_v3_main import *
import unittest

random.seed(10)


class MatrixTest(unittest.TestCase):
    def test_init(self):
        g_matrix = Matrix(size=3)
        for i in range(g_matrix.size):
            self.assertEqual([0, 0, 0], g_matrix.data[i])

    def test_add_number(self):
        g_matrix = Matrix(size=3)
        g_matrix.add_number()
        self.assertEqual([[2, 0, 0], [0, 0, 0], [0, 0, 0]], g_matrix.data)
        g_matrix.add_number()
        self.assertEqual([[2, 2, 0], [0, 0, 0], [0, 0, 0]], g_matrix.data)
        g_matrix.add_number()
        self.assertEqual([[2, 2, 0], [0, 0, 0], [0, 0, 2]], g_matrix.data)

        g_matrix.data = [[2, 2, 3], [4, 5, 6], [7, 8, 2]]
        # test if the matrix is full.
        g_matrix.add_number()
        self.assertEqual([[2, 2, 3], [4, 5, 6], [7, 8, 2]], g_matrix.data)

    def test_cover(self):
        g_matrix = Matrix(size=3)
        g_matrix.data = [[2, 2, 3], [4, 5, 6], [7, 8, 2]]
        g_matrix.covert()
        self.assertEqual([[2, 4, 7], [2, 5, 8], [3, 6, 2]], g_matrix.data)

    def test_move(self):
        g_matrix = Matrix(size=4)
        g_matrix.data = [[2, 4, 2, 4], [2, 8, 2, 4],
                         [2, 8, 0, 0], [0, 0, 0, 0]]
        g_matrix.move('r')
        self.assertEqual(
            [[2, 4, 2, 4], [2, 8, 2, 4], [0, 0, 2, 8], [0, 0, 0, 0]],
            g_matrix.data)
        g_matrix.move('d')
        self.assertEqual(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 2, 8], [4, 8, 4, 8]],
            g_matrix.data)
        g_matrix.move('l')
        self.assertEqual(
            [[0, 0, 0, 0], [0, 0, 0, 0], [4, 2, 8, 0], [4, 8, 4, 8]],
            g_matrix.data)
        g_matrix.move('u')
        self.assertEqual(
            [[8, 2, 8, 8], [0, 8, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            g_matrix.data)

    def test_game_over(self):
        g_matrix = Matrix(size=3)
        g_matrix.data = [[16, 2, 8], [2, 16, 2], [2, 4, 2]]
        self.assertEqual(False, g_matrix.game_over())
        self.assertEqual([[16, 2, 8], [2, 16, 2], [2, 4, 2]], g_matrix.data)

        g_matrix.data = [[16, 2, 16], [8, 16, 4], [2, 4, 2]]
        self.assertEqual(True, g_matrix.game_over())
        self.assertEqual([[16, 2, 16], [8, 16, 4], [2, 4, 2]], g_matrix.data)

    def test_get_score(self):
        g_matrix = Matrix(size=5)
        self.assertEqual(0, g_matrix.get_score())
        for i in range(10):
            g_matrix.add_number()
        self.assertEqual(22, g_matrix.get_score())

    def test_get_line(self):
        list1 = [0, 0, 2, 4, 8]
        self.assertEqual(get_line(list1), [2, 4, 8, 0, 0])
        list2 = [2, 2, 4, 4, 0]
        self.assertEqual(get_line(list2), [4, 8, 0, 0, 0])
        list3 = [2, 2, 2, 2, 2]
        self.assertEqual(get_line(list3), [4, 4, 2, 0, 0])
        list4 = [2, 4, 8, 16, 32]
        self.assertEqual(get_line(list4), [2, 4, 8, 16, 32])


def main():
    unittest.main(verbosity=3)


if __name__ == '__main__':
    main()
