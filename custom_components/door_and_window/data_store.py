""" The Data store module. """
from .coordinator import Coordinator


class DataStore():
    """
    Class is responsible for storing data in Home Assistant instance.
    """

    def __init__(self):
        """
        Initialize a new instance of `DataStore` class.
        """
        self._store: dict[str, Coordinator] = {}

    def is_coordinator_registered(self, config_entry_id: str) -> bool:
        """
        Returns the value indicates whether a `Coordinator` instance is registered
        for the specified config entry id.

        Args:
            config_entry_id:
                The config entry id.

        Returns:
        The value indicates whether a `Coordinator` instance is registered
        for the specified config entry id.
        """
        return config_entry_id in self._store

    def set_coordinator(
        self,
        config_entry_id: str,
        coordinator: Coordinator
    ) -> None:
        """
        Stores the `Coordinator` instance for the specified `config_entry_id`.

        Args:
            hass:
                The Home Assistant instance.
            config_entry_id:
                The config entry identifier.
            coordinator:
                The coordinator object to store.
        """
        self._store[config_entry_id] = coordinator

    def get_coordinator(
        self,
        config_entry_id: str
    ) -> Coordinator:
        """
        Gets the `Coordinator` instance for the specified `config_entry_id`.

        Args:
            config_entry_id:
                The config entry identifier.

        Returns:
            The `Coordinator` instance associated to the specified `config_entry_id`.
        """
        return self._store[config_entry_id]

    def remove_coordinator(
        self,
        config_entry_id: str
    ) -> None:
        """
        Remove the `Coordinator` instance for the specified `config_entry_id`.

        Args:
            config_entry_id:
                The config entry identifier.
        """
        return self._store.pop(config_entry_id, None)
