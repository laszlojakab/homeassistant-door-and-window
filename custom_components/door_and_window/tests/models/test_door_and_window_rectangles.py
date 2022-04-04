""" Tests for DoorAndWindowRectangles class. """
import numpy as np

from ...models.quadrilateral import Quadrilateral
from ...models.door_and_window_rectangles import DoorAndWindowRectangles


def test_attributes():
    """ Tests if the attributes are the same as set in the __init__ """
    door_and_window_rectangles = DoorAndWindowRectangles(
        glazing=Quadrilateral([0, 0, 0], [0, 10, 0], [5, 10, 15], [3, 4, 5]),
        outside_left_jamb_wall=Quadrilateral([1, 0, 0], [1, 10, 0], [1, 10, 15], [1, 4, 5]),
        outside_right_jamb_wall=Quadrilateral([2, 0, 0], [2, 10, 0], [2, 10, 15], [2, 4, 5]),
        outside_head_jamb_wall=Quadrilateral([3, 0, 0], [3, 10, 0], [3, 10, 15], [3, 4, 5]),
        outside_stool=Quadrilateral([4, 0, 0], [4, 10, 0], [4, 10, 15], [4, 4, 5]),
        inside_left_jamb_wall=Quadrilateral([5, 0, 0], [5, 10, 0], [5, 10, 15], [5, 4, 5]),
        inside_right_jamb_wall=Quadrilateral([6, 0, 0], [6, 10, 0], [6, 10, 15], [6, 4, 5]),
        inside_head_jamb_wall=Quadrilateral([7, 0, 0], [7, 10, 0], [7, 10, 15], [7, 4, 5]),
        inside_stool=Quadrilateral([8, 0, 0], [8, 10, 0], [8, 10, 15], [8, 4, 5]),
    )

    assert door_and_window_rectangles.glazing == Quadrilateral(
        [0, 0, 0],
        [0, 10, 0],
        [5, 10, 15],
        [3, 4, 5]
    )
    assert door_and_window_rectangles.outside_left_jamb_wall == Quadrilateral(
        [1, 0, 0],
        [1, 10, 0],
        [1, 10, 15],
        [1, 4, 5]
    )
    assert door_and_window_rectangles.outside_right_jamb_wall == Quadrilateral(
        [2, 0, 0],
        [2, 10, 0],
        [2, 10, 15],
        [2, 4, 5]
    )
    assert door_and_window_rectangles.outside_head_jamb_wall == Quadrilateral(
        [3, 0, 0],
        [3, 10, 0],
        [3, 10, 15],
        [3, 4, 5]
    )
    assert door_and_window_rectangles.outside_stool == Quadrilateral(
        [4, 0, 0],
        [4, 10, 0],
        [4, 10, 15],
        [4, 4, 5]
    )
    assert door_and_window_rectangles.inside_left_jamb_wall == Quadrilateral(
        [5, 0, 0],
        [5, 10, 0],
        [5, 10, 15],
        [5, 4, 5]
    )
    assert door_and_window_rectangles.inside_right_jamb_wall == Quadrilateral(
        [6, 0, 0],
        [6, 10, 0],
        [6, 10, 15],
        [6, 4, 5]
    )
    assert door_and_window_rectangles.inside_head_jamb_wall == Quadrilateral(
        [7, 0, 0],
        [7, 10, 0],
        [7, 10, 15],
        [7, 4, 5]
    )

    assert door_and_window_rectangles.inside_stool == Quadrilateral(
        [8, 0, 0],
        [8, 10, 0],
        [8, 10, 15],
        [8, 4, 5]
    )


