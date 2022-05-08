""" The configuration flow handler module for the Door and window integration. """
import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.entity_registry import async_get_registry

from .const import (CONF_AWNING_CLOSEST_TOP, CONF_AWNING_COVER_ENTITY,
                    CONF_AWNING_DISTANCE, CONF_AWNING_FARTHEST_TOP,
                    CONF_AWNING_LEFT_DISTANCE, CONF_AWNING_MAX_DEPTH,
                    CONF_AWNING_MIN_DEPTH, CONF_AWNING_RIGHT_DISTANCE,
                    CONF_AZIMUTH, CONF_FRAME_FACE_THICKNESS,
                    CONF_FRAME_THICKNESS, CONF_HAS_AWNING, CONF_HEIGHT,
                    CONF_HORIZON_PROFILE,
                    CONF_HORIZON_PROFILE_NUMBER_OF_MEASUREMENTS,
                    CONF_HORIZON_PROFILE_TYPE, CONF_INSIDE_DEPTH,
                    CONF_MANUFACTURER, CONF_MODEL, CONF_OUTSIDE_DEPTH,
                    CONF_PARAPET_WALL_HEIGHT, CONF_TILT, CONF_TYPE, CONF_WIDTH,
                    DOMAIN, HORIZON_PROFILE_TYPE_STATIC, TYPE_DOOR,
                    TYPE_WINDOW)

