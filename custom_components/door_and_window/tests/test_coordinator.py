""" The module of coordinator tests. """
from unittest.mock import ANY, MagicMock, patch

from homeassistant.helpers.event import async_track_state_change

from ..coordinator import Coordinator


@patch('door_and_window.coordinator.async_track_state_change', side_effect=async_track_state_change)
def test_coordinator_init(async_track_state_change_mock):
    """
    Tests if the coordinator starts to listening
    to sun position change.
    """
    async_track_state_change_mock.return_value = None
    door_and_window_mock = MagicMock()
    hass = MagicMock()
    coordinator = Coordinator(hass, door_and_window_mock, "sun.sun")

    # should track sun's position
    async_track_state_change_mock.assert_called_once_with(hass, "sun.sun", ANY)

    coordinator.dispose()


@patch('door_and_window.coordinator.async_track_state_change', side_effect=async_track_state_change)
def test_coordinator_dispose(async_track_state_change_mock):
    """
    Tests if the dispose method of door and window called
    in case of coordinator disposing.
    """
    async_track_state_change_mock.return_value = None
    door_and_window_mock = MagicMock()
    hass = MagicMock()
    coordinator = Coordinator(hass, door_and_window_mock, "sun.sun")

    coordinator.dispose()
    door_and_window_mock.dispose.assert_called_once()
