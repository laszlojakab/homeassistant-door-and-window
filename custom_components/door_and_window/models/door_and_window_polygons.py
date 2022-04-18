""" Module contains DoorAndWindowPolygons class. """
from shapely.geometry import Polygon

# pylint: disable=too-many-instance-attributes
class DoorAndWindowPolygons:
    """ Represents a door and window parts as polygons in 2D space. """

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
        inside_stool: Polygon
    ):
        """
        Initialize a new instance of DoorAndWindowRectangles class.

        Parameters
        ----------
        glazing
            The polygon represents the glazing.
        outside_left_jamb_wall
            The polygon represents the left outside jamb wall.
        outside_right_jamb_wall
            The polygon represents the right outside jamb wall.
        outside_head_jamb_wall
            The polygon represents the head outside jamb wall.
        outside_stool
            The polygon represents outside stool.
        inside_left_jamb_wall
            The polygon represents the left inside jamb wall.
        inside_right_jamb_wall
            The polygon represents the right inside jamb wall.
        inside_head_jamb_wall
            The polygon represents the head inside jamb wall.
        inside_stool
            The polygon represents inside stool.
        """
        self._glazing = glazing
        self._outside_left_jamb_wall = outside_left_jamb_wall
        self._outside_right_jamb_wall = outside_right_jamb_wall
        self._outside_head_jamb_wall = outside_head_jamb_wall
        self._outside_stool = outside_stool
        self._inside_left_jamb_wall = inside_left_jamb_wall
        self._inside_right_jamb_wall = inside_right_jamb_wall
        self._inside_head_jamb_wall = inside_head_jamb_wall
        self._inside_stool = inside_stool

    @property
    def glazing(self) -> Polygon:
        """ Gets the polygon represents the glazing. """
        return self._glazing

    @property
    def outside_left_jamb_wall(self) -> Polygon:
        """ Gets the polygon represents outside left jamb wall. """
        return self._outside_left_jamb_wall

    @property
    def outside_right_jamb_wall(self) -> Polygon:
        """ Gets the polygon represents outside right jamb wall. """
        return self._outside_right_jamb_wall

    @property
    def outside_head_jamb_wall(self) -> Polygon:
        """ Gets the polygon represents outside head jamb wall. """
        return self._outside_head_jamb_wall

    @property
    def outside_stool(self) -> Polygon:
        """ Gets the polygon represents outside stool. """
        return self._outside_stool

    @property
    def inside_left_jamb_wall(self) -> Polygon:
        """ Gets the polygon represents inside left jamb wall. """
        return self._inside_left_jamb_wall

    @property
    def inside_right_jamb_wall(self) -> Polygon:
        """ Gets the polygon represents inside right jamb wall. """
        return self._inside_right_jamb_wall

    @property
    def inside_head_jamb_wall(self) -> Polygon:
        """ Gets the polygon represents inside head jamb wall. """
        return self._inside_head_jamb_wall

    @property
    def inside_stool(self) -> Polygon:
        """ Gets the polygon represents inside stool. """
        return self._inside_stool
