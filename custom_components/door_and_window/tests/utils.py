""" Module for testing utility functions """
import math
import numpy as np

from ..models.quadrilateral import Quadrilateral


def assert_coordinates_are_close(
    coordinates_1: np.ndarray,
    coordinates_2: np.ndarray,
    prefix_message: str = ''
) -> None:
    """
    Asserts to check if the specified coordinates are close to each other.

    Args:
        coordinates_1
            The first coordinate to compare.
        coordinates_2
            The second coordinate to compare.
        prefix_message
            The prefix to add to assert message.
    """

    assert len(coordinates_1) == len(coordinates_2), \
        'Coordinates length must be the same'

    # pylint: disable=consider-using-enumerate
    for i in range(len(coordinates_1)):
        assert math.isclose(coordinates_1[i], coordinates_2[i], abs_tol=1e-5), \
            f'{prefix_message}Coordinates at {i} index must be ' + \
            f'the same: {coordinates_1}, {coordinates_2}'


def assert_quadrilaterals_are_close(
    quadrilateral_1: Quadrilateral,
    quadrilateral_2: Quadrilateral,
    prefix_message: str = ''
) -> None:
    """
    Asserts for all corners of the specified quadrilaterals
    to check if the corner pairs are close to each other.

    Args:
        quadrilateral_1
            The first quadrilateral to compare.
        quadrilateral_1
            The second quadrilateral to compare.
        prefix_message
            The prefix to add to assert message.
    """

    assert_coordinates_are_close(
        quadrilateral_1.corner_1,
        quadrilateral_2.corner_1,
        f'{prefix_message}1st corners should be the same. '
    )

    assert_coordinates_are_close(
        quadrilateral_1.corner_2,
        quadrilateral_2.corner_2,
        f'{prefix_message}2nd corners should be the same. '
    )

    assert_coordinates_are_close(
        quadrilateral_1.corner_3,
        quadrilateral_2.corner_3,
        f'{prefix_message}3rd corners should be the same. '
    )

    assert_coordinates_are_close(
        quadrilateral_1.corner_4,
        quadrilateral_2.corner_4,
        f'{prefix_message}4th corners should be the same. '
    )