def test_apply_matrix():
    """ Tests if the apply_matrix called to all the rectangles in the instance. """
    door_and_window_rectangles = DoorAndWindowRectangles(
        glazing=Quadrilateral([0, 0, 0], [0, 1, 0], [5, 1, 6], [3, 4, 5]),
        outside_left_jamb_wall=Quadrilateral([1, 0, 0], [1, 1, 0], [1, 8, 6], [1, 4, 5]),
        outside_right_jamb_wall=Quadrilateral([2, 0, 0], [2, 8, 0], [2, 8, 6], [2, 4, 5]),
        outside_head_jamb_wall=Quadrilateral([3, 0, 0], [3, 8, 0], [3, 8, 6], [3, 4, 5]),
        outside_stool=Quadrilateral([4, 0, 0], [4, 8, 0], [4, 8, 6], [4, 4, 5]),
        inside_left_jamb_wall=Quadrilateral([5, 0, 0], [5, 8, 0], [5, 8, 6], [5, 4, 5]),
        inside_right_jamb_wall=Quadrilateral([6, 0, 0], [6, 8, 0], [6, 8, 6], [6, 4, 5]),
        inside_head_jamb_wall=Quadrilateral([7, 0, 0], [7, 8, 0], [7, 8, 6], [7, 4, 5]),
        inside_stool=Quadrilateral([8, 0, 0], [8, 8, 0], [8, 8, 6], [8, 4, 5]),
    )

    translate_x = 3
    translate_y = 4
    translate_z = -2
    translate_matrix = np.array([
        [1., 0., 0., translate_x],
        [0., 1., 0., translate_y],
        [0., 0., 1., translate_z],
        [0., 0., 0., 1.]
    ])

    translated_door_and_window_rectangles = door_and_window_rectangles.apply_matrix(
        translate_matrix
    )
    assert translated_door_and_window_rectangles.glazing == Quadrilateral(
        [0 + translate_x, 0 + translate_y, 0 + translate_z],
        [0 + translate_x, 1 + translate_y, 0 + translate_z],
        [5 + translate_x, 1 + translate_y, 6 + translate_z],
        [3 + translate_x, 4 + translate_y, 5 + translate_z]
    )
    assert translated_door_and_window_rectangles.outside_left_jamb_wall == Quadrilateral(
        [1 + translate_x, 0 + translate_y, 0 + translate_z],
        [1 + translate_x, 1 + translate_y, 0 + translate_z],
        [1 + translate_x, 8 + translate_y, 6 + translate_z],
        [1 + translate_x, 4 + translate_y, 5 + translate_z]
    )
    assert translated_door_and_window_rectangles.outside_right_jamb_wall == Quadrilateral(
        [2 + translate_x, 0 + translate_y, 0 + translate_z],
        [2 + translate_x, 8 + translate_y, 0 + translate_z],
        [2 + translate_x, 8 + translate_y, 6 + translate_z],
        [2 + translate_x, 4 + translate_y, 5 + translate_z]
    )
    assert translated_door_and_window_rectangles.outside_head_jamb_wall == Quadrilateral(
        [3 + translate_x, 0 + translate_y, 0 + translate_z],
        [3 + translate_x, 8 + translate_y, 0 + translate_z],
        [3 + translate_x, 8 + translate_y, 6 + translate_z],
        [3 + translate_x, 4 + translate_y, 5 + translate_z]
    )
    assert translated_door_and_window_rectangles.outside_stool == Quadrilateral(
        [4 + translate_x, 0 + translate_y, 0 + translate_z],
        [4 + translate_x, 8 + translate_y, 0 + translate_z],
        [4 + translate_x, 8 + translate_y, 6 + translate_z],
        [4 + translate_x, 4 + translate_y, 5 + translate_z]
    )
    assert translated_door_and_window_rectangles.inside_left_jamb_wall == Quadrilateral(
        [5 + translate_x, 0 + translate_y, 0 + translate_z],
        [5 + translate_x, 8 + translate_y, 0 + translate_z],
        [5 + translate_x, 8 + translate_y, 6 + translate_z],
        [5 + translate_x, 4 + translate_y, 5 + translate_z]
    )
    assert translated_door_and_window_rectangles.inside_right_jamb_wall == Quadrilateral(
        [6 + translate_x, 0 + translate_y, 0 + translate_z],
        [6 + translate_x, 8 + translate_y, 0 + translate_z],
        [6 + translate_x, 8 + translate_y, 6 + translate_z],
        [6 + translate_x, 4 + translate_y, 5 + translate_z]
    )
    assert translated_door_and_window_rectangles.inside_head_jamb_wall == Quadrilateral(
        [7 + translate_x, 0 + translate_y, 0 + translate_z],
        [7 + translate_x, 8 + translate_y, 0 + translate_z],
        [7 + translate_x, 8 + translate_y, 6 + translate_z],
        [7 + translate_x, 4 + translate_y, 5 + translate_z]
    )

    assert translated_door_and_window_rectangles.inside_stool == Quadrilateral(
        [8 + translate_x, 0 + translate_y, 0 + translate_z],
        [8 + translate_x, 8 + translate_y, 0 + translate_z],
        [8 + translate_x, 8 + translate_y, 6 + translate_z],
        [8 + translate_x, 4 + translate_y, 5 + translate_z]
    )
