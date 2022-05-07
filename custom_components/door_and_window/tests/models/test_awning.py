# pylint: disable=missing-function-docstring
"""Test module for `Awning` class."""
from typing import Tuple

import pytest

from ...models.awning import Awning


@pytest.mark.parametrize("prop_and_arg_index", [
    ("width", 0),
    ("min_depth", 1),
    ("max_depth", 2),
    ("x", 3),
    ("y0", 4),
    ("y1", 5),
    ("z", 6),
    ("cover_position", 7)
])
def test_awning_property_set_in_constructor(prop_and_arg_index: Tuple[str, int]):
    args = [1000] * 8

    args[prop_and_arg_index[1]] = 10

    awning = Awning(*args)

    assert getattr(awning, prop_and_arg_index[0]) == 10


def test_awning_cover_position():
    awning = Awning(
        width=1000,
        min_depth=10,
        max_depth=500,
        x=0,
        y0=1500,
        y1=1200,
        z=0,
        cover_position=100
    )

    assert awning.cover_position == 100

    awning.cover_position = 50

    assert awning.cover_position == 50


def test_awning_current_depth():
    awning = Awning(
        width=1000,
        min_depth=100,
        max_depth=500,
        x=0,
        y0=1500,
        y1=1200,
        z=0,
        cover_position=0
    )

    assert awning.current_depth == 100

    change_count = 0

    # pylint: disable=unused-argument
    def change_callback(current_value):
        nonlocal change_count
        change_count += 1

    awning.on_current_depth_changed(change_callback)
    assert change_count == 0

    awning.cover_position = 50
    assert change_count == 1

    assert awning.current_depth == 300

    awning.cover_position = 100
    assert change_count == 2

    assert awning.current_depth == 500
