""" Tests for coordinate transformations """
import numpy as np

from ...transformers.coordinate_transformations import CoordinateTransformations


def test_convert_polar_coordinates_to_rectanglar():
    """ Tests the `convert_polar_coordinates_to_rectanglar` method """
    transformations = CoordinateTransformations()

    assert np.isclose(
        transformations.convert_polar_coordinates_to_rectanglar(0, 0),
        (1, 0, 0)
    ).all()

    assert np.isclose(
        transformations.convert_polar_coordinates_to_rectanglar(0, 90),
        (0, 0, 1)
    ).all()

    assert np.isclose(
        transformations.convert_polar_coordinates_to_rectanglar(0, -90),
        (0, 0, -1)
    ).all()

    assert np.isclose(
        transformations.convert_polar_coordinates_to_rectanglar(90, 0),
        (0, 1, 0)
    ).all()


def test_rotation_matrix_x():
    """ Tests if the rotation matrix around X axis is valid """

    transformations = CoordinateTransformations()

    assert np.isclose(
        transformations.get_rotation_matrix_x(0),
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    ).all()

    assert np.isclose(
        transformations.get_rotation_matrix_x(90),
        [
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ]
    ).all()

def test_rotation_matrix_y():
    """ Tests if the rotation matrix around Y axis is valid """

    transformations = CoordinateTransformations()

    assert np.isclose(
        transformations.get_rotation_matrix_y(0),
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    ).all()

    assert np.isclose(
        transformations.get_rotation_matrix_y(90),
        [
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 0, 1]
        ]
    ).all()

def test_translation_matrix():
    """ Tests if the translation matrix is valid """

    transformations = CoordinateTransformations()

    assert np.isclose(
        transformations.get_translation_matrix(0, 0, 0),
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    ).all()

    assert np.isclose(
        transformations.get_translation_matrix(1, 2, 3),
        [
            [1, 0, 0, 1],
            [0, 1, 0, 2],
            [0, 0, 1, 3],
            [0, 0, 0, 1]
        ]
    ).all()
