""" The module contains DoorAndWindowRectangles class. """
from typing import Final

import numpy as np

from ..models.quadrilateral import Quadrilateral

# pylint: disable=too-many-instance-attributes, too-few-public-methods
class DoorAndWindowRectangles:
    """
    Represents a door and window parts as rectangles in the 3D space.

    Attributes:
        glazing:
            The rectangle represents the glazing.
        outside_left_jamb_wall:
            The rectangle represents the left outside jamb wall.
        outside_right_jamb_wall:
            The rectangle represents the right outside jamb wall.
        outside_head_jamb_wall:
            The rectangle represents the head outside jamb wall.
        outside_stool:
            The rectangle represents outside stool.
        inside_left_jamb_wall:
            The rectangle represents the left inside jamb wall.
        inside_right_jamb_wall:
            The rectangle represents the right inside jamb wall.
        inside_head_jamb_wall:
            The rectangle represents the head inside jamb wall.
        inside_stool:
            The rectangle represents inside stool.
    """
    # pylint: disable=too-many-arguments
    def __init__(
        self,
        glazing: Quadrilateral,
        outside_left_jamb_wall: Quadrilateral,
        outside_right_jamb_wall: Quadrilateral,
        outside_head_jamb_wall: Quadrilateral,
        outside_stool: Quadrilateral,
        inside_left_jamb_wall: Quadrilateral,
        inside_right_jamb_wall: Quadrilateral,
        inside_head_jamb_wall: Quadrilateral,
        inside_stool: Quadrilateral
    ):
        """
        Initialize a new instance of DoorAndWindowRectangles class.

        Args:
            glazing:
                The rectangle represents the glazing.
            outside_left_jamb_wall:
                The rectangle represents the left outside jamb wall.
            outside_right_jamb_wall:
                The rectangle represents the right outside jamb wall.
            outside_head_jamb_wall:
                The rectangle represents the head outside jamb wall.
            outside_stool:
                The rectangle represents outside stool.
            inside_left_jamb_wall:
                The rectangle represents the left inside jamb wall.
            inside_right_jamb_wall:
                The rectangle represents the right inside jamb wall.
            inside_head_jamb_wall:
                The rectangle represents the head inside jamb wall.
            inside_stool:
                The rectangle represents inside stool.
        """
        self.glazing: Final[Quadrilateral] = glazing
        self.outside_left_jamb_wall: Final[Quadrilateral] = outside_left_jamb_wall
        self.outside_right_jamb_wall: Final[Quadrilateral] = outside_right_jamb_wall
        self.outside_head_jamb_wall: Final[Quadrilateral] = outside_head_jamb_wall
        self.outside_stool: Final[Quadrilateral] = outside_stool
        self.inside_left_jamb_wall: Final[Quadrilateral] = inside_left_jamb_wall
        self.inside_right_jamb_wall: Final[Quadrilateral] = inside_right_jamb_wall
        self.inside_head_jamb_wall: Final[Quadrilateral] = inside_head_jamb_wall
        self.inside_stool: Final[Quadrilateral] = inside_stool

    def apply_matrix(self, transformation_matrix: np.ndarray) -> None:
        """
        Applies the specified transformation matrix to all the rectangles
        and returns a new instance of DoorAndWindowRectangles with these transformed faces.

        Args:
            transformation_matrix
                The 4x4 transformation matrix to apply to rectangles.

        Returns:
            The transformed door and window rectangles.
        """
        return DoorAndWindowRectangles(
            glazing=self.glazing.apply_matrix(transformation_matrix),
            outside_left_jamb_wall=self.outside_left_jamb_wall.apply_matrix(transformation_matrix),
            outside_right_jamb_wall=self.outside_right_jamb_wall.apply_matrix(
                transformation_matrix),
            outside_head_jamb_wall=self.outside_head_jamb_wall.apply_matrix(transformation_matrix),
            outside_stool=self.outside_stool.apply_matrix(transformation_matrix),
            inside_left_jamb_wall=self.inside_left_jamb_wall.apply_matrix(transformation_matrix),
            inside_right_jamb_wall=self.inside_right_jamb_wall.apply_matrix(transformation_matrix),
            inside_head_jamb_wall=self.inside_head_jamb_wall.apply_matrix(transformation_matrix),
            inside_stool=self.inside_stool.apply_matrix(transformation_matrix)
        )
