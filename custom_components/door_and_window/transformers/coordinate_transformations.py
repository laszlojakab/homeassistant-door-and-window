""" Module for coordinate transformations. """
import math
from typing import Tuple

class CoordinateTransformations():
    """ Class for coordinate transformations. """

    def _get_sin_cos(self, angle: float) -> Tuple[float, float]:
        """
        Gets the sine and the cosine of the specified angle.

        Args:
            angle:
                The angle in degrees.
        Returns:
            The tuple of sine and cosine value.
        """
        rad_angle = math.radians(angle)
        return (math.sin(rad_angle), math.cos(rad_angle))

    def convert_polar_coordinates_to_rectanglar(
        self,
        azimuth: float,
        elevation: float
    ) -> Tuple[float, float, float]:
        """
        Converts polar coordinates to rectangular coordinates.

        Args:
            azimuth:
                The azimuth coordinate.
            elevation:
                The elevation coordinate.

        Returns:
            The 3D rectangular coordinate correspond to specified polar coordinate.
        """
        (sin_azimuth, cos_azimuth) = self._get_sin_cos(azimuth)
        (sin_elevation, cos_elevation) = self._get_sin_cos(90 - elevation)

        return (sin_elevation*cos_azimuth, sin_elevation*sin_azimuth, cos_elevation)
