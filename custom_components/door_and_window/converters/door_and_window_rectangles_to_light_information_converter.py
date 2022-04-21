""" Module for DoorAndWindowRectanglesToLightInformationConverter class. """
from shapely.geometry import Polygon

from ..converters.door_and_window_rectangles_to_polygons_converter import \
    DoorAndWindowRectanglesToPolygonsConverter
from ..models.door_and_window_light_information import \
    DoorAndWindowLightInformation
from ..models.door_and_window_rectangles import DoorAndWindowRectangles
from ..transformers.door_and_window_seen_from_sun_transformer import \
    DoorAndWindowRectanglesSeenFromSunTransformer

# pylint: disable=too-few-public-methods
class DoorAndWindowRectanglesToLightInformationConverter():
    """ Responsible for converting door and window rectangles to light information. """

    # pylint: disable=too-many-arguments
    @classmethod
    def convert(
        cls,
        door_and_window_rectangles: DoorAndWindowRectangles,
        angle_of_incidence: float,
        horizon_elevation_at_sun_azimuth: float,
        solar_azimuth: float,
        solar_elevation: float
    ) -> DoorAndWindowLightInformation:
        """
        Converts the specified door and window 3D rectangles
        to light information

        Args:
            door_and_window_rectangles:
                The door and window rectangles to convert.
            angle_of_incidence:
                The angle of incidence.
            horizon_elevation_at_sun_azimuth:
                The horizon elevation at sun azimuth.
            solar_azimuth:
                The sun's azimuth.
            solar_elevation:
                The sun's elevation.

        Returns:
            The door and window light information instance
            which describes the light state of the door and window.
        """
        if angle_of_incidence >= 90:
            # the sun is behind the door and window
            return DoorAndWindowLightInformation(angle_of_incidence, Polygon())

        if horizon_elevation_at_sun_azimuth > solar_elevation:
            # the sun is below the horizon
            return DoorAndWindowLightInformation(angle_of_incidence, Polygon())

        door_and_window_transformer = DoorAndWindowRectanglesSeenFromSunTransformer()

        door_and_window_rectangles_to_polygons_converter = \
            DoorAndWindowRectanglesToPolygonsConverter()

        door_and_window_rectangles_seen_from_sun = door_and_window_transformer.transform(
            door_and_window_rectangles,
            solar_azimuth,
            solar_elevation
        )

        door_and_window_polygons = door_and_window_rectangles_to_polygons_converter.convert(
            door_and_window_rectangles_seen_from_sun
        )

        sunny_glazing_area_polygon = door_and_window_polygons.glazing \
            .difference(door_and_window_polygons.outside_left_jamb_wall) \
            .difference(door_and_window_polygons.outside_right_jamb_wall) \
            .difference(door_and_window_polygons.outside_head_jamb_wall) \
            .difference(door_and_window_polygons.outside_stool)

        return DoorAndWindowLightInformation(angle_of_incidence, sunny_glazing_area_polygon)
