""" The module for coordinator. """
from typing import Callable, List

from homeassistant.core import State
from homeassistant.helpers.event import async_track_state_change
from homeassistant.helpers.typing import HomeAssistantType

from .converters.door_and_window_to_rectangles_converter import \
    DoorAndWindowToRectanglesConverter
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
        sun_entity_id: str
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
        """
        self._door_and_window = door_and_window
        self._hass = hass
        self._rectangles = DoorAndWindowToRectanglesConverter().convert(door_and_window)

        # initialize door and window size and facing tracking
        self._door_and_window_events_disposes: List[Callable[[], None]] = [
            self._door_and_window.on_azimuth_changed(self._on_needs_rectangles_update),
            self._door_and_window.on_frame_face_thickness_changed(self._on_needs_rectangles_update),
            self._door_and_window.on_frame_thickness_changed(self._on_needs_rectangles_update),
            self._door_and_window.on_height_changed(self._on_needs_rectangles_update),
            self._door_and_window.on_inside_depth_changed(self._on_needs_rectangles_update),
            self._door_and_window.on_outside_depth_changed(self._on_needs_rectangles_update),
            self._door_and_window.on_parapet_wall_height_changed(self._on_needs_rectangles_update),
            self._door_and_window.on_tilt_changed(self._on_needs_rectangles_update),
            self._door_and_window.on_width_changed(self._on_needs_rectangles_update),
        ]

        # initialize sun tracking
        self._track_sun_entity_dispose = async_track_state_change(
            hass,
            sun_entity_id,
            self._sun_entity_changed
        )

        sun_state = hass.states.get(sun_entity_id)
        if sun_state:
            self._sun_entity_changed(sun_entity_id, None, sun_state)

    @property
    def door_and_window(self):
        """The `DoorAndWindow` instance associated to the controller."""
        return self._door_and_window

    # pylint: disable=unused-argument
    def _sun_entity_changed(self, entity_id: str, old_state: State, new_state: State):
        self._door_and_window.update(
            float(new_state.attributes['azimuth']),
            float(new_state.attributes['elevation'])
        )

    # pylint: disable=unused-argument
    def _on_needs_rectangles_update(self, new_value: float):
        """
        Updates the rectangles of door and window whenever
        the door and window size or facing parameters has changed.
        """
        self._rectangles = DoorAndWindowToRectanglesConverter().convert(self._door_and_window)

    def dispose(self):
        """
        Removes all change tracking.
        """
        self._door_and_window.dispose()
        self._track_sun_entity_dispose()
        for dispose_door_and_window_event in self._door_and_window_events_disposes:
            dispose_door_and_window_event()
