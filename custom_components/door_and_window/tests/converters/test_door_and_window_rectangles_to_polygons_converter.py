""" Module for DoorAndWindowRectanglesToPolygonsConverter class tests. """

from shapely.geometry import Polygon

from ...converters.door_and_window_rectangles_to_polygons_converter import \
    DoorAndWindowRectanglesToPolygonsConverter
from ...models.door_and_window_rectangles import DoorAndWindowRectangles
from ...models.quadrilateral import Quadrilateral


def test_door_and_window_rectangles_to_polygons_converter():
    """ Tests if the converter returns the 3D coordinates in 2 polygons. """

    door_and_window_rectangles = DoorAndWindowRectangles(
        Quadrilateral([0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        Quadrilateral([1, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        Quadrilateral([2, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        Quadrilateral([3, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        Quadrilateral([4, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        Quadrilateral([5, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        Quadrilateral([6, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        Quadrilateral([7, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        Quadrilateral([8, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
        # TODO: add tests for awning
        None
    )

    converter = DoorAndWindowRectanglesToPolygonsConverter()
    door_and_window_polygons = converter.convert(door_and_window_rectangles)

    assert door_and_window_polygons.glazing == \
        Polygon([(0, 1), (3, 4), (6, 7), (9, 10)])
    assert door_and_window_polygons.outside_left_jamb_wall == \
        Polygon([(1, 1), (3, 4), (6, 7), (9, 10)])
    assert door_and_window_polygons.outside_right_jamb_wall == \
        Polygon([(2, 1), (3, 4), (6, 7), (9, 10)])
    assert door_and_window_polygons.outside_head_jamb_wall == \
        Polygon([(3, 1), (3, 4), (6, 7), (9, 10)])
    assert door_and_window_polygons.outside_stool == \
        Polygon([(4, 1), (3, 4), (6, 7), (9, 10)])
    assert door_and_window_polygons.inside_left_jamb_wall == \
        Polygon([(5, 1), (3, 4), (6, 7), (9, 10)])
    assert door_and_window_polygons.inside_right_jamb_wall == \
        Polygon([(6, 1), (3, 4), (6, 7), (9, 10)])
    assert door_and_window_polygons.inside_head_jamb_wall == \
        Polygon([(7, 1), (3, 4), (6, 7), (9, 10)])
    assert door_and_window_polygons.inside_stool == \
        Polygon([(8, 1), (3, 4), (6, 7), (9, 10)])
