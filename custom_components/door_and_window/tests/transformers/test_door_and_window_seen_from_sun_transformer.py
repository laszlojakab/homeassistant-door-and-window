""" Tests for DoorAndWindowRectanglesSeenFromSunTransformer class. """
from ...tests.utils import assert_quadrilaterals_are_close
from ...models.quadrilateral import Quadrilateral
from ...models.door_and_window_rectangles import DoorAndWindowRectangles
from ...transformers.door_and_window_seen_from_sun_transformer import \
    DoorAndWindowRectanglesSeenFromSunTransformer


def test_door_and_window_seen_from_sun_transformer_if_sun_is_in_front():
    """
    Tests the DoorAndWindowRectanglesSeenFromSunTransformer class
    if sun is in front of the door and window.
    """
    transformer = DoorAndWindowRectanglesSeenFromSunTransformer()

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
        Quadrilateral([9, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
    )

    door_and_window_rectangles_seen_from_sun = transformer.transform(
        door_and_window_rectangles, 0, 0)

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.glazing,
        door_and_window_rectangles_seen_from_sun.glazing
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.inside_head_jamb_wall,
        door_and_window_rectangles_seen_from_sun.inside_head_jamb_wall
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.inside_left_jamb_wall,
        door_and_window_rectangles_seen_from_sun.inside_left_jamb_wall
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.inside_right_jamb_wall,
        door_and_window_rectangles_seen_from_sun.inside_right_jamb_wall
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.inside_stool,
        door_and_window_rectangles_seen_from_sun.inside_stool
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.outside_head_jamb_wall,
        door_and_window_rectangles_seen_from_sun.outside_head_jamb_wall
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.outside_left_jamb_wall,
        door_and_window_rectangles_seen_from_sun.outside_left_jamb_wall
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.outside_right_jamb_wall,
        door_and_window_rectangles_seen_from_sun.outside_right_jamb_wall
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.outside_stool,
        door_and_window_rectangles_seen_from_sun.outside_stool
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles.awning,
        door_and_window_rectangles_seen_from_sun.awning
    )


def test_door_and_window_seen_from_sun_transformer_if_sun_is_on_the_side():
    """
    Tests the DoorAndWindowRectanglesSeenFromSunTransformer class
    if sun is on the side of the door and window
    """
    transformer = DoorAndWindowRectanglesSeenFromSunTransformer()

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
        Quadrilateral([9, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]),
    )

    door_and_window_rectangles_seen_from_sun = transformer.transform(
        door_and_window_rectangles, 90, 0)

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.glazing,
        Quadrilateral([-2, 1, 0], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Glazing '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.outside_left_jamb_wall,
        Quadrilateral([-2, 1, 1], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Outside left jamb wall '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.outside_right_jamb_wall,
        Quadrilateral([-2, 1, 2], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Outside right jamb wall '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.outside_head_jamb_wall,
        Quadrilateral([-2, 1, 3], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Outside head jamb wall '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.outside_stool,
        Quadrilateral([-2, 1, 4], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Outside stool '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.inside_left_jamb_wall,
        Quadrilateral([-2, 1, 5], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Inside left jamb wall '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.inside_right_jamb_wall,
        Quadrilateral([-2, 1, 6], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Inside right jamb wall '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.inside_head_jamb_wall,
        Quadrilateral([-2, 1, 7], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Inside head jamb wall '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.inside_stool,
        Quadrilateral([-2, 1, 8], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Inside stool '
    )

    assert_quadrilaterals_are_close(
        door_and_window_rectangles_seen_from_sun.awning,
        Quadrilateral([-2, 1, 9], [-5, 4, 3], [-8, 7, 6], [-11, 10, 9]),
        'Awning '
    )
