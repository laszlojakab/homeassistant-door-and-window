""" The module contains the DoorAndWindow class. """


from typing import List
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
        self.width = width
        self.height = height
        self.frame_face_thickness = frame_face_thickness
        self.frame_thickness = frame_thickness
        self.outside_depth = outside_depth
        self.inside_depth = inside_depth
        self.parapet_wall_height = parapet_wall_height
        self.azimuth = azimuth
        self.tilt = tilt
        self._horizon_profile = horizon_profile

    def horizon_profile(self) -> List[float]:
        """
        The elevation of horizon as seen from the door and window.
        The values are the measured horizon elevation from left to
        right in equal distances. There are at least two measurement for the most left
        and the most right place.
        """
        return self._horizon_profile.get_horizon_profile()

    def destroy(self):
        """
        Destroyes the current instance.
        """
        self._horizon_profile.destroy()
