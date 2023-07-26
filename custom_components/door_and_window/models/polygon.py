""" Module of polygon classes. """
from abc import ABC
from dataclasses import dataclass
from typing import Final, Iterable

# pylint: disable=too-few-public-methods
@dataclass
class Vertex:
    """Represents a vertex (2D point)"""

    # pylint: disable=invalid-name
    x: Final[float]
    """X coordinate of the vertex."""

    # pylint: disable=invalid-name
    y: Final[float]
    """Y coordinate of the vertex."""

    def __repr__(self) -> str:
        return f"(x={self.x}, y={self.y})"


class PolygonBase(ABC):
    """Base class of polygons."""


class Polygon(PolygonBase):
    """Represents a polygon."""

    def __init__(self, vertexes: Iterable[Vertex]):
        """
        Initializes a new instance of `Polygon` class.

        Args:
            vertexes:
                Vertexes of the polygon.
        """

        def compute_signed_area(polygon: list[Vertex]) -> float:
            """Computes the signed area of a polygon using the shoelace formula."""
            number_of_vertexes = len(polygon)
            area = 0.0
            for i in range(number_of_vertexes):
                j = (i + 1) % number_of_vertexes
                area += polygon[i].x * polygon[j].y - polygon[j].x * polygon[i].y

            return 0.5 * area

        vertexes_list = list(vertexes)
        signed_area = compute_signed_area(vertexes_list)

        self.area: Final[float] = abs(signed_area)
        """ The area of the polygon. """

        # If signed area is positive then polygon is defined by vertexes in clockwise
        # otherwise it is defined in counter clockwise so we rotate it.
        self.vertexes: Final[Iterable[Vertex]] = (
            vertexes_list if signed_area > 0 else vertexes_list[::-1]
        )
        """ The vertexes of the polygon in clockwise order. """


class MultiPolygon(PolygonBase):
    """Represents multiple polygons."""

    def __init__(self, polygons: Iterable[Polygon]):
        """
        Initializes a new instance of `MultiPolygon` class.

        Args:
            polygons:
                The part of the multi polygon.
        """
        self.polygons = list(polygons)
