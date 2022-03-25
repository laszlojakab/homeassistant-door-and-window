""" Represents the module of Door and Window integration sensors. """
from datetime import date, datetime
import logging
from typing import Callable, List, Optional, Union

from homeassistant.components.sensor import (SensorEntity,
                                             SensorEntityDescription)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import HomeAssistantType, StateType

from .const import DOMAIN
from .data_store import get_door_and_window
from .models.door_and_window import DoorAndWindow

_LOGGER = logging.getLogger(__name__)


class DoorAndWindowSensorEntityDescriptor(SensorEntityDescription):
    """
    Describes a `DoorAndWindowSensor` entity.
    """
    name: Optional[Callable[
        [str], str
    ]] = lambda val: val


SENSOR_DESCRIPTIONS: List[DoorAndWindowSensorEntityDescriptor] = [
    DoorAndWindowSensorEntityDescriptor(
        key="width",
        name=lambda name: f"{name} width",
        icon="mdi:arrow-left-right",
        native_unit_of_measurement="mm",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        entity_registry_enabled_default=False
    ),
    DoorAndWindowSensorEntityDescriptor(
        key="height",
        name=lambda name: f"{name} height",
        icon="mdi:arrow-up-down",
        native_unit_of_measurement="mm",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        entity_registry_enabled_default=False
    ),
    DoorAndWindowSensorEntityDescriptor(
        key="inside_depth",
        name=lambda name: f"{name} inside depth",
        icon="mdi:arrow-top-right-bottom-left",
        native_unit_of_measurement="mm",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        entity_registry_enabled_default=False
    ),
    DoorAndWindowSensorEntityDescriptor(
        key="outside_depth",
        name=lambda name: f"{name} outside depth",
        icon="mdi:arrow-top-right-bottom-left",
        native_unit_of_measurement="mm",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        entity_registry_enabled_default=False
    ),
    DoorAndWindowSensorEntityDescriptor(
        key="frame_thickness",
        name=lambda name: f"{name} frame thickness",
        icon="mdi:rectangle-outline",
        native_unit_of_measurement="mm",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        entity_registry_enabled_default=False
    ),
    DoorAndWindowSensorEntityDescriptor(
        key="frame_face_thickness",
        name=lambda name: f"{name} frame face depth",
        icon="mdi:rectangle-outline",
        native_unit_of_measurement="mm",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        entity_registry_enabled_default=False
    ),
    DoorAndWindowSensorEntityDescriptor(
        key="azimuth",
        name=lambda name: f"{name} azimuth",
        icon="mdi:compass",
        native_unit_of_measurement="°",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        entity_registry_enabled_default=False
    ),
    DoorAndWindowSensorEntityDescriptor(
        key="tilt",
        name=lambda name: f"{name} tilt",
        icon="mdi:angle-acute",
        native_unit_of_measurement="°",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        entity_registry_enabled_default=False
    )
]


class DoorAndWindowSensor(SensorEntity):
    """ Represents a sensor which value is directly calculated from a `DoorAndWindow` instance. """

    def __init__(
        self,
        door_and_window: DoorAndWindow,
        config_entry_id: str,
        entity_description: DoorAndWindowSensorEntityDescriptor
    ):
        """
        Initialize a new instance of `DoorAndWindowSensor`.

        Args:
            door_and_window:
                The `DoorAndWindow` instance to provide data from.
            config_entry_id:
                The ID of the config entry which defined the `door_and_window` instance.
            entity_description:
                The entity description which defines the sensor.
        """
        self._door_and_window = door_and_window
        self._attr_unique_id = f"{config_entry_id}.{entity_description.key}"
        self.entity_description = SensorEntityDescription(
            entity_description.key,
            entity_description.device_class,
            entity_description.entity_category,
            entity_description.entity_registry_enabled_default,
            entity_description.force_update,
            entity_description.icon,
            entity_description.name(self._door_and_window.name),
            entity_description.unit_of_measurement,
            entity_description.last_reset,
            entity_description.native_unit_of_measurement,
            entity_description.state_class
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
            self._attr_native_value = value
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
    door_and_window = get_door_and_window(hass, config_entry.entry_id)
    _LOGGER.info("Setting up window and door device sensors.")

    for descriptor in SENSOR_DESCRIPTIONS:
        async_add_entities([
            DoorAndWindowSensor(door_and_window, config_entry.entry_id, descriptor)
        ])

    _LOGGER.info("Setting up window and door device sensors completed.")
