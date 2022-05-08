""" Module for coordinate transformations. """
import math
from typing import Tuple

import numpy as np

# Rotation matrix based on:
# https://www.brainvoyager.com/bv/doc/UsersGuide/CoordsAndTransforms/SpatialTransformationMatrices.html

# pylint: disable=too-few-public-methods
class CoordinateTransformations():
    """ Class for coordinate transformations. """

    @classmethod
    def get_sin_cos(cls, angle: float) -> Tuple[float, float]:
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
        (sin_azimuth, cos_azimuth) = self.get_sin_cos(azimuth)
        (sin_elevation, cos_elevation) = self.get_sin_cos(90 - elevation)

        return (sin_elevation*cos_azimuth, sin_elevation*sin_azimuth, cos_elevation)


    def get_rotation_matrix_x(self, angle: float) -> np.ndarray:
        """
        Gets the rotation matrix for rotating a vector on X axis in 3D
        by the specified angle (in degrees).

        Args:
            angle:
                The angle of rotation in degrees.

        Returns:
            The numpy array contains the rotation matrix.
        """
        (sin, cos) = self.get_sin_cos(angle)

        return np.array([
            [1, 0, 0, 0],
            [0, cos, -sin, 0],
            [0, sin, cos, 0],
            [0, 0, 0, 1]
        ])

    def get_rotation_matrix_y(self, angle: float) -> np.ndarray:
        """
        Gets the rotation matrix for rotating a vector on Y axis in 3D
        by the specified angle (in degrees).

        Args:
            angle:
                The angle of rotation in degrees.

        Returns:
            The numpy array contains the rotation matrix.
        """
        (sin, cos) = self.get_sin_cos(angle)

        return np.array([
            [cos, 0., sin, 0.],
            [0., 1., 0., 0.],
            [-sin, 0., cos, 0.],
            [0., 0., 0., 1.]
        ])

    # pylint: disable=invalid-name
    @classmethod
    def get_translation_matrix(cls, x: float, y: float, z: float) -> np.ndarray:
        """
        Gets the translation matrix for 3D translation

        Args:
            x:
                The translation amount on X axis.
            y:
                The translation amount on Y axis.
            z:
                The translation amount on Z axis.

        Returns:
            The numpy array contains the translation matrix.
        """
        return np.array([
            [1., 0., 0., x],
            [0., 1., 0., y],
            [0., 0., 1., z],
            [0., 0., 0., 1.]
        ])
