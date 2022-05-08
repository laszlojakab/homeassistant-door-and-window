""" Module for DoorAndWindowRectanglesToPolygonsConverter class. """
from typing import Union
from shapely.geometry import Polygon

from ..models.door_and_window_polygons import DoorAndWindowPolygons
from ..models.door_and_window_rectangles import DoorAndWindowRectangles
from ..models.quadrilateral import Quadrilateral

# pylint: disable=too-few-public-methods


class DoorAndWindowRectanglesToPolygonsConverter():
    """ Responsible for converting door and window rectangles to polygons. """

    def convert(self, door_and_window_rectangles: DoorAndWindowRectangles) -> DoorAndWindowPolygons:
        """
        Converts the specified door and window 3D rectangles to
        2D polygons by projecting the coordinates to the (x, y) plane.

        Args:
            door_and_window_rectangles:
                The door and window rectangles to convert

        Returns:
            The DoorAndWindowPolygons which represents the
            door and window rectangles in the (x, y) plane.
        """
        return DoorAndWindowPolygons(
            glazing=self._convert_rectangle_to_polygon(door_and_window_rectangles.glazing),
            outside_left_jamb_wall=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.outside_left_jamb_wall),
            outside_right_jamb_wall=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.outside_right_jamb_wall),
            outside_head_jamb_wall=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.outside_head_jamb_wall),
            outside_stool=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.outside_stool),
            inside_left_jamb_wall=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.inside_left_jamb_wall),
            inside_right_jamb_wall=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.inside_right_jamb_wall),
            inside_head_jamb_wall=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.inside_head_jamb_wall),
            inside_stool=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.inside_stool),
            awning=self._convert_rectangle_to_polygon(
                door_and_window_rectangles.awning)
        )

    @classmethod
    def _convert_rectangle_to_polygon(cls, rectangle: Union[Quadrilateral, None]) -> Polygon:
        return Polygon() if rectangle is None else Polygon([
            rectangle.corner_1[0:2],
            rectangle.corner_2[0:2],
            rectangle.corner_3[0:2],
            rectangle.corner_4[0:2]
        ])
