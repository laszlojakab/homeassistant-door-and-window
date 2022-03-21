""" Module of horizon profiles. """

from abc import ABC, abstractmethod
from typing import List

from homeassistant.core import State
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.helpers.event import async_track_state_change


class HorizonProfile(ABC):
    """ Represents a horizon profile seen from a door and window. """
    @abstractmethod
    def get_horizon_profile(self) -> List[float]:
        """
        Gets the horizon profile.

        Returns:
            The horizon_profile
        """

    @abstractmethod
    def destroy(self) -> None:
        """
        Destroyes the current horizon profile.
        """


class StaticHorizonProfile(HorizonProfile):
    """
    Represents a horizon profile which is not changing.
    """

    def __init__(self, horizon_profile: List[float]):
        """
        Initialize the horizon profile with the specified values.

        Args:
            horizon_profile:
                The horizon profile elevation values.
        """
        self.horion_profile = horizon_profile

    def get_horizon_profile(self) -> List[float]:
        return self.horion_profile

    def destroy(self) -> None:
        pass


class DynamicHorizonProfile(HorizonProfile):
    """
    Represents a horizon profile which is supported by an external function.
    """

    def __init__(self, hass: HomeAssistantType, horizon_profile_entity_id: str):
        """
        Initialize a new instance of `DynamicHorizonProfile` class.

        Args:
            hass:
                The Home Assistant instance.
            horizon_profile_entity_id:
                The id of the entity which provides the horizon profile.
        """
        self.horizon_profile = [0, 0]

        # pylint: disable=unused-argument
        def update_horizon_profile(entity_id: str, old_state: State, new_state: State) -> None:
            self.horizon_profile = new_state.state

        self.destroy_callback = async_track_state_change(
            hass,
            horizon_profile_entity_id,
            update_horizon_profile
        )

    def get_horizon_profile(self) -> List[float]:
        return self.horizon_profile

    def destroy(self) -> None:
        self.destroy_callback()
