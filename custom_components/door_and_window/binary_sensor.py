""" Represents the module of Door and Window integration sensors. """
import logging
from datetime import date, datetime
from typing import Callable, List, Optional, Union

from homeassistant.components.binary_sensor import (BinarySensorEntity,
                                                    BinarySensorEntityDescription,
                                                    BinarySensorDeviceClass)
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import HomeAssistantType, StateType

from .const import DOMAIN
from .coordinator import Coordinator
from .data_store import DataStore
from .models.door_and_window import DoorAndWindow

_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-few-public-methods
class DoorAndWindowBinarySensorEntityDescriptor(BinarySensorEntityDescription):
    """
    Describes a `DoorAndWindowBinarySensor` entity.
    """
    name: Optional[Callable[
        [str], str
    ]] = lambda val: val


SENSOR_DESCRIPTIONS: List[DoorAndWindowBinarySensorEntityDescriptor] = [
    DoorAndWindowBinarySensorEntityDescriptor(
        key="glazing_has_direct_sunlight",
        name=lambda name: f"{name} glazing has direct sunlight",
        icon="mdi:weather-sunny-alert",
        entity_registry_enabled_default=True,
        device_class=BinarySensorDeviceClass.LIGHT
    )
]


class DoorAndWindowBinarySensor(BinarySensorEntity):
    """
    Represents a binary sensor which value is directly
    calculated from a `DoorAndWindow` instance.
    """

    def __init__(
        self,
        door_and_window: DoorAndWindow,
        config_entry_id: str,
        entity_description: DoorAndWindowBinarySensorEntityDescriptor
    ):
        """
        Initialize a new instance of `DoorAndWindowBinarySensor` class.

        Args:
            door_and_window:
                The `DoorAndWindow` instance to provide data from.
            config_entry_id:
                The ID of the config entry which defined the `door_and_window` instance.
            entity_description:
                The entity description which defines the binary sensor.
        """
        self._door_and_window = door_and_window
        self._attr_unique_id = f"{config_entry_id}.{entity_description.key}"
        self.entity_description = BinarySensorEntityDescription(
            entity_description.key,
            entity_description.device_class,
            entity_description.entity_category,
            entity_description.entity_registry_enabled_default,
            entity_description.force_update,
            entity_description.icon,
            entity_description.name(self._door_and_window.name)
        )

        self._track_change_dispose = None
        self._attr_should_poll = False

        self._attr_device_info = {
            "identifiers": {
                (DOMAIN, config_entry_id)
            },
            "name": door_and_window.name,
            "model":  door_and_window.model,
            "manufacturer": door_and_window.manufacturer
        }

    async def async_added_to_hass(self) -> None:
        def update_native_value(value):
            self._attr_is_on = value
            self.async_schedule_update_ha_state()

        on_change = getattr(self._door_and_window, f"on_{self.entity_description.key}_changed")

        self._track_change_dispose = on_change(update_native_value)

    async def async_will_remove_from_hass(self) -> None:
        if self._track_change_dispose is not None:
            self._track_change_dispose()

    @property
    def native_value(self) -> Union[StateType, date, datetime]:
        """Return the value reported by the sensor."""
        return getattr(self._door_and_window, self.entity_description.key)


async def async_setup_entry(
    hass: HomeAssistantType,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback
):
    """
    Handles the creation of sensors based on the specified `ConfigEntry` instance.

    Args:
        hass:
            The Home Assistant instance.
        config_entry:
            The configuration entry which provides information for sensor creation.
        async_add_entities:
            The callback to use to add sensors to Home Assistant.
    """
    data_store: DataStore = hass.data[DOMAIN]
    coordinator: Coordinator = data_store.get_coordinator(config_entry.entry_id)
    _LOGGER.info("Setting up door and window binary sensors.")

    for descriptor in SENSOR_DESCRIPTIONS:
        async_add_entities([
            DoorAndWindowBinarySensor(
                coordinator.door_and_window,
                config_entry.entry_id,
                descriptor
            )
        ])

    _LOGGER.info("Setting up door and window binary sensors completed.")
