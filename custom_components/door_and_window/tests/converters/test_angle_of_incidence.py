""" Tests for angle of incidence """
# pylint: disable=missing-function-docstring

import math
from ...converters.angle_of_incidence import get_angle_of_incidence


def test_angle_of_incidence():
    assert math.isclose(get_angle_of_incidence(0, 0, 0, 90), 0, abs_tol=1e-5)

    assert math.isclose(get_angle_of_incidence(0, 0, 30, 90), 30, abs_tol=1e-5)

    assert math.isclose(get_angle_of_incidence(0, 0, 0, 80), 10, abs_tol=1e-5)

    assert math.isclose(get_angle_of_incidence(0, 20, 0, 90), 20, abs_tol=1e-5)

    assert math.isclose(get_angle_of_incidence(0, 20, 0, 70), 0, abs_tol=1e-5)

    assert math.isclose(get_angle_of_incidence(45, 0, 0, 90), 45, abs_tol=1e-5)

    assert math.isclose(get_angle_of_incidence(-50, 0, 0, 90), 50, abs_tol=1e-5)
