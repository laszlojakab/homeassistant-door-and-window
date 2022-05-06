""" Module for EventHandler class. """
from typing import Callable
from .event import Event

class EventHandler:
    """ Responsible for adding listeners to an event and firing the event. """
    def __init__(self):
        self._event = Event()

    def listen(self, callback: Callable[..., None]) -> Callable[[], None]:
        """
        Adds a listener to the event.

        Args:
            callback:
                The function to call whenever the event happens.

        Returns:
            The function to stop listening to the event.
        """
        self._event.add_listener(callback)

        def untrack():
            self._event.remove_listener(callback)

        return untrack

    def fire(self, *args, **kwargs) -> None:
        """ Fires the event with the specified arguments. """
        self._event(*args, **kwargs)

    def dispose(self) -> None:
        """ Removes all the event listeners. """
        self._event.clear_event_listeners()
