""" The module for coordinator. """
from homeassistant.core import State
from homeassistant.helpers.event import async_track_state_change
from homeassistant.helpers.typing import HomeAssistantType

from .models.door_and_window import DoorAndWindow


class Coordinator():
    """
    Responsible for reporting required sensor values to `DoorAndWindow` instance.
    """
    # pylint: disable=unused-argument

    def __init__(
        self,
        hass: HomeAssistantType,
        door_and_window: DoorAndWindow,
        sun_entity_id: str,
        horizon_profile_entity_id: str
    ):
        """
        Initialize a new instance of `Coordinator` class.

        Args:
            hass:
                The Home Assistant instance.
            door_and_window:
                The door and window to update based on the sensor values.
            sun_entity_id:
                The entity id of the sun entity.
            horizon_profile_entity_id:
                The entity id of horizon profile in case of dynamic horizon.
        """
        self._door_and_window = door_and_window
        self._hass = hass

        # initialize sun tracking
        self._track_sun_entity_dispose = async_track_state_change(
            hass,
            sun_entity_id,
            self._sun_entity_changed
        )

        sun_state = hass.states.get(sun_entity_id)
        if sun_state:
            self._sun_entity_changed(sun_entity_id, None, sun_state)

        # initialize horizon profile tracking
        self._track_horizon_profile_dispose = None
        self._horizon_profile_entity_id = ''
        self.horizon_profile_entity_id = horizon_profile_entity_id

    @property
    def door_and_window(self):
        """The `DoorAndWindow` instance associated to the controller."""
        return self._door_and_window

    @property
    def horizon_profile_entity_id(self) -> str:
        """ The """
        return self._horizon_profile_entity_id

    @horizon_profile_entity_id.setter
    def horizon_profile_entity_id(self, value: str) -> None:
        if value != self._horizon_profile_entity_id:
            if self._track_horizon_profile_dispose is not None:
                self._track_horizon_profile_dispose()
                self._track_horizon_profile_dispose = None

            self._horizon_profile_entity_id = value

            if value:
                self._track_horizon_profile_dispose = async_track_state_change(
                    self._hass,
                    value,
                    self._horizon_profile_entity_changed
                )

    # pylint: disable=unused-argument
    def _horizon_profile_entity_changed(self, entity_id: str, old_state: State, new_state: State):
        if isinstance(new_state.state, list):
            if len(new_state.state) >= 2:
                self._door_and_window.horizon_profile = new_state.state
            else:
                self._door_and_window.horizon_profile = [0, 0]

    # pylint: disable=unused-argument
    def _sun_entity_changed(self, entity_id: str, old_state: State, new_state: State):
        self._door_and_window.update(
            float(new_state.attributes['azimuth']),
            float(new_state.attributes['elevation'])
        )

    def dispose(self):
        """
        Removes all change tracking.
        """
        self._door_and_window.dispose()
        self._track_sun_entity_dispose()
