""" Tests for door and window to rectangle converter. """
from ...converters.door_and_window_to_rectangles_converter import \
    DoorAndWindowToRectanglesConverter
from ...models.awning import Awning
from ...models.door_and_window import DoorAndWindow
from ...models.quadrilateral import Quadrilateral
from ..utils import assert_quadrilaterals_are_close


def test_door_and_window_to_rectangles_converter():
    """ Tests the door and window converter on a window looking to north. """
    converter = DoorAndWindowToRectanglesConverter()
    door_and_window = DoorAndWindow(
        "Window",
        "My window",
        "Manufacturer",
        "Model",
        1000,
        1500,
        90,
        89,
        100,
        200,
        900,
        0,
        90,
        [0, 0],
        Awning(
            1000,
            1200,
            1200,
            0,
            100,
            0,
            150,
            100
        )
    )

    rectangles = converter.convert(door_and_window)

    assert_quadrilaterals_are_close(
        rectangles.glazing,
        Quadrilateral(
            [-411, 989, 0],
            [411, 989, 0],
            [411, 2311, 0],
            [-411, 2311, 0]
        ),
        "Glazing: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_stool,
        Quadrilateral(
            [-500, 900, 90],
            [-500, 900, 290],
            [500, 900, 290],
            [500, 900, 90],
        ),
        "Inside stool: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_stool,
        Quadrilateral(
            [-500, 900, 0],
            [-500, 900, -100],
            [500, 900, -100],
            [500, 900, 0],
        ),
        "Outside stool: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_head_jamb_wall,
        Quadrilateral(
            [-500, 2400, 90],
            [-500, 2400, 290],
            [500, 2400, 290],
            [500, 2400, 90],
        ),
        "Inside head jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_head_jamb_wall,
        Quadrilateral(
            [-500, 2400, 0],
            [-500, 2400, -100],
            [500, 2400, -100],
            [500, 2400, 0],
        ),
        "Outside head jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_left_jamb_wall,
        Quadrilateral(
            [-500, 900, 90],
            [-500, 900, 290],
            [-500, 2400, 290],
            [-500, 2400, 90],
        ),
        "Inside left jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_left_jamb_wall,
        Quadrilateral(
            [-500, 900, 0],
            [-500, 900, -100],
            [-500, 2400, -100],
            [-500, 2400, 0],
        ),
        "Outside left jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_right_jamb_wall,
        Quadrilateral(
            [500, 900, 90],
            [500, 900, 290],
            [500, 2400, 290],
            [500, 2400, 90],
        ),
        "Inside right jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_right_jamb_wall,
        Quadrilateral(
            [500, 900, 0],
            [500, 900, -100],
            [500, 2400, -100],
            [500, 2400, 0],
        ),
        "Outside right jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.awning,
        Quadrilateral(
            [-500, 2500, -250],
            [500, 2500, -250],
            [500, 2400, -1450],
            [-500, 2400, -1450],
        ),
        "Awning: "
    )