_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-locals
class WindowAndDoorDeviceOptionsFlow(config_entries.OptionsFlow):
    """ The options flow handler for the Door and window integration. """

    def __init__(self, config_entry: config_entries.ConfigEntry):
        self.config_entry = config_entry
        self.updated_config = {}
        self.data: dict[str, any] = {}

    async def async_step_init(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the init step of the options flow.

        During the init step the user can change the following properties:

        - type
        - manufacturer
        - model

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.config_entry.data | user_input
            if user_input[CONF_TYPE] == TYPE_WINDOW:
                return await self.async_step_window_dimensions()

            return await self.async_step_door_dimensions()

        return self.async_show_form(step_id="init", data_schema=vol.Schema({
            vol.Required(
                CONF_TYPE,
                default=self.config_entry.data[CONF_TYPE]
            ): vol.In({TYPE_WINDOW: 'Window', TYPE_DOOR: 'Door'}),
            vol.Optional(
                CONF_MANUFACTURER,
                default=self.config_entry.data.get(CONF_MANUFACTURER, '')
            ): str,
            vol.Optional(
                CONF_MODEL,
                default=self.config_entry.data.get(CONF_MODEL, '')
            ): str
        }))

    async def async_step_window_dimensions(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of setting window dimensions.

        During the this step the user can change the following properties:

        - width
        - height
        - outside depth
        - inside depth
        - frame thickness
        - frame face thickness
        - parapet wall height

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            return await self.async_step_facing()

        return self.async_show_form(
            step_id="window_dimensions",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_WIDTH,
                    default=self.config_entry.data[CONF_WIDTH]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_HEIGHT,
                    default=self.config_entry.data[CONF_HEIGHT]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_OUTSIDE_DEPTH,
                    default=self.config_entry.data[CONF_OUTSIDE_DEPTH]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_INSIDE_DEPTH,
                    default=self.config_entry.data[CONF_INSIDE_DEPTH]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_FRAME_THICKNESS,
                    default=self.config_entry.data[CONF_FRAME_THICKNESS]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_FRAME_FACE_THICKNESS,
                    default=self.config_entry.data[CONF_FRAME_FACE_THICKNESS]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Optional(
                    CONF_PARAPET_WALL_HEIGHT,
                    default=self.config_entry.data[CONF_PARAPET_WALL_HEIGHT]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
            })
        )

    async def async_step_door_dimensions(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of setting door dimensions.

        During the this step the user can change the following properties:

        - width
        - height
        - outside depth
        - inside depth
        - frame thickness
        - frame face thickness

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            return await self.async_step_facing()

        return self.async_show_form(
            step_id="door_dimensions",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_WIDTH,
                    default=self.config_entry.data[CONF_WIDTH]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_HEIGHT,
                    default=self.config_entry.data[CONF_HEIGHT]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_OUTSIDE_DEPTH,
                    default=self.config_entry.data[CONF_OUTSIDE_DEPTH]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_INSIDE_DEPTH,
                    default=self.config_entry.data[CONF_INSIDE_DEPTH]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_FRAME_THICKNESS,
                    default=self.config_entry.data[CONF_FRAME_THICKNESS]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(
                    CONF_FRAME_FACE_THICKNESS,
                    default=self.config_entry.data[CONF_FRAME_FACE_THICKNESS]
                ): vol.All(vol.Coerce(int), vol.Range(min=0)),
            })
        )

    async def async_step_facing(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of setting door and window facing.

        During the this step the user can change the following properties:

        - tilt
        - azimuth

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            return await self.async_step_horizon_profile_number_of_measurements()

        return self.async_show_form(
            step_id="facing",
            data_schema=vol.Schema({
                vol.Required(CONF_TILT, default=self.config_entry.data[CONF_TILT]):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=90)),
                vol.Required(CONF_AZIMUTH, default=self.config_entry.data[CONF_AZIMUTH]):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=359)),
            })
        )

    async def async_step_horizon_profile_number_of_measurements(
        self,
        user_input: dict[str, any] = None
    ) -> FlowResult:
        """
        Handles the step of setting static horizon profile measurements count.

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            self.data[CONF_HORIZON_PROFILE_TYPE] = HORIZON_PROFILE_TYPE_STATIC
            return await self.async_step_horizon_profile_measurements()

        return self.async_show_form(
            step_id="horizon_profile_number_of_measurements",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_HORIZON_PROFILE_NUMBER_OF_MEASUREMENTS,
                    default=(self.config_entry.data.get(
                        CONF_HORIZON_PROFILE_NUMBER_OF_MEASUREMENTS) or 2)
                ): vol.All(vol.Coerce(int), vol.Range(min=2, max=19))
            })
        )

    async def async_step_horizon_profile_measurements(
        self,
        user_input: dict[str, any] = None
    ) -> FlowResult:
        """
        Handles the step of setting static horizon profile measurements.

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data[CONF_HORIZON_PROFILE] = []
            for i in range(0, 19):
                if f"horizon_profile_{i}" in user_input:
                    self.data[CONF_HORIZON_PROFILE].append(
                        user_input[f"horizon_profile_{i}"])
                else:
                    break

            return await self.async_step_has_awning()

        schema = {}

        for i in range(0, self.data[CONF_HORIZON_PROFILE_NUMBER_OF_MEASUREMENTS]):
            schema[
                vol.Required(
                    f"horizon_profile_{i}",
                    default=(self.config_entry.data[CONF_HORIZON_PROFILE][i] if i < len(
                        self.config_entry.data[CONF_HORIZON_PROFILE]) else 0)
                    if CONF_HORIZON_PROFILE in self.config_entry.data
                    else 0
                )
            ] = vol.All(
                vol.Coerce(int), vol.Range(min=0, max=90))

        return self.async_show_form(
            step_id="horizon_profile_measurements",
            data_schema=vol.Schema(schema)
        )

    async def async_step_has_awning(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of querying if an awning attached to the door and window.

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            if self.data[CONF_HAS_AWNING]:
                return await self.async_step_awning()

            self.hass.config_entries.async_update_entry(
                self.config_entry, data=self.data
            )

            return self.async_abort(reason="reconfigure_successful")

        return self.async_show_form(
            step_id="has_awning",
            data_schema=vol.Schema({
                vol.Required(CONF_HAS_AWNING, default=self.config_entry.data[CONF_HAS_AWNING]): bool
            })
        )

    async def async_step_awning(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of setting awning parameters.

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input

            self.hass.config_entries.async_update_entry(
                self.config_entry, data=self.data
            )

            return self.async_abort(reason="reconfigure_successful")

        entity_registry = await async_get_registry(self.hass)

        return self.async_show_form(
            step_id="awning",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_AWNING_MIN_DEPTH,
                    default=self.config_entry.data[CONF_AWNING_MIN_DEPTH]
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=10000)),
                vol.Required(
                    CONF_AWNING_MAX_DEPTH,
                    default=self.config_entry.data[CONF_AWNING_MAX_DEPTH]
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=10000)),
                vol.Required(
                    CONF_AWNING_LEFT_DISTANCE,
                    default=self.config_entry.data[CONF_AWNING_LEFT_DISTANCE]
                ): vol.All(vol.Coerce(int), vol.Range(min=-10000, max=10000)),
                vol.Required(
                    CONF_AWNING_RIGHT_DISTANCE,
                    default=self.config_entry.data[CONF_AWNING_RIGHT_DISTANCE]
                ): vol.All(vol.Coerce(int), vol.Range(min=-10000, max=10000)),
                vol.Required(
                    CONF_AWNING_CLOSEST_TOP,
                    default=self.config_entry.data[CONF_AWNING_CLOSEST_TOP]
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=1500)),
                vol.Required(
                    CONF_AWNING_FARTHEST_TOP,
                    default=self.config_entry.data[CONF_AWNING_FARTHEST_TOP]
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=1500)),
                vol.Required(
                    CONF_AWNING_DISTANCE,
                    default=self.config_entry.data[CONF_AWNING_DISTANCE]
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=5000)),
                vol.Optional(
                    CONF_AWNING_COVER_ENTITY,
                    default=self.config_entry.data.get(CONF_AWNING_COVER_ENTITY, None)
                ): vol.In(
                    [None] + [x for x in entity_registry.entities.keys() if x.startswith("cover.")]
                )
            })
        )


