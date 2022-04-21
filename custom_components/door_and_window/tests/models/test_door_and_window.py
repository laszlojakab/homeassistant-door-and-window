# pylint: disable=missing-function-docstring
"""Test module for `DoorAndWindow` class."""
import math
from typing import Any
from unittest.mock import patch

import pytest
from shapely.geometry import Polygon

from ...converters.door_and_window_rectangles_to_light_information_converter import \
    DoorAndWindowRectanglesToLightInformationConverter
from ...converters.door_and_window_to_rectangles_converter import \
    DoorAndWindowToRectanglesConverter
from ...models.door_and_window import DoorAndWindow
from ...models.door_and_window_light_information import \
    DoorAndWindowLightInformation


@pytest.mark.parametrize('prop', [
    'width',
    'height',
    'frame_thickness',
    'frame_face_thickness',
    'outside_depth',
    'inside_depth',
    'azimuth',
    'tilt'
])
def test_door_and_window_property_changed(prop: str):
    door_and_window = DoorAndWindow(
        'window',
        'my window',
        'manufacturer',
        'model',
        900,
        1200,
        90,
        89,
        100,
        200,
        900,
        0,
        90,
        None
    )

    property_change_count = 0

    #pylint: disable=unused-argument
    def track_property_change(value: Any):
        nonlocal property_change_count
        property_change_count += 1

    getattr(door_and_window, f"on_{prop}_changed")(track_property_change)

    setattr(door_and_window, prop, 999)

    assert property_change_count == 1, \
        f"change event must be fired if {prop} property has changed"

    setattr(door_and_window, prop, 999)

    assert property_change_count == 1, \
        f"change event must not be fired if {prop} property has not been changed"


def test_horizon_elevation_at_sun_azimuth():
    door_and_window = DoorAndWindow(
        'window',
        'my window',
        'manufacturer',
        'model',
        900,
        1200,
        90,
        89,
        100,
        200,
        900,
        0,  # heading to north
        90,
        [0, 180]
    )

    door_and_window.update(0, 45)  # sun is at north
    assert door_and_window.horizon_elevation_at_sun_azimuth == 90

    door_and_window.update(90, 45)  # sun is at east
    assert door_and_window.horizon_elevation_at_sun_azimuth == 180

    door_and_window.update(270, 45)  # sun is at west
    assert door_and_window.horizon_elevation_at_sun_azimuth == 0

    door_and_window.update(180, 45)  # sun is behind the window
    assert door_and_window.horizon_elevation_at_sun_azimuth is None


def test_angle_of_incidence():
    door_and_window = DoorAndWindow(
        'window',
        'my window',
        'manufacturer',
        'model',
        900,
        1200,
        90,
        89,
        100,
        200,
        900,
        0,  # heading to north
        90,
        [0, 180]
    )

    door_and_window.update(180, 0)  # sun is behind the window
    assert math.isclose(door_and_window.angle_of_incidence, 180)

    door_and_window.update(0, 0)
    assert math.isclose(door_and_window.angle_of_incidence, 0)

    door_and_window.update(0, 30)
    assert math.isclose(door_and_window.angle_of_incidence, 30)

    door_and_window.update(0, -30)
    assert math.isclose(door_and_window.angle_of_incidence, 30)


@pytest.mark.parametrize('prop', [
    'width',
    'height',
    'frame_thickness',
    'frame_face_thickness',
    'outside_depth',
    'inside_depth',
    'azimuth',
    'tilt'
])
def test_if_rectangles_updated(prop: str):
    with patch.object(
        DoorAndWindowToRectanglesConverter,
        'convert',
        return_value=None
    ) as convert_mock:
        with patch.object(
            DoorAndWindowRectanglesToLightInformationConverter,
            'convert',
            return_value=DoorAndWindowLightInformation(0, Polygon())
        ):
            door_and_window = DoorAndWindow(
                'window',
                'my window',
                'manufacturer',
                'model',
                900,
                1200,
                90,
                89,
                100,
                200,
                900,
                0,
                90,
                [0, 0]
            )

            # rectangle converting should not be called before updating
            convert_mock.assert_not_called()

            door_and_window.update(1, 0)

            # rectangle converting should be called after updating (and no property changed)
            convert_mock.assert_called_once()

            setattr(door_and_window, prop, 999)

            # should not call rectangle updates
            convert_mock.assert_called_once()

            door_and_window.update(2, 0)

            # rectangle converting should be called after updating (and no property changed)
            assert convert_mock.call_count == 2
