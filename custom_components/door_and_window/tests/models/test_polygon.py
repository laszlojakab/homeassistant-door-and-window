""" Test cases for polygons. """
from ...models.polygon import Polygon, Vertex, MultiPolygon


def test_polygon_area():
    """Tests the area property of polygons."""
    polygon = Polygon([Vertex(0, 0), Vertex(0, 10), Vertex(10, 10), Vertex(10, 0)])
    assert polygon.area == 100.0

    polygon = Polygon()
    assert polygon.area == 0.0

    polygon = Polygon([Vertex(0, 0)])
    assert polygon.area == 0.0

    polygon = Polygon([Vertex(0, 0), Vertex(10, 10), Vertex(20, 0)])
    assert polygon.area == 20 * 10 / 2

    # TODO: create tests for multipolygon


def test_subtract_1():
    """Test case 1 of subtraction."""
    polygon1 = Polygon(
        [
            Vertex(161, 137),
            Vertex(429, 376),
            Vertex(558, 192),
            Vertex(619, 418),
            Vertex(281, 431),
        ]
    )

    polygon2 = Polygon(
        [
            Vertex(183, 391),
            Vertex(224, 240),
            Vertex(610, 107),
            Vertex(657, 361),
            Vertex(429, 376),
        ]
    )

    result = polygon1 - polygon2

    expected = MultiPolygon(
        [
            Polygon(
                [
                    Vertex(261.867222318, 226.95248557436787),
                    Vertex(429.0, 376.0),
                    Vertex(262.690140845, 386.1408450704268),
                    Vertex(215.627162458, 270.8365480205366),
                    Vertex(224, 240),
                ]
            ),
            Polygon(
                [
                    Vertex(429.0, 376.0),
                    Vertex(558, 192),
                    Vertex(604.546479034, 364.45088953723683),
                ]
            ),
        ]
    )

    assert result == expected


def test_subtract_2():
    """Test case 2 of subtraction."""
    polygon_1 = Polygon(
        [
            Vertex(281, 159),
            Vertex(472, 155),
            Vertex(569, 248),
            Vertex(506, 419),
            Vertex(242, 366),
        ]
    )

    polygon_2 = Polygon(
        [
            Vertex(149, 241),
            Vertex(282, 72),
            Vertex(559, 111),
            Vertex(628, 406),
            Vertex(418, 475),
            Vertex(170, 407),
        ]
    )

    result = polygon_1 - polygon_2

    expected = Polygon(
        [
            Vertex(281, 159),
            Vertex(472, 155),
            Vertex(569, 248),
            Vertex(506, 419),
            Vertex(242, 366),
        ]
    )

    assert result == expected
