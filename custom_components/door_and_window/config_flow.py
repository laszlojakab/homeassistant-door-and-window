""" The configuration flow handler module for the Door and window integration. """
import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import (CONF_FRAME_FACE_THICKNESS, CONF_FRAME_THICKNESS,
                    CONF_HEIGHT, CONF_INSIDE_DEPTH, CONF_MANUFACTURER,
                    CONF_MODEL, CONF_OUTSIDE_DEPTH, CONF_PARAPET_WALL_HEIGHT,
                    CONF_TYPE, CONF_WIDTH, DOMAIN, TYPE_DOOR, TYPE_WINDOW)

_LOGGER = logging.getLogger(__name__)


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
            else:
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
            self.hass.config_entries.async_update_entry(
                self.config_entry, data=self.data
            )

            return self.async_abort(reason="reconfigure_successful")

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
            self.hass.config_entries.async_update_entry(
                self.config_entry, data=self.data
            )

            return self.async_abort(reason="reconfigure_successful")

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
            else:
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
            return self.async_create_entry(
                title=self.data[CONF_NAME], data=self.data
            )

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
            return self.async_create_entry(
                title=self.data[CONF_NAME], data=self.data
            )

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