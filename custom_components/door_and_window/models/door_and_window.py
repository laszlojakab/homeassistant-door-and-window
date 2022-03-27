""" The module contains the DoorAndWindow class. """


from typing import Any, Callable, List

from .event import Event
from .horizon_profile import HorizonProfile


class DoorAndWindow():
    """
    Represents a door and window object.

    Attributes:
        type:
            The type of door and window. Possible values: "door", "window"
        name:
            The name of the door and window.
        manufacturer:
            The manufacturer of the door and window.
        model:
            The model of the door and window.
    """

    def __init__(
        self,
        # pylint: disable=redefined-builtin
        type: str,
        name: str,
        manufacturer: str,
        model: str,
        width: float,
        height: float,
        frame_thickness: float,
        frame_face_thickness: float,
        outside_depth: float,
        inside_depth: float,
        parapet_wall_height: float,
        azimuth: float,
        tilt: float,
        horizon_profile: HorizonProfile
    ):
        """
        Initialize a new instance of DoorAndWindow class

        Args:
            type:
                The type of door and window. Possible values: "door", "window"
            name:
                The name of the door and window.
            manufacturer:
                The manufacturer of the door and window.
            model:
                The model of the door and window.
            width:
                The width of door and window.
            height:
                The height of door and window.
            frame_thickness:
                The thickness of door and window frame.
            frame_face_thickness:
                The thickness of door and window frame face.
            outside_depth:
                The distance between the outside wall face and
                the outside door and window frame face.
            inside_depth:
                The distance between the inside wall face and
                the inside door and window frame face.
            parapet_wall_height:
                The height of the parapet wall. This is the distance between the floor and
                the bottom of a window. For doors it should be 0.
            azimuth:
                The azimuth of the door and window outside face.
                For north heading door and window it is 0° for east heading
                this value is 90°, and so on.
            tilt:
                The tilt of the door and window. If the window is perpendicular to the floor
                then it should be 90° degree.
                For roof tilted windows this value should be the roof tilt angle.
            horizon_profile:
                The `HorizonProfile` instance which provides the elevation values
                of horizon as seen from the door and window.
        """
        self.type = type
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self._width = width
        self._height = height
        self._frame_face_thickness = frame_face_thickness
        self._frame_thickness = frame_thickness
        self._outside_depth = outside_depth
        self._inside_depth = inside_depth
        self._parapet_wall_height = parapet_wall_height
        self._azimuth = azimuth
        self._tilt = tilt
        self._horizon_profile = horizon_profile
        self._events: dict[str, Event] = {}

    @property
    def horizon_profile(self) -> List[float]:
        """
        The elevation of horizon as seen from the door and window.
        The values are the measured horizon elevation from left to
        right in equal distances. There are at least two measurement for the most left
        and the most right place.
        """
        return self._horizon_profile.horizon_profile

    def on_horizon_profile_changed(
        self,
        callback: Callable[[List[float]], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the horizon_profile property has changed.

        Args:
            callback:
                The function to call when horizon_profile property has changed.

        Returns:
            A function to stop calling the callback function
            when horizon_profile property has changed.
        """
        return self._horizon_profile.on_horizon_profile_changed(callback)

    @property
    def width(self) -> float:
        """ The width of door and window. """
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if value != self._width:
            self._width = value
            self.__get_change_event('width')(value)

    def on_width_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the width property has changed.

        Args:
            callback:
                The function to call when width property has changed.

        Returns:
            A function to stop calling the callback function when width property has changed.
        """
        return self.__track_change('width', callback)

    @property
    def height(self) -> float:
        """ The height of door and window. """
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if value != self._height:
            self._height = value
            self.__get_change_event('height')(value)

    def on_height_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the height property has changed.

        Args:
            callback:
                The function to call when height property has changed.

        Returns:
            A function to stop calling the callback function when height property has changed.
        """
        return self.__track_change('height', callback)

    @property
    def frame_face_thickness(self) -> float:
        """ The thickness of door and window frame face. """
        return self._frame_face_thickness

    @frame_face_thickness.setter
    def frame_face_thickness(self, value: float) -> None:
        if value != self._frame_face_thickness:
            self._frame_face_thickness = value
            self.__get_change_event('frame_face_thickness')(value)

    def on_frame_face_thickness_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the frame_face_thickness property has changed.

        Args:
            callback:
                The function to call when frame_face_thickness property has changed.

        Returns:
            A function to stop calling the callback function when
            frame_face_thickness property has changed.
        """
        return self.__track_change('frame_face_thickness', callback)

    @property
    def frame_thickness(self) -> float:
        """ The thickness of door and window frame. """
        return self._frame_thickness

    @frame_thickness.setter
    def frame_thickness(self, value: float) -> None:
        if value != self._frame_thickness:
            self._frame_thickness = value
            self.__get_change_event('frame_thickness')(value)

    def on_frame_thickness_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the frame_thickness property has changed.

        Args:
            callback:
                The function to call when frame_thickness property has changed.

        Returns:
            A function to stop calling the callback function
            when frame_thickness property has changed.
        """
        return self.__track_change('frame_thickness', callback)

    @property
    def outside_depth(self) -> float:
        """
        The distance between the outside wall face and
        the outside door and window frame face.
        """
        return self._outside_depth

    @outside_depth.setter
    def outside_depth(self, value: float) -> None:
        if value != self._outside_depth:
            self._outside_depth = value
            self.__get_change_event('outside_depth')(value)

    def on_outside_depth_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the outside_depth property has changed.

        Args:
            callback:
                The function to call when outside_depth property has changed.

        Returns:
            A function to stop calling the callback function when
            outside_depth property has changed.
        """
        return self.__track_change('outside_depth', callback)

    @property
    def inside_depth(self) -> float:
        """
        The distance between the inside wall face and
        the inside door and window frame face.
        """
        return self._inside_depth

    @inside_depth.setter
    def inside_depth(self, value: float) -> None:
        if value != self._inside_depth:
            self._inside_depth = value
            self.__get_change_event('inside_depth')(value)

    def on_inside_depth_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the inside_depth property has changed.

        Args:
            callback:
                The function to call when inside_depth property has changed.

        Returns:
            A function to stop calling the callback function when inside_depth property has changed.
        """
        return self.__track_change('inside_depth', callback)

    @property
    def parapet_wall_height(self) -> float:
        """
        The height of the parapet wall. This is the distance between the floor and
        the bottom of a window. For doors it should be 0.
        """
        return self._parapet_wall_height

    @parapet_wall_height.setter
    def parapet_wall_height(self, value: float) -> None:
        if value != self._parapet_wall_height:
            self._parapet_wall_height = value
            self.__get_change_event('parapet_wall_height')(value)

    def on_parapet_wall_height_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the parapet_wall_height property has changed.

        Args:
            callback:
                The function to call when parapet_wall_height property has changed.

        Returns:
            A function to stop calling the callback function
            when parapet_wall_height property has changed.
        """
        return self.__track_change('parapet_wall_height', callback)

    @property
    def azimuth(self) -> float:
        """
        The azimuth of the door and window outside face.
        For north heading door and window it is 0° for east heading
        this value is 90°, and so on.
        """
        return self._azimuth

    @azimuth.setter
    def azimuth(self, value: float) -> None:
        if value != self._azimuth:
            self._azimuth = value
            self.__get_change_event('azimuth')(value)

    def on_azimuth_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the azimuth property has changed.

        Args:
            callback:
                The function to call when azimuth property has changed.

        Returns:
            A function to stop calling the callback function when azimuth property has changed.
        """
        return self.__track_change('azimuth', callback)

    @property
    def tilt(self) -> float:
        """
        The tilt of the door and window. If the window is perpendicular to the floor
        then it should be 90° degree.
        For roof tilted windows this value should be the roof tilt angle.
        """
        return self._tilt

    @tilt.setter
    def tilt(self, value: float) -> None:
        if value != self._tilt:
            self._tilt = value
            self.__get_change_event('tilt')(value)

    def on_tilt_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the tilt property has changed.

        Args:
            callback:
                The function to call when tilt property has changed.

        Returns:
            A function to stop calling the callback function when tilt property has changed.
        """
        return self.__track_change('tilt', callback)

    def dispose(self):
        """
        Destroys the current instance.
        """
        self._horizon_profile.dispose()

        for event in self._events.values():
            event.clear_event_listeners()

    def __track_change(self, prop: str, callback: Callable[[Any], None]) -> Callable[[], None]:
        """
        Tracks the change of a property
        """
        event = self.__get_change_event(prop)
        event.add_listener(callback)

        def untrack():
            event = self.__get_change_event(prop)
            event.remove_listener(callback)

        return untrack

    def __get_change_event(self, prop: str):
        event = self._events.get(prop, None)
        if event is None:
            self._events[prop] = event = event = Event()

        return event
