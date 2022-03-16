"""Door and window device integration."""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME
from homeassistant.helpers.device_registry import async_get_registry
from homeassistant.helpers.typing import ConfigType, HomeAssistantType

from .const import (CONF_MANUFACTURER, CONF_MODEL, CONF_TYPE,
                    DATA_DOOR_AND_WINDOWS, DOMAIN)
from .data_providers import get_door_and_window
from .models.door_and_window import DoorAndWindow

_LOGGER = logging.getLogger(__name__)

# pylint: disable=unused-argument


async def async_setup(hass: HomeAssistantType, config: ConfigType) -> bool:
    """
    Initialize the component.

    Args:
        hass:
            The Home Assistant instance.
        config:
            The component configuration.

    Returns:
        The value indicates whether the setup of the integration was successful.
    """
    hass.data[DOMAIN] = {
        DATA_DOOR_AND_WINDOWS: {}
    }
    return True


async def async_setup_entry(hass: HomeAssistantType, config_entry: ConfigEntry) -> bool:
    """
    Initialize the integration for the specified `config_entry`.

    Args:
        hass:
            The Home Assistant instance.
        config_entry:
            The configuration entry to use for integration configuration.

    Returns:
        The value indicates whether the initialization was successful.
    """
    if config_entry.entry_id not in hass.data[DOMAIN][DATA_DOOR_AND_WINDOWS]:
        hass.data[DOMAIN][DATA_DOOR_AND_WINDOWS][config_entry.entry_id] = DoorAndWindow(
            config_entry.data[CONF_TYPE],
            config_entry.data[CONF_NAME],
            config_entry.data[CONF_MANUFACTURER],
            config_entry.data[CONF_MODEL]
        )

    config_entry.async_on_unload(config_entry.add_update_listener(update_listener))

    return True


async def update_listener(hass: HomeAssistantType, config_entry: ConfigEntry):
    """
    Handles the event when to config entry changes
    and the underlaying model has to be changed.

    Args:
        hass:
            The Home Assistant instance.
        config_entry:
            The changed config entry.
    """
    door_and_window: DoorAndWindow = get_door_and_window(hass, config_entry.entry_id)
    door_and_window.model = config_entry.data[CONF_MODEL]
    door_and_window.manufacturer = config_entry.data[CONF_MANUFACTURER]
    door_and_window.type = config_entry.data[CONF_TYPE]

    device_registry = await async_get_registry(hass)

    device_entry = device_registry.async_get_device(
        {(DOMAIN, config_entry.entry_id)}
    )

    device_registry.async_update_device(
        device_entry.id, model=door_and_window.model, manufacturer=door_and_window.manufacturer
    )
