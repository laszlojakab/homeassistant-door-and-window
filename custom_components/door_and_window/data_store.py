""" The Data store module. """
from .const import DATA_DOOR_AND_WINDOWS
from .models.door_and_window import DoorAndWindow


class DataStore():
    """
    Class is responsible for storing data in Home Assistant instance.
    """

    def __init__(self):
        """
        Initialize a new instance of `DataStore` class.
        """
        self._store = {
            DATA_DOOR_AND_WINDOWS: {}
        }

    def is_door_and_window_registered(self, config_entry_id: str) -> bool:
        """
        Returns the value indicates whether a `DoorAndWindow` instance is registered
        for the specified config entry id.

        Args:
            config_entry_id:
                The config entry id.

        Returns:
        The value indicates whether a `DoorAndWindow` instance is registered
        for the specified config entry id.
        """
        return config_entry_id in self._store

    def set_door_and_window(
        self,
        config_entry_id: str,
        door_and_window: DoorAndWindow
    ) -> None:
        """
        Stores the `DoorAndWindow` instance for the specified `config_entry_id`.

        Args:
            hass:
                The Home Assistant instance.
            config_entry_id:
                The config entry identifier.
            door_and_window:
                The door and window object to store.
        """
        self._store[DATA_DOOR_AND_WINDOWS][config_entry_id] = door_and_window

    def get_door_and_window(
        self,
        config_entry_id: str
    ) -> DoorAndWindow:
        """
        Gets the DoorAndWindow instance for the specified `config_entry_id`.

        Args:
            config_entry_id:
                The config entry identifier.

        Returns:
            The `DoorAndWindow` instance associated to the specified `config_entry_id`.
        """
        return self._store[DATA_DOOR_AND_WINDOWS][config_entry_id]

    def remove_door_and_window(
        self,
        config_entry_id: str
    ) -> None:
        """
        Remove the `DoorAndWindow` instance for the specified `config_entry_id`.

        Args:
            config_entry_id:
                The config entry identifier.
        """
        return self._store[DATA_DOOR_AND_WINDOWS].pop(config_entry_id, None)
