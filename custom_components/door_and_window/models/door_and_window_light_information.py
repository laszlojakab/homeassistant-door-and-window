""" The module contains the DoorAndWindowLightInformation class. """
from shapely.geometry.polygon import Polygon


class DoorAndWindowLightInformation:
    """
    Contains information about sun light received by a door and window.
    """

    def __init__(
        self,
        angle_of_incidence: float,
        sunny_glazing_area_polygon: Polygon,
    ):
        """
        Initialize a new instance of LightInformation class.

        Args:
            angle_of_incidence:
                The angle of incidence. If it is between 0 and 90 degrees
                then the door and window is faceing to sun.
                Otherwise the sun is behind the door and window.
            sunny_glazing_area_polygon:
                The glazing sunny area polygon.
        """
        self._angle_of_incidence = angle_of_incidence
        self._sunny_glazing_area_polygon = sunny_glazing_area_polygon

    @property
    def sunny_glazing_area_polygon(self) -> Polygon:
        """
        Gets the glazing sunny area polygon.
        """
        return self._sunny_glazing_area_polygon

    @property
    def angle_of_incidence(self) -> float:
        """
        Gets the angle of incidence. If it is between 0 and 90 degrees
        then the door and window is faceing to sun.
        Otherwise the sun is behind the door and window.
        """
        return self._angle_of_incidence
