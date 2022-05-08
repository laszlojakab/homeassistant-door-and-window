""" The module of AwningToRectangleConverter class. """
from ..models.awning import Awning
from ..models.quadrilateral import Quadrilateral

# pylint: disable=too-few-public-methods
class AwningToRectangleConverter():
    """
    Responsible for converting awning to a rectangle.
    """

    @classmethod
    def convert(cls, awning: Awning) -> Quadrilateral:
        """
        Converts the specified Awning instance to a Quadrilateral instance.

        Args:
            awning
                The awning to convert.

        Returns:
            The Rectangle instance which represents the awning in the 3D space.
        """
        return Quadrilateral(
            [awning.x - awning.width / 2, awning.y0, -awning.z],
            [awning.x + awning.width / 2, awning.y0, -awning.z],
            [awning.x + awning.width / 2, awning.y1, -awning.z - awning.current_depth],
            [awning.x - awning.width / 2, awning.y1, -awning.z - awning.current_depth],
        )
