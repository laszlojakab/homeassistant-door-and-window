"""Door and window device integration."""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME
from homeassistant.helpers.device_registry import async_get_registry
from homeassistant.helpers.typing import ConfigType, HomeAssistantType

from .const import (CONF_FRAME_FACE_THICKNESS, CONF_FRAME_THICKNESS,
                    CONF_HEIGHT, CONF_INSIDE_DEPTH, CONF_MANUFACTURER,
                    CONF_MODEL, CONF_OUTSIDE_DEPTH, CONF_PARAPET_WALL_HEIGHT,
                    CONF_TYPE, CONF_WIDTH, DATA_DOOR_AND_WINDOWS, DOMAIN, TYPE_DOOR)
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
            config_entry.data.get(CONF_MANUFACTURER),
            config_entry.data.get(CONF_MODEL),
            config_entry.data[CONF_WIDTH],
            config_entry.data[CONF_HEIGHT],
            config_entry.data[CONF_FRAME_THICKNESS],
            config_entry.data[CONF_FRAME_FACE_THICKNESS],
            config_entry.data[CONF_OUTSIDE_DEPTH],
            config_entry.data[CONF_INSIDE_DEPTH],
            config_entry.data.get(CONF_PARAPET_WALL_HEIGHT, 0),
        )

        device_registry = await async_get_registry(hass)

        device_registry.async_get_or_create(
            config_entry_id=config_entry.entry_id,
            identifiers={
                (DOMAIN, config_entry.entry_id)
            },
            name=config_entry.data[CONF_NAME],
            model=config_entry.data.get(CONF_MODEL),
            manufacturer=config_entry.data.get(CONF_MANUFACTURER),
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
    door_and_window.model = config_entry.data.get(CONF_MODEL)
    door_and_window.manufacturer = config_entry.data.get(CONF_MANUFACTURER)
    door_and_window.type = config_entry.data[CONF_TYPE]
    door_and_window.width = config_entry.data[CONF_WIDTH]
    door_and_window.height = config_entry.data[CONF_HEIGHT]
    door_and_window.inside_depth = config_entry.data[CONF_INSIDE_DEPTH]
    door_and_window.outside_depth = config_entry.data[CONF_OUTSIDE_DEPTH]
    door_and_window.frame_thickness = config_entry.data[CONF_FRAME_THICKNESS]
    door_and_window.frame_face_thickness = config_entry.data[CONF_FRAME_FACE_THICKNESS]
    door_and_window.parapet_wall_height = \
        0 if door_and_window.type == TYPE_DOOR \
        else config_entry.data.get(CONF_PARAPET_WALL_HEIGHT, 0)

    device_registry = await async_get_registry(hass)

    device_entry = device_registry.async_get_device(
        {(DOMAIN, config_entry.entry_id)}
    )

    device_registry.async_update_device(
        device_entry.id, model=door_and_window.model, manufacturer=door_and_window.manufacturer
    )
