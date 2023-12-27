""" Module of polygon classes. """
from abc import ABC, abstractmethod
from dataclasses import dataclass
import math
from typing import Final, Iterable
from .polygon_cut import decode, PolyClipping, encode

ABSOLUTE_TOLERANCE = 0.001

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

    def __eq__(self, other: object) -> bool:
        # TODO: put it back...
        # if not isinstance(other, Vertex):
        #     return False

        return math.isclose(
            other.x, self.x, abs_tol=ABSOLUTE_TOLERANCE
        ) and math.isclose(other.y, self.y, abs_tol=ABSOLUTE_TOLERANCE)


class PolygonBase(ABC):
    """Base class of polygons."""

    @abstractmethod
    def __sub__(self, other):
        ...


class Polygon(PolygonBase):
    """Represents a polygon."""

    def __init__(self, vertexes: Iterable[Vertex] = iter([])):
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

    def __sub__(self, other):
        if not isinstance(other, PolygonBase):
            raise ValueError("subtraction not supported")

        S = decode([self.vertexes])
        C = decode([other.vertexes])

        result = [
            Polygon(encode(polygon_str)) for polygon_str in PolyClipping(S[0], C[0])
        ]
        if len(result) == 1:
            return result[0]
        if len(result) > 1:
            return MultiPolygon(result)
        # TODO: empty?
        raise ValueError()

    def __repr__(self) -> str:
        return f"Polygon({', '.join([vertex.__repr__() for vertex  in self.vertexes])})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Polygon):
            return False

        if len(other.vertexes) != len(self.vertexes):
            return False

        for idx, item in enumerate(self.vertexes):
            if item != other.vertexes[idx]:
                return False

        return True


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

    def __repr__(self) -> str:
        return f"MultiPolygon({', '.join([polygon.__repr__() for polygon  in self.polygons])})"

    def __sub__(self, other):
        if not isinstance(other, PolygonBase):
            raise ValueError("subtraction not supported")

        simple_polygons: list[Polygon]
        if isinstance(other, Polygon):
            simple_polygons = [other]
        elif isinstance(other, MultiPolygon):
            simple_polygons = other.polygons
        else:
            raise ValueError("Unknown polygon type")

        result: list[Polygon] = []

        raise NotImplementedError("TODO")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MultiPolygon):
            return False

        if len(other.polygons) != len(self.polygons):
            return False

        for idx, item in enumerate(self.polygons):
            if item != other.polygons[idx]:
                return False

        return True
