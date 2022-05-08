""" Module for Awning class. """
from typing import Callable
from .event_handler import EventHandler

# pylint: disable=too-many-instance-attributes


class Awning():
    """ Represents an awning """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        width: float,
        min_depth: float,
        max_depth: float,
        # pylint: disable=invalid-name
        x: float,
        # pylint: disable=invalid-name
        y0: float,
        # pylint: disable=invalid-name
        y1: float,
        # pylint: disable=invalid-name
        z: float,
        cover_position: float
    ):
        """
        Initialize a new instance of Awning class.

        Args:
            width:
                The width of the awning.
            min_depth:
                The minimum depth of the awning when it is closed.
            max_depth:
                The maximum depth of the awning when it is opened.
            x:
                The distance between the center of the awning and the center of the door and window.
            y0:
                The distance between the top of the door and window
                and the awning at close to the wall.
            y1:
                The distance between the top of the door and window
                and the awning at far from the wall.
            z:
                The distance between the awning and the wall.
            cover_position:
                The initial awning position. 100 means opened, 0 means closed.
        """
        self._width = width
        self._min_depth = min_depth
        self._max_depth = max_depth
        self._x = x
        self._y0 = y0
        self._y1 = y1
        self._z = z
        self._cover_position = cover_position
        self._current_depth_changed = EventHandler()

    @property
    def width(self) -> float:
        """ Gets the width of the awning. """
        return self._width

    @property
    def min_depth(self) -> float:
        """ Gets the minimum depth of the awning when it is closed. """
        return self._min_depth

    @property
    def max_depth(self) -> float:
        """ Gets the maximum depth of the awning when it is opened. """
        return self._max_depth

    # pylint: disable=invalid-name
    @property
    def x(self) -> float:
        """
        Gets the distance between the center of the awning
        and the center of the door and window.
        """
        return self._x

    # pylint: disable=invalid-name
    @property
    def y0(self) -> float:
        """
        Gets the distance between the top of the door and window
        and the awning at close the wall.
        """
        return self._y0

    # pylint: disable=invalid-name
    @property
    def y1(self) -> float:
        """
        Gets the distance between the top of the door and window
        and the awning at far from the wall.
        """
        return self._y1

    # pylint: disable=invalid-name
    @property
    def z(self) -> float:
        """ Gets the distance between the awning and the wall. """
        return self._z

    @property
    def cover_position(self) -> float:
        """
        Gets or sets the cover position of the awning.
        100 means opened, 0 means closed.
        """
        return self._cover_position

    @cover_position.setter
    def cover_position(self, value: float) -> None:
        if value != self._cover_position:
            self._cover_position = value
            self._current_depth_changed.fire(self.current_depth)

    @property
    def current_depth(self) -> float:
        """
        Gets the current depth of the awning based on the current position.
        """
        return self.min_depth + (self.max_depth - self.min_depth) * self.cover_position / 100.0

    def on_current_depth_changed(
        self,
        callback: Callable[[float], None]
    ) -> Callable[[], None]:
        """
        Calls the specified function whenever the current_depth property has changed.

        Args:
            callback:
                The function to call when current_depth property has changed.

        Returns:
            A function to stop calling the callback function
            when current_depth property has changed.
        """
        return self._current_depth_changed.listen(callback)

    def dispose(self):
        """
        Destroys the current instance.
        """
        self._current_depth_changed.dispose()
