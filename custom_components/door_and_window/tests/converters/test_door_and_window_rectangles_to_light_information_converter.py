""" Tests for DoorAndWindowRectanglesToLightInformationConverter class. """
from ...converters.door_and_window_rectangles_to_light_information_converter import \
    DoorAndWindowRectanglesToLightInformationConverter
from ...models.door_and_window_rectangles import DoorAndWindowRectangles
from ...models.quadrilateral import Quadrilateral


def get_door_and_window_rectangles():
    """ Returns the test door and window rectangles """
    return DoorAndWindowRectangles(
        Quadrilateral(
            [-411, 989, 0],
            [411, 989, 0],
            [411, 2311, 0],
            [-411, 2311, 0]
        ),
        Quadrilateral(
            [-500, 900, 0],
            [-500, 900, -100],
            [-500, 2400, -100],
            [-500, 2400, 0],
        ),
        Quadrilateral(
            [500, 900, 0],
            [500, 900, -100],
            [500, 2400, -100],
            [500, 2400, 0],
        ),
        Quadrilateral(
            [-500, 2400, 0],
            [-500, 2400, -100],
            [500, 2400, -100],
            [500, 2400, 0],
        ),
        Quadrilateral(
            [-500, 900, 0],
            [-500, 900, -100],
            [500, 900, -100],
            [500, 900, 0],
        ),
        Quadrilateral(
            [-500, 900, 90],
            [-500, 900, 290],
            [-500, 2400, 290],
            [-500, 2400, 90],
        ),
        Quadrilateral(
            [500, 900, 90],
            [500, 900, 290],
            [500, 2400, 290],
            [500, 2400, 90],
        ),
        Quadrilateral(
            [-500, 2400, 90],
            [-500, 2400, 290],
            [500, 2400, 290],
            [500, 2400, 90],
        ),
        Quadrilateral(
            [-500, 900, 90],
            [-500, 900, 290],
            [500, 900, 290],
            [500, 900, 90],
        )
    )


def test_if_sun_below_horizon():
    """ Tests if the sunny glazing polygon is empty if sun is below horizon. """
    converter = DoorAndWindowRectanglesToLightInformationConverter()
    door_and_window_rectangles = get_door_and_window_rectangles()

    light_info = converter.convert(door_and_window_rectangles, 30, 0, 90, 0, 20)

    assert light_info.sunny_glazing_area_polygon.area == 0


def test_if_sun_is_behind_door_and_window():
    """ Tests if the sunny glazing polygon is empty if sun is behind the door and window. """
    converter = DoorAndWindowRectanglesToLightInformationConverter()
    door_and_window_rectangles = get_door_and_window_rectangles()

    light_info = converter.convert(door_and_window_rectangles, 0, 0, 90, 180, 45)

    assert light_info.sunny_glazing_area_polygon.area == 0


def test_if_sun_is_in_front_of_door_and_window():
    """ Tests if the sunny glazing polygon is not empty if sun is in front of the window. """
    converter = DoorAndWindowRectanglesToLightInformationConverter()
    door_and_window_rectangles = get_door_and_window_rectangles()

    light_info = converter.convert(door_and_window_rectangles, 0, 0, 90, 0, 45)

    assert light_info.sunny_glazing_area_polygon.area > 0
