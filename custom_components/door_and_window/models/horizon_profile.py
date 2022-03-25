""" Module of horizon profiles. """

from abc import ABC, abstractmethod
from typing import Callable, List

from homeassistant.core import State
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.helpers.event import async_track_state_change

from .event import Event


class HorizonProfile(ABC):
    """ Represents a horizon profile seen from a door and window. """

    @property
    @abstractmethod
    def horizon_profile(self) -> List[float]:
        """
        The horizon profile.
        """

    @abstractmethod
    def on_horizon_profile_changed(
        self,
        callback: Callable[[List[float]], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the horizon_profile property has changed.

        Args:
            callback:
                The function to call when parapet_wall_height property has changed.

        Returns:
            A function to stop calling the callback function
            when parapet_wall_height property has changed.
        """

    @abstractmethod
    def dispose(self) -> None:
        """
        Disposes the current horizon profile.
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
        self._horion_profile = horizon_profile

    @property
    def horizon_profile(self) -> List[float]:
        return self._horion_profile

    def on_horizon_profile_changed(
        self,
        callback: Callable[[List[float]], None]
    ) -> Callable[[], None]:
        def empty_function():
            pass

        return empty_function

    def dispose(self) -> None:
        pass


class DynamicHorizonProfile(HorizonProfile):
    """
    Represents a horizon profile which is supported by an entity.
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
        self._horizon_profile = [0, 0]
        self._on_horizon_profile_changed = Event()

        # pylint: disable=unused-argument
        def update_horizon_profile(entity_id: str, old_state: State, new_state: State) -> None:
            self._horizon_profile = new_state.state

        self._track_horizon_profile_entity_dispose = async_track_state_change(
            hass,
            horizon_profile_entity_id,
            update_horizon_profile
        )

    @property
    def horizon_profile(self) -> List[float]:
        return self._horizon_profile

    def dispose(self) -> None:
        self._track_horizon_profile_entity_dispose()

    def on_horizon_profile_changed(
        self,
        callback: Callable[[List[float]], None]
    ) -> Callable[[], None]:
        return self._on_horizon_profile_changed.add_listener(callback)
