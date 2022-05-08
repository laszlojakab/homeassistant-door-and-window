""" The module contains the DoorAndWindow class. """


import math
from typing import Callable, List, Union

from ..converters.door_and_window_rectangles_to_light_information_converter import \
    DoorAndWindowRectanglesToLightInformationConverter
from ..converters.door_and_window_to_rectangles_converter import \
    DoorAndWindowToRectanglesConverter
from ..utils import normalize_angle
from .awning import Awning
from .door_and_window_rectangles import DoorAndWindowRectangles
from .event_handler import EventHandler

# pylint: disable=too-many-instance-attributes, too-many-public-methods


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
    # pylint: disable=too-many-arguments, too-many-locals

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
        horizon_profile: List[float],
        awning: Union[Awning, None]
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
                The elevation values of horizon as seen from the door and window.
            awning:
                The awning of for door and window.
        """
        self.type = type
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self._width = width
        self._width_changed = EventHandler()
        self._height = height
        self._height_changed = EventHandler()
        self._frame_face_thickness = frame_face_thickness
        self._frame_face_thickness_changed = EventHandler()
        self._frame_thickness = frame_thickness
        self._frame_thickness_changed = EventHandler()
        self._outside_depth = outside_depth
        self._outside_depth_changed = EventHandler()
        self._inside_depth = inside_depth
        self._inside_depth_changed = EventHandler()
        self._parapet_wall_height = parapet_wall_height
        self._parapet_wall_height_changed = EventHandler()
        self._azimuth = azimuth
        self._azimuth_changed = EventHandler()
        self._tilt = tilt
        self._tilt_changed = EventHandler()
        self._horizon_profile = horizon_profile
        self._horizon_profile_changed = EventHandler()
        self._awning = awning
        self._awning_changed = EventHandler()
        self._horizon_elevation_at_sun_azimuth = None
        self._horizon_elevation_at_sun_azimuth_changed = EventHandler()
        self._angle_of_incidence = None
        self._angle_of_incidence_changed = EventHandler()
        self._sunny_glazing_area: Union[float, None] = None
        self._sunny_glazing_area_changed = EventHandler()
        self._sunny_glazing_area_percentage: Union[float, None] = None
        self._sunny_glazing_area_percentage_changed = EventHandler()
        self._glazing_has_direct_sunlight: Union[bool, None] = None
        self._glazing_has_direct_sunlight_changed = EventHandler()
        self._rectangles: DoorAndWindowRectangles = None
        self._rectangles_spoiled: bool = True

    @property
    def horizon_profile(self) -> List[float]:
        """
        The elevation of horizon as seen from the door and window.
        The values are the measured horizon elevation from left to
        right in equal distances. There are at least two measurement for the most left
        and the most right place.
        """
        return self._horizon_profile

    @horizon_profile.setter
    def horizon_profile(self, value: List[float]) -> None:
        if value != self._horizon_profile:
            self._horizon_profile = value or [0, 0]
            self._horizon_profile_changed.fire(value)

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
        return self._horizon_profile_changed.listen(callback)

    @property
    def awning(self) -> Union[Awning, None]:
        """
        Gets or sets the awning associated to the door and window.
        """
        return self._awning

    @awning.setter
    def awning(self, value:  Union[Awning, None]) -> None:
        if value != self._awning:
            if self._awning:
                # calling dispose removes
                # eventhandler for on_current_depth_change event
                self._awning.dispose()

            self._awning = value
            self._awning_changed.fire(value)

            if self._awning:
                # pylint: disable=unused-argument
                def on_awning_depth_change(depth: float):
                    self._rectangles_spoiled = True

                self._awning.on_current_depth_changed(on_awning_depth_change)
            self._rectangles_spoiled = True

    def on_awning_changed(
        self,
        callback: Callable[[List[float]], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the awning property has changed.

        Args:
            callback:
                The function to call when awning property has changed.

        Returns:
            A function to stop calling the callback function
            when awning property has changed.
        """
        return self._awning_changed.listen(callback)

    @property
    def width(self) -> float:
        """ The width of door and window. """
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if value != self._width:
            self._width = value
            self._width_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._width_changed.listen(callback)

    @property
    def height(self) -> float:
        """ The height of door and window. """
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if value != self._height:
            self._height = value
            self._height_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._height_changed.listen(callback)

    @property
    def frame_face_thickness(self) -> float:
        """ The thickness of door and window frame face. """
        return self._frame_face_thickness

    @frame_face_thickness.setter
    def frame_face_thickness(self, value: float) -> None:
        if value != self._frame_face_thickness:
            self._frame_face_thickness = value
            self._frame_face_thickness_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._frame_face_thickness_changed.listen(callback)

    @property
    def frame_thickness(self) -> float:
        """ The thickness of door and window frame. """
        return self._frame_thickness

    @frame_thickness.setter
    def frame_thickness(self, value: float) -> None:
        if value != self._frame_thickness:
            self._frame_thickness = value
            self._frame_thickness_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._frame_thickness_changed.listen(callback)

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
            self._outside_depth_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._outside_depth_changed.listen(callback)

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
            self._inside_depth_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._inside_depth_changed.listen(callback)

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
            self._parapet_wall_height_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._parapet_wall_height_changed.listen(callback)

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
            self._azimuth_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._azimuth_changed.listen(callback)

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
            self._tilt_changed.fire(value)
            self._rectangles_spoiled = True

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
        return self._tilt_changed.listen(callback)

    @property
    def horizon_elevation_at_sun_azimuth(self) -> Union[float, None]:
        """
        The horizon elevation towards the sun.

        If the sun is behind the door and window the value is None.
        """
        return self._horizon_elevation_at_sun_azimuth

    def on_horizon_elevation_at_sun_azimuth_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the horizon_elevation_at_sun_azimuth
        property has changed.

        Args:
            callback:
                The function to call when horizon_elevation_at_sun_azimuth property has changed.

        Returns:
            A function to stop calling the callback function when
            horizon_elevation_at_sun_azimuth property has changed.
        """
        return self._horizon_elevation_at_sun_azimuth_changed.listen(callback)

    @property
    def angle_of_incidence(self) -> Union[float, None]:
        """
        The angle of incidence.
        """
        return self._angle_of_incidence

    def on_angle_of_incidence_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the angle_of_incidence
        property has changed.

        Args:
            callback:
                The function to call when angle_of_incidence property has changed.

        Returns:
            A function to stop calling the callback function when
            angle_of_incidence property has changed.
        """
        return self._angle_of_incidence_changed.listen(callback)

    @property
    def sunny_glazing_area(self) -> Union[float, None]:
        """
        The sunny glazing area.
        """
        return self._sunny_glazing_area

    def on_sunny_glazing_area_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the sunny_glazing_area
        property has changed.

        Args:
            callback:
                The function to call when sunny_glazing_area property has changed.

        Returns:
            A function to stop calling the callback function when
            sunny_glazing_area property has changed.
        """
        return self._sunny_glazing_area_changed.listen(callback)

    @property
    def sunny_glazing_area_percentage(self) -> Union[float, None]:
        """
        The sunny glazing area percentage.
        """
        return self._sunny_glazing_area_percentage

    def on_sunny_glazing_area_percentage_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the sunny_glazing_area_percentage
        property has changed.

        Args:
            callback:
                The function to call when sunny_glazing_area_percentage property has changed.

        Returns:
            A function to stop calling the callback function when
            sunny_glazing_area_percentage property has changed.
        """
        return self._sunny_glazing_area_percentage_changed.listen(callback)

    @property
    def glazing_has_direct_sunlight(self) -> Union[bool, None]:
        """
        The value indicates whether the glazing has direct sunlight.
        """
        return self._glazing_has_direct_sunlight

    def on_glazing_has_direct_sunlight_changed(
        self,
        callback: Callable[[bool], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the glazing_has_direct_sunlight
        property has changed.

        Args:
            callback:
                The function to call when glazing_has_direct_sunlight property has changed.

        Returns:
            A function to stop calling the callback function when
            glazing_has_direct_sunlight property has changed.
        """
        return self._glazing_has_direct_sunlight_changed.listen(callback)

    def update(self, sun_azimuth: float, sun_elevation: float):
        """
        Updates the instance based on the sun position.

        Args:
            sun_azimuth:
                The azimuth of the sun.
            sun_elevation:
                The elevation of the sun.
        """
        # recalculate horizon elevation at sun azimuth
        horizon_elevation_at_sun_azimuth = None
        azimuth = normalize_angle(sun_azimuth - self.azimuth)

        sun_position = azimuth + 90
        if 0 <= sun_position <= 180:
            # Sun is in front of the door and window

            # We calculate the degrees between each horizon profile points
            # this will be the horizon profile resolution
            horizon_profile_resolution = 180 / (len(self.horizon_profile) - 1)

            # We calculate the lower index at horizon profile array
            # of the position belongs to the sun's azimuth.
            horizon_profile_index = math.floor(sun_position / horizon_profile_resolution)

            if len(self.horizon_profile) - 1 == horizon_profile_index:
                # If the calculated horizon profile index is the last one
                # than the sun is barely visible (a moment later it won't be),
                # In that case we must use the last horizon profile elevation value
                horizon_elevation_at_sun_azimuth = self.horizon_profile[-1]
            else:
                # We calculate a weight which will tell us
                # the rate of the higher index elevation value
                # must be used for calculating the actual horizon elevation
                weight = (sun_position - horizon_profile_resolution *
                          horizon_profile_index) / horizon_profile_resolution

                # This is simple linear regression between the lower and
                # the higher index elevation value.
                horizon_elevation_at_sun_azimuth = \
                    self.horizon_profile[horizon_profile_index] * (1 - weight) + \
                    self.horizon_profile[horizon_profile_index + 1] * weight

            horizon_elevation_at_sun_azimuth = round(horizon_elevation_at_sun_azimuth, 2)
        else:
            # sun is behind the door and window
            horizon_elevation_at_sun_azimuth = None

        if self._horizon_elevation_at_sun_azimuth != horizon_elevation_at_sun_azimuth:
            self._horizon_elevation_at_sun_azimuth = horizon_elevation_at_sun_azimuth
            self._horizon_elevation_at_sun_azimuth_changed.fire(horizon_elevation_at_sun_azimuth)

        # If the size or faceing of the door and window change
        # we must update the associated rectangles.
        if self._rectangles_spoiled:
            self._rectangles = DoorAndWindowToRectanglesConverter().convert(self)
            self._rectangles_spoiled = False

        light_information = DoorAndWindowRectanglesToLightInformationConverter().convert(
            self._rectangles,
            self._horizon_elevation_at_sun_azimuth,
            self.azimuth,
            self.tilt,
            sun_azimuth,
            sun_elevation
        )

        # If angle of incidence has changed than we send a change event
        if self._angle_of_incidence != light_information.angle_of_incidence:
            self._angle_of_incidence = light_information.angle_of_incidence
            self._angle_of_incidence_changed.fire(self._angle_of_incidence)

        # If sunny glazing area has changed than we send a change event
        sunny_glazing_area: float = round(light_information.sunny_glazing_area_polygon.area, 2)
        if self._sunny_glazing_area != sunny_glazing_area:
            self._sunny_glazing_area = sunny_glazing_area
            self._sunny_glazing_area_changed.fire(self._sunny_glazing_area)

        # Calculate sunny glazing area percentage and send a change event if has changed
        glazing_area = (self.width - self.frame_face_thickness * 2) * \
            (self.height - self.frame_face_thickness * 2)
        sunny_glazing_area_percentage = round(sunny_glazing_area / glazing_area * 100, 2)
        if self._sunny_glazing_area_percentage != sunny_glazing_area_percentage:
            self._sunny_glazing_area_percentage = sunny_glazing_area_percentage
            self._sunny_glazing_area_percentage_changed.fire(self._sunny_glazing_area_percentage)

        # If sunny glazing area has changed than we send a change event
        glazing_has_direct_sunlight: bool = sunny_glazing_area > 0.01
        if self._glazing_has_direct_sunlight != glazing_has_direct_sunlight:
            self._glazing_has_direct_sunlight = glazing_has_direct_sunlight
            self._glazing_has_direct_sunlight_changed.fire(self._glazing_has_direct_sunlight)

    def dispose(self):
        """
        Destroys the current instance.
        """
        self._width_changed.dispose()
        self._height_changed.dispose()
        self._frame_face_thickness_changed.dispose()
        self._frame_thickness_changed.dispose()
        self._outside_depth_changed.dispose()
        self._inside_depth_changed.dispose()
        self._parapet_wall_height_changed.dispose()
        self._azimuth_changed.dispose()
        self._tilt_changed.dispose()
        self._horizon_profile_changed.dispose()
        self._horizon_elevation_at_sun_azimuth_changed.dispose()
        self._angle_of_incidence_changed.dispose()
        self._sunny_glazing_area_changed.dispose()
        self._sunny_glazing_area_percentage_changed.dispose()
        self._glazing_has_direct_sunlight_changed.dispose()
        self._awning_changed.dispose()
