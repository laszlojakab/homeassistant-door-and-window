""" Module contains DoorAndWindowPolygons class. """
from typing import Final
from shapely.geometry import Polygon

# pylint: disable=too-many-instance-attributes, too-few-public-methods
class DoorAndWindowPolygons:
    """
    Represents a door and window parts as polygons in 2D space.

    Attributes:
        glazing:
            The polygon represents the glazing.
        outside_left_jamb_wall:
            The polygon represents the left outside jamb wall.
        outside_right_jamb_wall:
            The polygon represents the right outside jamb wall.
        outside_head_jamb_wall:
            The polygon represents the head outside jamb wall.
        outside_stool:
            The polygon represents outside stool.
        inside_left_jamb_wall:
            The polygon represents the left inside jamb wall.
        inside_right_jamb_wall:
            The polygon represents the right inside jamb wall.
        inside_head_jamb_wall:
            The polygon represents the head inside jamb wall.
        inside_stool:
            The polygon represents inside stool.
        awning:
            The polygon represents the awning.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        glazing: Polygon,
        outside_left_jamb_wall: Polygon,
        outside_right_jamb_wall: Polygon,
        outside_head_jamb_wall: Polygon,
        outside_stool: Polygon,
        inside_left_jamb_wall: Polygon,
        inside_right_jamb_wall: Polygon,
        inside_head_jamb_wall: Polygon,
        inside_stool: Polygon,
        awning: Polygon
    ):
        """
        Initialize a new instance of DoorAndWindowRectangles class.

        Args:
            glazing:
                The polygon represents the glazing.
            outside_left_jamb_wall:
                The polygon represents the left outside jamb wall.
            outside_right_jamb_wall:
                The polygon represents the right outside jamb wall.
            outside_head_jamb_wall:
                The polygon represents the head outside jamb wall.
            outside_stool:
                The polygon represents outside stool.
            inside_left_jamb_wall:
                The polygon represents the left inside jamb wall.
            inside_right_jamb_wall:
                The polygon represents the right inside jamb wall.
            inside_head_jamb_wall:
                The polygon represents the head inside jamb wall.
            inside_stool:
                The polygon represents inside stool.
            awning:
                The polygon represents the awning. If no awning then polygon is empty.
        """
        self.glazing: Final[Polygon] = glazing
        self.outside_left_jamb_wall: Final[Polygon] = outside_left_jamb_wall
        self.outside_right_jamb_wall: Final[Polygon] = outside_right_jamb_wall
        self.outside_head_jamb_wall: Final[Polygon] = outside_head_jamb_wall
        self.outside_stool: Final[Polygon] = outside_stool
        self.inside_left_jamb_wall: Final[Polygon] = inside_left_jamb_wall
        self.inside_right_jamb_wall: Final[Polygon] = inside_right_jamb_wall
        self.inside_head_jamb_wall: Final[Polygon] = inside_head_jamb_wall
        self.inside_stool: Final[Polygon] = inside_stool
        self.awning: Final[Polygon] = awning
