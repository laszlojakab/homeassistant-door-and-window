""" Tests for Quadrilateral class. """
import numpy as np

from ...models.quadrilateral import Quadrilateral


def test_quadrilateral_corners():
    """ Tests if the given corners are set. """
    quadrilateral = Quadrilateral([0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0])

    assert np.isclose(quadrilateral.corner_1, [0, 0, 0, 1]).all()
    assert np.isclose(quadrilateral.corner_2, [10, 0, 0, 1]).all()
    assert np.isclose(quadrilateral.corner_3, [10, 10, 0, 1]).all()
    assert np.isclose(quadrilateral.corner_4, [0, 10, 0, 1]).all()


def test_apply_matrix():
    """
    Tests if the specified matrix is
    applied the quadrilateral correctly
    """
    quadrilateral = Quadrilateral([0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0])

    translate_x = 3
    translate_y = 4
    translate_z = -2
    translate_matrix = np.array([
        [1., 0., 0., translate_x],
        [0., 1., 0., translate_y],
        [0., 0., 1., translate_z],
        [0., 0., 0., 1.]
    ])

    translated = quadrilateral.apply_matrix(translate_matrix)

    assert np.isclose(
        translated.corner_1,
        [0 + translate_x, 0 + translate_y, 0 + translate_z, 1]
    ).all()

    assert np.isclose(
        translated.corner_2,
        [10 + translate_x, 0 + translate_y, 0 + translate_z, 1]
    ).all()

    assert np.isclose(
        translated.corner_3,
        [10 + translate_x, 10 + translate_y, 0 + translate_z, 1]
    ).all()

    assert np.isclose(
        translated.corner_4,
        [0 + translate_x, 10 + translate_y, 0 + translate_z, 1]
    ).all()

def test_equality():
    """ Tests the equality of quadrilaterals. """
    quadrilateral_1 = Quadrilateral([0, 0, 0], [1, 2, 3], [4, 5, 6], [7, 8, 9])
    quadrilateral_2 = Quadrilateral([0, 0, 0], [1, 2, 3], [4, 5, 6], [7, 8, 9])
    assert quadrilateral_1 == quadrilateral_2
