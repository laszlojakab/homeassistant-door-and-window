"""Door and window device integration."""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME
from homeassistant.helpers.device_registry import async_get_registry
from homeassistant.helpers.typing import ConfigType, HomeAssistantType

from .const import (CONF_AWNING_CLOSEST_TOP, CONF_AWNING_DISTANCE, CONF_AWNING_FARTHEST_TOP,
                    CONF_AWNING_LEFT_DISTANCE, CONF_AWNING_MAX_DEPTH,
                    CONF_AWNING_MIN_DEPTH, CONF_AWNING_RIGHT_DISTANCE,
                    CONF_AZIMUTH, CONF_FRAME_FACE_THICKNESS,
                    CONF_FRAME_THICKNESS, CONF_HAS_AWNING, CONF_HEIGHT,
                    CONF_HORIZON_PROFILE, CONF_INSIDE_DEPTH, CONF_MANUFACTURER,
                    CONF_MODEL, CONF_OUTSIDE_DEPTH, CONF_PARAPET_WALL_HEIGHT,
                    CONF_TILT, CONF_TYPE, CONF_WIDTH, DOMAIN, TYPE_DOOR)
from .coordinator import Coordinator
from .data_store import DataStore
from .models.awning import Awning
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
    hass.data[DOMAIN] = DataStore()
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

    data_store: DataStore = hass.data[DOMAIN]

    if not data_store.is_coordinator_registered(config_entry.entry_id):
        awning : Awning
        if config_entry.data[CONF_HAS_AWNING]:
            awning = Awning(
                config_entry.data[CONF_AWNING_LEFT_DISTANCE] + \
                config_entry.data[CONF_WIDTH] + config_entry.data[CONF_AWNING_RIGHT_DISTANCE],
                config_entry.data[CONF_AWNING_MIN_DEPTH],
                config_entry.data[CONF_AWNING_MAX_DEPTH],
                -config_entry.data[CONF_WIDTH] / 2 + \
                config_entry.data[CONF_AWNING_RIGHT_DISTANCE] - \
                config_entry.data[CONF_AWNING_LEFT_DISTANCE],
                config_entry.data[CONF_AWNING_CLOSEST_TOP],
                config_entry.data[CONF_AWNING_FARTHEST_TOP],
                config_entry.data[CONF_AWNING_DISTANCE],
                100,
            )
        else:
            awning = None

        door_and_window = DoorAndWindow(
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
            config_entry.data[CONF_AZIMUTH],
            config_entry.data[CONF_TILT],
            config_entry.data.get(CONF_HORIZON_PROFILE, [0, 0]),
            awning
        )
        data_store.set_coordinator(config_entry.entry_id, Coordinator(
            hass,
            door_and_window,
            "sun.sun"
        ))

        device_registry = await async_get_registry(hass)

        device_registry.async_get_or_create(
            config_entry_id=config_entry.entry_id,
            identifiers={(DOMAIN, config_entry.entry_id)},
            name=config_entry.data[CONF_NAME],
            model=config_entry.data.get(CONF_MODEL),
            manufacturer=config_entry.data.get(CONF_MANUFACTURER),
            sw_version=get_software_version(
                config_entry.data[CONF_WIDTH], config_entry.data[CONF_HEIGHT])
        )

    config_entry.async_on_unload(config_entry.add_update_listener(update_listener))

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            config_entry, "sensor"
        )
    )

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            config_entry, "binary_sensor"
        )
    )

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
    data_store: DataStore = hass.data[DOMAIN]
    coordinator: Coordinator = data_store.get_coordinator(config_entry.entry_id)
    door_and_window: DoorAndWindow = coordinator.door_and_window
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
    door_and_window.azimuth = config_entry.data[CONF_AZIMUTH]
    door_and_window.tilt = config_entry.data[CONF_TILT]
    door_and_window.horizon_profile = config_entry.data.get(CONF_HORIZON_PROFILE, [0, 0])

    if config_entry.data[CONF_HAS_AWNING]:
        door_and_window.awning = Awning(
            config_entry.data[CONF_AWNING_LEFT_DISTANCE] + \
            config_entry.data[CONF_WIDTH] + config_entry.data[CONF_AWNING_RIGHT_DISTANCE],
            config_entry.data[CONF_AWNING_MIN_DEPTH],
            config_entry.data[CONF_AWNING_MAX_DEPTH],
            -config_entry.data[CONF_WIDTH] / 2 + config_entry.data[CONF_AWNING_RIGHT_DISTANCE] - \
            config_entry.data[CONF_AWNING_LEFT_DISTANCE],
            config_entry.data[CONF_AWNING_CLOSEST_TOP],
            config_entry.data[CONF_AWNING_FARTHEST_TOP],
            config_entry.data[CONF_AWNING_DISTANCE],
            100,
        )
    else:
        door_and_window.awning = None

    device_registry = await async_get_registry(hass)

    device_entry = device_registry.async_get_device(
        {(DOMAIN, config_entry.entry_id)}
    )

    device_registry.async_update_device(
        device_entry.id,
        model=door_and_window.model,
        manufacturer=door_and_window.manufacturer,
        sw_version=get_software_version(door_and_window.width, door_and_window.height)
    )


async def async_unload_entry(hass: HomeAssistantType, config_entry: ConfigEntry):
    """
    Unloads the specified config entry.

    Args:
        hass:
            The Home Assistant instance.
        config_entry:
            The config entry to unload.
    """
    if not await hass.config_entries.async_forward_entry_unload(config_entry, 'sensor'):
        return False

    if not await hass.config_entries.async_forward_entry_unload(config_entry, 'binary_sensor'):
        return False

    data_store: DataStore = hass.data[DOMAIN]

    coordinator = data_store.get_coordinator(config_entry.entry_id)
    coordinator.dispose()

    data_store.remove_coordinator(config_entry.entry_id)

    return True


def get_software_version(width: float, height: float):
    """
    Gets the software version for the door and window device.

    The version is the size of the door and window.
    """
    return str(width / 1000) + ' x ' + str(height / 1000)
