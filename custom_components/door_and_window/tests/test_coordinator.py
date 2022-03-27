""" The module of coordinator tests. """
from unittest.mock import MagicMock

from ..coordinator import Coordinator


def test_coordinator_dispose():
    """
    Tests if the dispose method of door and window called
    in case of coordinator disposing.
    """
    door_and_window_mock = MagicMock()
    coordinator = Coordinator(None, door_and_window_mock)
    coordinator.dispose()
    door_and_window_mock.dispose.assert_called_once()
