import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.data_entry_flow import FlowResult

from .const import (CONF_MANUFACTURER, CONF_MODEL, CONF_TYPE, DOMAIN,
                    TYPE_DOOR, TYPE_WINDOW)

_LOGGER = logging.getLogger(__name__)


@config_entries.HANDLERS.register(DOMAIN)
class WindowAndDoorDeviceConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """ The configuration flow handler for Door and window integration. """
    VERSION = 1

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
