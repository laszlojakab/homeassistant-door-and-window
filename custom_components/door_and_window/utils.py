""" The module for utility functions """
import math


def normalize_angle(angle: float) -> float:
    """
    Converts the angle to be between -180 and +180 degrees.

    Args:
        angle:
            The angle to covert

    Returns:
        The angle represented between -180 and +180 degrees.
    """
    angle = angle - math.floor(angle / 360) * 360
    angle = round(angle if angle < 180 else angle - 360, 2)
    return angle
