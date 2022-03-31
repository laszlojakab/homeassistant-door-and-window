""" Tests for coordinate transformations """
# pylint: disable=missing-function-docstring

import numpy as np

from ..coordinate_transformations import CoordinateTransformations


def test_convert_polar_coordinates_to_rectanglar():
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