def test_door_and_window_to_rectangles_converter_with_azimuth():
    """ Tests the door and window converter on a window looking to east. """
    converter = DoorAndWindowToRectanglesConverter()
    door_and_window = DoorAndWindow(
        "Window",
        "My window",
        "Manufacturer",
        "Model",
        1000,
        1500,
        90,
        89,
        100,
        200,
        900,
        # window rotated east (clockwise 90)
        90,
        90,
        [0, 0],
        Awning(
            1000,
            1200,
            1200,
            0,
            100,
            0,
            150,
            100
        )
    )

    rectangles = converter.convert(door_and_window)

    assert_quadrilaterals_are_close(
        rectangles.glazing,
        Quadrilateral(
            [0, 989, 411],
            [0, 989, -411],
            [0, 2311, -411],
            [0, 2311, 411]
        ),
        "Glazing: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_stool,
        Quadrilateral(
            [90, 900, 500],
            [290, 900, 500],
            [290, 900, -500],
            [90, 900, -500],
        ),
        "Inside stool: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_stool,
        Quadrilateral(
            [0, 900, 500],
            [-100, 900, 500],
            [-100, 900, -500],
            [0, 900, -500],
        ),
        "Outside stool: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_head_jamb_wall,
        Quadrilateral(
            [90, 2400, 500],
            [290, 2400, 500],
            [290, 2400, -500],
            [90, 2400, -500],
        ),
        "Inside head jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_head_jamb_wall,
        Quadrilateral(
            [0, 2400, 500],
            [-100, 2400, 500],
            [-100, 2400, -500],
            [0, 2400, -500],
        ),
        "Outside head jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_left_jamb_wall,
        Quadrilateral(
            [90, 900, 500],
            [290, 900, 500],
            [290, 2400, 500],
            [90, 2400, 500],
        ),
        "Inside left jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_left_jamb_wall,
        Quadrilateral(
            [0, 900, 500],
            [-100, 900, 500],
            [-100, 2400, 500],
            [0, 2400, 500],
        ),
        "Outside left jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_right_jamb_wall,
        Quadrilateral(
            [90, 900, -500],
            [290, 900, -500],
            [290, 2400, -500],
            [90, 2400, -500],
        ),
        "Inside right jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_right_jamb_wall,
        Quadrilateral(
            [0, 900, -500],
            [-100, 900, -500],
            [-100, 2400, -500],
            [0, 2400, -500],
        ),
        "Outside right jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.awning,
        Quadrilateral(
            [-250, 2500, 500],
            [-250, 2500, -500],
            [-1450, 2400, -500],
            [-1450, 2400, 500],
        ),
        "Awning: "
    )

def test_door_and_window_to_rectangles_converter_with_0_tilt():
    """ Tests the door and window converter on a window looking to east. """
    converter = DoorAndWindowToRectanglesConverter()
    door_and_window = DoorAndWindow(
        "Window",
        "My window",
        "Manufacturer",
        "Model",
        1000,
        1500,
        90,
        89,
        100,
        200,
        900,
        0,
        # window is looking upward to the sky
        0,
        [0, 0],
        None
    )

    rectangles = converter.convert(door_and_window)

    assert_quadrilaterals_are_close(
        rectangles.glazing,
        Quadrilateral(
            [-411, 0, 989],
            [411, 0, 989],
            [411, 0, 2311],
            [-411, 0, 2311]
        ),
        "Glazing: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_stool,
        Quadrilateral(
            [-500, -90, 900],
            [-500, -290, 900],
            [500, -290, 900],
            [500, -90, 900],
        ),
        "Inside stool: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_stool,
        Quadrilateral(
            [-500, 0, 900],
            [-500, 100, 900],
            [500, 100, 900],
            [500, 0, 900],
        ),
        "Outside stool: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_head_jamb_wall,
        Quadrilateral(
            [-500, -90, 2400],
            [-500, -290, 2400],
            [500, -290, 2400],
            [500, -90, 2400],
        ),
        "Inside head jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_head_jamb_wall,
        Quadrilateral(
            [-500, 0, 2400],
            [-500, 100, 2400],
            [500, 100, 2400],
            [500, 0, 2400],
        ),
        "Outside head jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_left_jamb_wall,
        Quadrilateral(
            [-500, -90, 900],
            [-500, -290, 900],
            [-500, -290, 2400],
            [-500, -90, 2400],
        ),
        "Inside left jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_left_jamb_wall,
        Quadrilateral(
            [-500, 0, 900],
            [-500, 100, 900],
            [-500, 100, 2400],
            [-500, 0, 2400],
        ),
        "Outside left jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.inside_right_jamb_wall,
        Quadrilateral(
            [500, -90, 900],
            [500, -290, 900],
            [500, -290, 2400],
            [500, -90, 2400],
        ),
        "Inside right jamb wall: "
    )

    assert_quadrilaterals_are_close(
        rectangles.outside_right_jamb_wall,
        Quadrilateral(
            [500, 0, 900],
            [500, 100, 900],
            [500, 100, 2400],
            [500, 0, 2400],
        ),
        "Outside right jamb wall: "
    )

    assert rectangles.awning is None
