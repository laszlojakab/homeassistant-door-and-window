# pylint: disable=missing-function-docstring
"""Test module for `DoorAndWindow` class."""

from shapely.geometry import Polygon

from ...models.door_and_window_polygons import DoorAndWindowPolygons


def test_door_and_window_polygons_properties():
    glazing = Polygon([(0, 0), (1, 0), (1, 1)])
    outside_left_jamb_wall = Polygon([(0, 1), (1, 0), (1, 1)])
    outside_right_jamb_wall = Polygon([(0, 2), (1, 0), (1, 1)])
    outside_head_jamb_wall = Polygon([(0, 3), (1, 0), (1, 1)])
    outside_stool = Polygon([(0, 4), (1, 0), (1, 1)])
    inside_left_jamb_wall = Polygon([(0, 5), (1, 0), (1, 1)])
    inside_right_jamb_wall = Polygon([(0, 6), (1, 0), (1, 1)])
    inside_head_jamb_wall = Polygon([(0, 7), (1, 0), (1, 1)])
    inside_stool = Polygon([(0, 8), (1, 0), (1, 1)])
    awning = Polygon([(0, 9), (1, 0), (1, 1)])

    door_and_window_polygons = DoorAndWindowPolygons(
        glazing,
        outside_left_jamb_wall,
        outside_right_jamb_wall,
        outside_head_jamb_wall,
        outside_stool,
        inside_left_jamb_wall,
        inside_right_jamb_wall,
        inside_head_jamb_wall,
        inside_stool,
        awning
    )

    assert door_and_window_polygons.glazing == glazing
    assert door_and_window_polygons.outside_left_jamb_wall == outside_left_jamb_wall
    assert door_and_window_polygons.outside_right_jamb_wall == outside_right_jamb_wall
    assert door_and_window_polygons.outside_head_jamb_wall == outside_head_jamb_wall
    assert door_and_window_polygons.outside_stool == outside_stool
    assert door_and_window_polygons.inside_left_jamb_wall == inside_left_jamb_wall
    assert door_and_window_polygons.inside_right_jamb_wall == inside_right_jamb_wall
    assert door_and_window_polygons.inside_head_jamb_wall == inside_head_jamb_wall
    assert door_and_window_polygons.inside_stool == inside_stool
    assert door_and_window_polygons.awning == awning
