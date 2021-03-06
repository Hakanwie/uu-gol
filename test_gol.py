import gol
import numpy as np


def progressed_board():

    return np.array([[0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 1., 0., 1., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
                     [0., 1., 0., 0., 0., 0., 0., 0., 1., 0.],
                     [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                     [0., 1., 0., 0., 0., 0., 0., 0., 1., 0.],
                     [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
                     [0., 0., 1., 0., 0., 0., 1., 0., 0., 0.],
                     [0., 0., 0., 1., 0., 1., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.]])


def test_gol():
    board = gol.cross(10)
    assert np.array_equal(gol.progress(board), progressed_board())