@config_entries.HANDLERS.register(DOMAIN)
class WindowAndDoorDeviceConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """ The configuration flow handler for Door and window integration. """
    VERSION = 1

    def __init__(self):
        self.data: dict[str, any] = None

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: config_entries.ConfigFlow):
        return WindowAndDoorDeviceOptionsFlow(config_entry)

    async def async_step_user(self, user_input: dict[str, any] = None) -> FlowResult:
        if user_input is not None:
            self.data = user_input
            if user_input[CONF_TYPE] == TYPE_WINDOW:
                return await self.async_step_window_dimensions()

            return await self.async_step_door_dimensions()

        return self.async_show_form(step_id="user", data_schema=vol.Schema({
            vol.Required(CONF_TYPE): vol.In({TYPE_WINDOW: 'Window', TYPE_DOOR: 'Door'}),
            vol.Required(CONF_NAME): str,
            vol.Optional(CONF_MANUFACTURER): str,
            vol.Optional(CONF_MODEL): str
        }))

    async def async_step_window_dimensions(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of setting window dimensions.

        During the this step the user can set the following properties:

        - width
        - height
        - outside depth
        - inside depth
        - frame thickness
        - frame face thickness
        - parapet wall height

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            return await self.async_step_facing()

        return self.async_show_form(
            step_id="window_dimensions",
            data_schema=vol.Schema({
                vol.Required(CONF_WIDTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_HEIGHT):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_OUTSIDE_DEPTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_INSIDE_DEPTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_FRAME_THICKNESS):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_FRAME_FACE_THICKNESS):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_PARAPET_WALL_HEIGHT, default=900):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
            })
        )

    async def async_step_door_dimensions(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of setting door dimensions.

        During the this step the user can set the following properties:

        - width
        - height
        - outside depth
        - inside depth
        - frame thickness
        - frame face thickness

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            return await self.async_step_facing()

        return self.async_show_form(
            step_id="door_dimensions",
            data_schema=vol.Schema({
                vol.Required(CONF_WIDTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_HEIGHT):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_OUTSIDE_DEPTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_INSIDE_DEPTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_FRAME_THICKNESS):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
                vol.Required(CONF_FRAME_FACE_THICKNESS):
                    vol.All(vol.Coerce(int), vol.Range(min=0)),
            })
        )

    async def async_step_facing(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of setting door and window facing.

        During the this step the user can set the following properties:

        - tilt
        - azimuth

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            return await self.async_step_horizon_profile_number_of_measurements()

        return self.async_show_form(
            step_id="facing",
            data_schema=vol.Schema({
                vol.Required(CONF_TILT, default=90):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=90)),
                vol.Required(CONF_AZIMUTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=359)),
            })
        )

    async def async_step_horizon_profile_number_of_measurements(
        self,
        user_input: dict[str, any] = None
    ) -> FlowResult:
        """
        Handles the step of setting static horizon profile measurements count.

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            self.data[CONF_HORIZON_PROFILE_TYPE] = HORIZON_PROFILE_TYPE_STATIC
            return await self.async_step_horizon_profile_measurements()

        return self.async_show_form(
            step_id="horizon_profile_number_of_measurements",
            data_schema=vol.Schema({
                vol.Required(CONF_HORIZON_PROFILE_NUMBER_OF_MEASUREMENTS):
                    vol.All(vol.Coerce(int), vol.Range(min=2, max=19))
            })
        )

    async def async_step_horizon_profile_measurements(
        self,
        user_input: dict[str, any] = None
    ) -> FlowResult:
        """
        Handles the step of setting static horizon profile measurements.

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data[CONF_HORIZON_PROFILE] = []
            for i in range(0, 19):
                if f"horizon_profile_{i}" in user_input:
                    self.data[CONF_HORIZON_PROFILE].append(
                        user_input[f"horizon_profile_{i}"])
                else:
                    break

            return await self.async_step_has_awning()

        schema = {}

        for i in range(0, self.data[CONF_HORIZON_PROFILE_NUMBER_OF_MEASUREMENTS]):
            schema[vol.Required(f"horizon_profile_{i}", default=0)] = vol.All(
                vol.Coerce(int), vol.Range(min=0, max=90))

        return self.async_show_form(
            step_id="horizon_profile_measurements",
            data_schema=vol.Schema(schema)
        )

    async def async_step_has_awning(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of querying if an awning attached to the door and window.

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            if self.data[CONF_HAS_AWNING]:
                return await self.async_step_awning()

            return self.async_create_entry(
                title=self.data[CONF_NAME], data=self.data
            )

        return self.async_show_form(
            step_id="has_awning",
            data_schema=vol.Schema({
                vol.Required(CONF_HAS_AWNING): bool
            })
        )

    async def async_step_awning(self, user_input: dict[str, any] = None) -> FlowResult:
        """
        Handles the step of setting awning parameters.

        Args:
            user_input:
                The values entered by the user on the UI.

        Returns:
            The result of the options flow step.
        """
        if user_input is not None:
            self.data = self.data | user_input
            return self.async_create_entry(
                title=self.data[CONF_NAME], data=self.data
            )

        entity_registry = await async_get_registry(self.hass)

        return self.async_show_form(
            step_id="awning",
            data_schema=vol.Schema({
                vol.Required(CONF_AWNING_MIN_DEPTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=10000)),
                vol.Required(CONF_AWNING_MAX_DEPTH):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=10000)),
                vol.Required(CONF_AWNING_LEFT_DISTANCE, default=0):
                    vol.All(vol.Coerce(int), vol.Range(min=-10000, max=10000)),
                vol.Required(CONF_AWNING_RIGHT_DISTANCE, default=0):
                    vol.All(vol.Coerce(int), vol.Range(min=-10000, max=10000)),
                vol.Required(CONF_AWNING_CLOSEST_TOP):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=1500)),
                vol.Required(CONF_AWNING_FARTHEST_TOP):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=1500)),
                vol.Required(CONF_AWNING_DISTANCE, default=0):
                    vol.All(vol.Coerce(int), vol.Range(min=0, max=5000)),
                vol.Optional(CONF_AWNING_COVER_ENTITY):
                    vol.In(
                        [""] +
                        [x for x in entity_registry.entities.keys() if x.startswith("cover.")]
                )
            })
        )
