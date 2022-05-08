""" Test module for AwningToRectangleConverter class. """
from ...models.quadrilateral import Quadrilateral
from ...tests.utils import assert_quadrilaterals_are_close
from ...models.awning import Awning
from ...converters.awning_to_rectangle_converter import AwningToRectangleConverter


def test_awning_to_rectangle_converter_opened():
    """ Tests the converter on a fully opened awning. """
    converter = AwningToRectangleConverter()
    awning = Awning(
        1000,
        100,
        700,
        100,
        2000,
        1500,
        150,
        100
    )

    rectangle = converter.convert(awning)
    assert_quadrilaterals_are_close(rectangle, Quadrilateral(
        [-400, 2000, -150],
        [600, 2000, -150],
        [600, 1500, -850],
        [-400, 1500, -850],
    ))


def test_awning_to_rectangle_converter_closed():
    """ Tests the converter on a fully closed awning. """
    converter = AwningToRectangleConverter()
    awning = Awning(
        1000,
        100,
        700,
        100,
        2000,
        1500,
        150,
        0
    )

    rectangle = converter.convert(awning)
    assert_quadrilaterals_are_close(rectangle, Quadrilateral(
        [-400, 2000, -150],
        [600, 2000, -150],
        [600, 1500, -250],
        [-400, 1500, -250],
    ))
