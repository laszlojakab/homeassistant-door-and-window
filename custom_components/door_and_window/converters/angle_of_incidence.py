""" The module for calculating angle of incidence. """
import math

import numpy as np

from ..transformers.coordinate_transformations import CoordinateTransformations


def get_angle_of_incidence(
    solar_azimuth: float,
    solar_elevation: float,
    door_and_window_azimuth: float,
    door_and_window_tilt: float
):
    """
    Gets the angle of incidence. This is tha angle between the sun ray and the window face.

    Args:
        solar_azimuth:
            The sun azimuth.
        solar_elevation:
            The sun elevation.
        door_and_window_azimuth:
            The door and window azimuth.
        door_and_window_elevation:
            The door and window elevation.

    Returns:
        The angle of incidence.
    """
    transformations = CoordinateTransformations()
    sun_vector = np.array(transformations.convert_polar_coordinates_to_rectanglar(
        solar_azimuth, solar_elevation))
    door_and_window_vector = np.array(transformations.convert_polar_coordinates_to_rectanglar(
        door_and_window_azimuth, 90 - door_and_window_tilt))

    angle_between_sun_and_door_and_window_face = math.degrees(
        math.acos(door_and_window_vector.dot(sun_vector)))
    return angle_between_sun_and_door_and_window_face
