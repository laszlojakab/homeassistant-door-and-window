""" Data provider functions module. """
from homeassistant.helpers.typing import HomeAssistantType

from .const import DATA_DOOR_AND_WINDOWS, DOMAIN
from .models.door_and_window import DoorAndWindow


def get_door_and_window(hass: HomeAssistantType, config_entry_id: str) -> DoorAndWindow:
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
