""" Module for DoorAndWindowRectanglesSeenFromSunTransformer class. """
from ..models.door_and_window_rectangles import DoorAndWindowRectangles
from .coordinate_transformations import CoordinateTransformations


# pylint: disable=too-few-public-methods
class DoorAndWindowRectanglesSeenFromSunTransformer():
    """ Responsible for transforming door and window rectangles as seen from the sun's position """

    def __init__(self):
        """ Initialize a new instance of `DoorAndWindowRectanglesSeenFromSunTransformer` class. """
        self._transformations = CoordinateTransformations()

    def transform(
            self,
            door_and_window_rectangles: DoorAndWindowRectangles,
            solar_azimuth: float,
            solar_elevation: float
    ) -> DoorAndWindowRectangles:
        """
        Transforms the specified DoorAndWindowRectangles instance
        as it would be seen from the specified sun position.

        Args:
            door_and_window_rectangles:
                The door and window rectangles to transform.
            solar_azimuth:
                The sun azimuth.
            solar_elevation:
                The sun elevation.

        Returns:
            The transformed DoorAndWindowRectangles instance
            as it would be seen from the specified sun position.
        """

        x_rotation = -solar_elevation
        y_rotation = -solar_azimuth

        rotation_matrix_x = self._transformations.get_rotation_matrix_x(x_rotation)
        rotation_matrix_y = self._transformations.get_rotation_matrix_y(y_rotation)

        transformation_matrix = rotation_matrix_x.dot(rotation_matrix_y)

        return door_and_window_rectangles.apply_matrix(transformation_matrix)
