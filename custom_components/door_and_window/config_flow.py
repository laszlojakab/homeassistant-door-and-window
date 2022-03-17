""" The configuration flow handler module for the Door and window integration. """
import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import (CONF_MANUFACTURER, CONF_MODEL, CONF_TYPE, DOMAIN,
                    TYPE_DOOR, TYPE_WINDOW)

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

        Returns
            The result of the options flow step.
        """
        if user_input is not None:
            self.hass.config_entries.async_update_entry(
                self.config_entry, data=self.config_entry.data | user_input
            )

            return self.async_abort(reason="reconfigure_successful")

        return self.async_show_form(step_id="init", data_schema=vol.Schema({
            vol.Required(CONF_TYPE, default=self.config_entry.data[CONF_TYPE]):
                vol.In({TYPE_WINDOW: 'Window', TYPE_DOOR: 'Door'}),
            vol.Optional(CONF_MANUFACTURER, default=self.config_entry.data[CONF_MANUFACTURER]): str,
            vol.Optional(CONF_MODEL, default=self.config_entry.data[CONF_MODEL]): str
        }))


@config_entries.HANDLERS.register(DOMAIN)
class WindowAndDoorDeviceConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """ The configuration flow handler for Door and window integration. """
    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: config_entries.ConfigFlow):
        return WindowAndDoorDeviceOptionsFlow(config_entry)

    async def async_step_user(self, user_input: dict[str, any] = None) -> FlowResult:
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME], data=user_input
            )

        return self.async_show_form(step_id="user", data_schema=vol.Schema({
            vol.Required(CONF_TYPE): vol.In({TYPE_WINDOW: 'Window', TYPE_DOOR: 'Door'}),
            vol.Required(CONF_NAME): str,
            vol.Optional(CONF_MANUFACTURER): str,
            vol.Optional(CONF_MODEL): str
        }))
