""" Data store functions module. """
from homeassistant.helpers.typing import HomeAssistantType

from .const import DATA_DOOR_AND_WINDOWS, DOMAIN
from .models.door_and_window import DoorAndWindow


def set_door_and_window(
    hass: HomeAssistantType,
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
    hass.data[DOMAIN][DATA_DOOR_AND_WINDOWS][config_entry_id] = door_and_window


def get_door_and_window(
    hass: HomeAssistantType,
    config_entry_id: str
) -> DoorAndWindow:
    """
    Gets the DoorAndWindow instance for the specified `config_entry_id`.

    Args:
        hass:
            The Home Assistant instance.
        config_entry_id:
            The config entry identifier.

    Returns:
        The `DoorAndWindow` instance associated to the specified `config_entry_id`.
    """
    return hass.data[DOMAIN][DATA_DOOR_AND_WINDOWS][config_entry_id]
