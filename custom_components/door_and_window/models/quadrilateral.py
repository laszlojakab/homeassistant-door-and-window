""" The module contains Quadrilateral  class. """
from typing import Any, List

import numpy as np


class Quadrilateral():
    """ Represents an immutable quadrilateral (4 sided shape) in the 3D space."""

    def __init__(
        self,
        corner_1: List[float],
        corner_2: List[float],
        corner_3: List[float],
        corner_4: List[float]
    ):
        """
        Initialize a new instance of Quadrilateral .

        Args:
            corner_1:
                the coordinates of the 1st corner [x, y, z]
            corner_2:
                the coordinates of the 2nd corner [x, y, z]
            corner_3:
                the coordinates of the 3rd corner [x, y, z]
            corner_4:
                the coordinates of the 4th corner [x, y, z]
        """
        self._corner_1: np.ndarray = np.append(corner_1, [1])
        self._corner_2: np.ndarray = np.append(corner_2, [1])
        self._corner_3: np.ndarray = np.append(corner_3, [1])
        self._corner_4: np.ndarray = np.append(corner_4, [1])

    @property
    def corner_1(self) -> np.ndarray:
        """ The coordinates of the 1st corner. """
        return self._corner_1

    @property
    def corner_2(self) -> np.ndarray:
        """ The coordinates of the 2nd corner. """
        return self._corner_2

    @property
    def corner_3(self) -> np.ndarray:
        """ The coordinates of the 3rd corner. """
        return self._corner_3

    @property
    def corner_4(self) -> np.ndarray:
        """ The coordinates of the 4th corner. """
        return self._corner_4

    def __str__(self):
        """ Gets the string representation of the instance. """
        return f"[\n{self.corner_1}\n{self._corner_2}\n{self._corner_3}\n{self._corner_4}\n]"

    def apply_matrix(self, matrix: np.ndarray):
        """
        Applies the specified transformation matrix to the
        corner points of the quadrilateral and returns a new `Quadrilateral` instance.
        """
        return Quadrilateral(
            matrix.dot(self.corner_1)[:3],
            matrix.dot(self.corner_2)[:3],
            matrix.dot(self.corner_3)[:3],
            matrix.dot(self.corner_4)[:3]
        )

    def __eq__(self, other: Any):
        """Overrides the default implementation"""
        if isinstance(other, Quadrilateral):
            return (self.corner_1 == other.corner_1).all() and \
                    (self.corner_2 == other.corner_2).all() and \
                    (self.corner_3 == other.corner_3).all() and \
                    (self.corner_4 == other.corner_4).all()
        return False
