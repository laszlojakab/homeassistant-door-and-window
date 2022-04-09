""" The module of coordinator tests. """
from unittest.mock import ANY, MagicMock, patch

from ..coordinator import Coordinator


@patch('door_and_window.coordinator.DoorAndWindowToRectanglesConverter.convert', return_value=None)
@patch('door_and_window.coordinator.async_track_state_change', return_value=lambda: None)
def test_coordinator_init(async_track_state_change_mock, convert_mock):
    """
    Tests if the coordinator starts to listening
    to sun position change.
    """

    door_and_window_mock = MagicMock()
    hass = MagicMock()
    coordinator = Coordinator(hass, door_and_window_mock, "sun.sun")

    # should track sun's position
    async_track_state_change_mock.assert_called_once_with(hass, "sun.sun", ANY)

    # should generate initial rectangles
    convert_mock.assert_called_once_with(door_and_window_mock)

    coordinator.dispose()


@patch('door_and_window.coordinator.DoorAndWindowToRectanglesConverter.convert', return_value=None)
@patch('door_and_window.coordinator.async_track_state_change', return_value=lambda: None)
# pylint: disable=unused-argument
def test_coordinator_dispose(async_track_state_change_mock, convert_mock):
    """
    Tests if the dispose method of door and window called
    in case of coordinator disposing.
    """
    door_and_window_mock = MagicMock()
    hass = MagicMock()
    coordinator = Coordinator(hass, door_and_window_mock, "sun.sun")

    coordinator.dispose()
    door_and_window_mock.dispose.assert_called_once()
