""" The module for coordinator. """
from homeassistant.helpers.typing import HomeAssistantType

from .models.door_and_window import DoorAndWindow


class Coordinator():
    """
    Responsible for reporting required sensor values to `DoorAndWindow` instance.
    """
    # pylint: disable=unused-argument
    def __init__(self, hass: HomeAssistantType, door_and_window: DoorAndWindow):
        """
        Initialize a new instance of `Coordinator` class.

        Args:
            hass:
                The Home Assistant instance.
            door_and_window:
                The door and window to update based on the sensor values.
        """
        self._door_and_window = door_and_window

    @property
    def door_and_window(self):
        """The `DoorAndWindow` instance associated to the controller."""
        return self._door_and_window

    def dispose(self):
        """
        Removes all change tracking.
        """
        self._door_and_window.dispose()
