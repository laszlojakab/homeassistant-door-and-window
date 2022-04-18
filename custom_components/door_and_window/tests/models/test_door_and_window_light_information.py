# pylint: disable=missing-function-docstring
"""Test module for `DoorAndWindowLightInformation` class."""
from shapely.geometry.polygon import Polygon

from ...models.door_and_window_light_information import DoorAndWindowLightInformation


def test_door_and_window_light_information_angle_of_incidence():
    door_and_window_light_info = DoorAndWindowLightInformation(15, Polygon())
    assert door_and_window_light_info.angle_of_incidence == 15, \
        'Angle of incidence must be the value set in constructor.'


def test_door_and_window_light_information_sunn_glazing_area_polygon():
    polygon = Polygon()
    door_and_window_light_info = DoorAndWindowLightInformation(15, polygon)
    assert door_and_window_light_info.sunny_glazing_area_polygon == polygon, \
        'Sunny glazing area polygon must be the value set in constructor.'
