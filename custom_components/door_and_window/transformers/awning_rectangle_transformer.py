""" Module for AwningToRectangleTransformer class. """
from __future__ import annotations

from typing import TYPE_CHECKING

from ..models.quadrilateral import Quadrilateral
from .coordinate_transformations import CoordinateTransformations

if TYPE_CHECKING:
    from ..models.door_and_window import DoorAndWindow

# pylint: disable=too-few-public-methods
class AwningRectangleTransformer():
    """
    Responsible for transforming the rectangle of an awning into the
    coordinate space of the door and window.
    """

    def __init__(self):
        """
        Initialize a new instance of AwningRectangleTransformer class.
        """
        self._transformations = CoordinateTransformations()

    def transform(
        self,
        awning_rectangle: Quadrilateral,
        door_and_window: DoorAndWindow
    ) -> Quadrilateral:
        """
        Transforms the specified awning rectangle coordinates relative
        to DoorAndWindow instance coordinates.

        Args:
            awning_rectangle:
                The Quadrilateral instance of the awning to transform.
            door_and_window:
                The DoorAndWindow instance which belongs to the awning.

        Returns:
            The modified rectangle which coordinates are relative
            to the specified DoorAndWindow instance coordinates.
        """

        # The initial origin coordinates of the awning
        # pylint: disable=invalid-name
        z = door_and_window.outside_depth
        # pylint: disable=invalid-name
        y = door_and_window.height

        (sin, cos) = self._transformations.get_sin_cos(90 - door_and_window.tilt)

        # The initial origin rotated to:
        rotated_z = cos*z - sin*y
        rotated_y = sin*z + cos*y

        # The translation required for awning
        delta_z = z - rotated_z
        delta_y = y - rotated_y

        rotation_matrix = self._transformations.get_rotation_matrix_y(door_and_window.azimuth)
        translate_matrix = self._transformations.get_translation_matrix(
            0,
            door_and_window.height + door_and_window.parapet_wall_height - delta_y,
            delta_z - door_and_window.outside_depth
        )

        return awning_rectangle.apply_matrix(rotation_matrix.dot(translate_matrix))
