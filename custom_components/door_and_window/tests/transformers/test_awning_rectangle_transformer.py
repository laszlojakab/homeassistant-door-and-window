""" Module for AwningRectangleTransformer class. """
from ...tests.utils import assert_quadrilaterals_are_close
from ...models.door_and_window import DoorAndWindow
from ...models.quadrilateral import Quadrilateral
from ...transformers.awning_rectangle_transformer import \
    AwningRectangleTransformer


def test_awning_rectangle_transformer_heading_north():
    """ Tests the AwningRectangleTransformer class. """
    awning_rectangle = Quadrilateral(
        [-100, 5, -10],
        [100, 5, -10],
        [100, 5, -510],
        [-100, 5, -510]
    )

    door_and_window = DoorAndWindow(
        'window',
        'my window',
        'manufacturer',
        'model',
        900,
        1200,
        90,
        89,
        # outside_depth
        100,
        200,
        # parapet wall height
        900,
        # facing north
        0,
        # vertical window
        90,
        None,
        None
    )

    transformer = AwningRectangleTransformer()
    transformed_awning_rectangle = transformer.transform(awning_rectangle, door_and_window)

    assert_quadrilaterals_are_close(
        transformed_awning_rectangle,
        Quadrilateral(
            [-100, 2105, -110],
            [100, 2105, -110],
            [100, 2105, -610],
            [-100, 2105, -610]
        )
    )


def test_awning_rectangle_transformer_heading_east():
    """ Tests the AwningRectangleTransformer class. """
    awning_rectangle = Quadrilateral(
        [-100, 5, -10],
        [100, 5, -10],
        [100, 5, -510],
        [-100, 5, -510]
    )

    door_and_window = DoorAndWindow(
        'window',
        'my window',
        'manufacturer',
        'model',
        900,
        1200,
        90,
        89,
        # outside_depth
        100,
        200,
        # parapet wall height
        900,
        # facing east
        90,
        # vertical window
        90,
        None,
        None
    )

    transformer = AwningRectangleTransformer()
    transformed_awning_rectangle = transformer.transform(awning_rectangle, door_and_window)

    assert_quadrilaterals_are_close(
        transformed_awning_rectangle,
        Quadrilateral(
            [-110, 2105, 100],
            [-110, 2105, -100],
            [-610, 2105, -100],
            [-610, 2105, 100]
        )
    )
